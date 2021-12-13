from operator import itemgetter

if __name__ == '__main__':
    matrix = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]

    matrix = sorted(matrix, key=itemgetter(1))
    print(matrix)

    new_dict = {}
    for row in matrix:
        new_dict[row[1]] = [row[0], row[2], row[3]]
    print(new_dict)

    for row in matrix:
        new_dict[row[1]] = sorted(new_dict[row[1]], reverse=True)
    print(new_dict)

    flat_list = list()
    for value in new_dict.values():
        flat_list += value
    unique_values = set(flat_list)
    print(unique_values)

    stringify_values = ''
    for x in unique_values:
        stringify_values += str(x)
    print(stringify_values)
