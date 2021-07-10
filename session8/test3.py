def search_num1(n):
    if n == "":
        return n
    result = ""
    for k in n:
        result += (k + search_num1(n[k]))

    return result


def search_num2(n):
    print("=====")
    print(n)

    root_key = list(n.items())[0][0]
    root_value = list(n.items())[0][1]
    print("root_key", root_key)
    print("root_value", root_value)

    if root_value == "":
        return root_key

    left_key = list(root_value.items())[0][0]
    print("left_key", left_key)
    left_value = list(root_value.items())[0][1]
    print("left_value", left_value)

    right_key = list(root_value.items())[1][0]
    print("right_key", right_key)
    right_value = list(root_value.items())[1][1]
    print("right_value", right_value)

    left = search_num2({left_key: left_value})
    right = search_num2({right_key: right_value})

    print("left: ", left)
    print("right: ", right)

    return left + root_key + right


def search_num3(n):
    if n == "":
        return n
    result = ""
    for k in n:
        result += search_num3(n[k])
        result += k

    return result


if __name__== '__main__':
    N = {
        "1": {
                "2": {
                    "4": "",
                    "5": ""
                },
                "3": {
                    "6": "",
                    "7": ""
                }
            }
    }

    print(search_num1(N))
    print(search_num2(N))
    print(search_num3(N))
