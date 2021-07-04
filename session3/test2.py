if __name__ == "__main__":
    s = input().lower()

    filtered_s = ""

    for c in s:
        if (ord("a") <= ord(c) <= ord("z")) or (ord("A") <= ord(c) <= ord("Z")):
            filtered_s += c

    filtered_reversed_s = filtered_s[::-1]
    hals_l = int(len(filtered_s) / 2)

    if filtered_s[:hals_l] == filtered_reversed_s[:hals_l]:
        print("YES")
