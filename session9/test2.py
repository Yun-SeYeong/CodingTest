def get_num(path, c, target, result_path):
    result = []
    for i in range(len(path)):
        if path[i][0] == c and path[i][1] not in result_path:
            t = path.copy()
            del t[i]
            if path[i][1] == target:
                print("result_path: ", result_path)
                result.append(result_path)
            else:
                rp = result_path.copy()
                rp.append(path[i][1])
                data = get_num(t, path[i][1], target, rp)
                if len(data) > 0:
                    for d in data:
                        result.append(d)
    return result


if __name__== '__main__':
    first = [int(n) for n in input().split(" ")]
    path = []
    for i in range(first[1]):
        path.append([int(n) for n in input().split(" ")])

    print(path)
    print(len(get_num(path, 1, first[0], [1])))
