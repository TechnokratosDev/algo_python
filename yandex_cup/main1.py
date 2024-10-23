if __name__ == '__main__':
    dict = {}
    sum_ = 0
    count = 0

    str_ = input()
    while str_ != "!":
        data = str_.split(" ")

        if data[0] == "+":
            dict[data[1]] = float(data[2])
            count += 1
            sum_ += float(data[2])
        elif data[0] == "-":
            count -= 1
            sum_ -= dict[data[1]]
            del dict[data[1]]
        elif data[0] == "~":
            sum_ += float(data[2])
            sum_ -= dict[data[1]]
            dict[data[1]] = float(data[2])
        elif data[0] == "?":
            if count == 0:
                print(round(0, 9), flush=True)
            else:
                print(round(sum_ / count, 9), flush=True)

        str_ = input()
