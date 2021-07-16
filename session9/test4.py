def get_num(m):
    if len(m) <= 0:
        return []

    result = []
    for k in m:
        result.append(k)

    for i in range(len(result)):
        for d in get_num(m[result[i]]):
            result.append(d)

    return result


if __name__ == '__main__':
    m = {
        1: {
            2: {
                4: {},
                5: {}
            },
            3: {
                6: {},
                7: {}
            }
        }
    }

    print(get_num(m))
