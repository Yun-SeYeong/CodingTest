if __name__ == '__main__':
    s = input()
    half_len = int(len(s)/2)
    print(half_len)
    print(half_len - (half_len % 2))
    print(s[half_len - (1 - len(s) % 2): half_len+1])
