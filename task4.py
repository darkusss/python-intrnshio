import sqlite3


def create_cities_dict():
    cities_dict = {}
    with open('city_list.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            if line.find(';') and 'Country' not in line:
                country, city, city_id = line.replace('"', '').split(';')
                city_id = city_id.replace('\n', '')
                if not cities_dict.get(country):
                    cities_dict[country] = [[city, city_id]]
                else:
                    cities_dict[country].append([city, city_id])
    return cities_dict


def create_db_with_table_city_data():
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS city(
            city_id integer primary key,
            country text,
            city text
        )""")

    for key, value in create_cities_dict().items():
        sql_values = []
        for a in value:
            sql_values.append('({0},"{1}","{2}")'.format(int(a[1]), key, a[0]))
        sql_insert = """INSERT INTO city(city_id, country, city) VALUES""" + ','.join(sql_values)
        print(sql_insert)
        try:
            cur.execute(sql_insert)
        except sqlite3.DatabaseError as err:
            print('Error: {}'.format(err))

    con.commit()
    cur.close()
    con.close()


create_db_with_table_city_data()
