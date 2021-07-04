if __name__ == "__main__":
    s = input()

    result = ""

    prev = ""
    count = 1
    for c in s:
        if prev != "":
            if prev != c:
                result += (prev + (str(count) if count > 1 else ""))
                count = 1
            else:
                count += 1
        prev = c

    result += (prev + (str(count) if count > 1 else ""))

    print(result)
