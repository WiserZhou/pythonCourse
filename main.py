def is_non_ascii(char):
    """判断一个字符是否为非ASCII字符"""
    return ord(char) >= 128


def main():
    s = input("输入句子:")  # 输入字符串
    non_ascii_chars = ""  # 存储非ASCII字符
    ascii_chars = ""  # 存储ASCII字符
    last_was_non_ascii = False  # 标记变量，用于控制空格插入

    for char in s:
        if is_non_ascii(char):  # 判断是否为非ASCII字符
            if not last_was_non_ascii:
                ascii_chars += ' '  # 插入空格
            non_ascii_chars += char  # 将非ASCII字符添加到non_ascii_chars
            last_was_non_ascii = True
        else:
            ascii_chars += char  # 将ASCII字符添加到ascii_chars
            last_was_non_ascii = False

    print("非ASCII字符:", non_ascii_chars)  # 输出非ASCII字符组成的字符串
    print("ASCII字符:", ascii_chars)  # 输出ASCII字符组成的字符串，并在不同类型字符间插入空格


if __name__ == "__main__":
    main()
