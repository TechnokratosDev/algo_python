if __name__ == '__main__':
    drakkars_count, cart_weight = map(int, input().split(" "))
    drakkar_lens: list = list(map(int, input().split(" ")))
    playground = []

    drakkars = []
    for i in range(drakkars_count):
        drakkar_stacks = []
        for j in range(drakkar_lens[i]):
            stack: list[int] = list(map(int, input().split(" ")))

            drakkar_stacks.append([])
            for k in range(stack[0], 0, -1):
                drakkar_stacks[j].append(stack[k])

        drakkars.append(drakkar_stacks)

    current_weight = 0
    current_num = 1
    while k > -1:
        k, l = -1, -1

        # пытаемся найти такое на площадке
        if current_num in playground:
            p_num = playground.index(current_num)
            print(2, p_num)
            current_weight += 1
            playground.pop(p_num)
            k = 0
            continue

        # пытаемся найти такое же где-то ещё
        for i in range(drakkars_count):
            for j in range(drakkar_lens[i]):
                if drakkars[i][j] and current_num in drakkars[i][j]:
                    k, l, num = i, j, drakkars[i][j].index(current_num)

                    if len(playground) + (len(drakkars[k][l]) - num + 1) <= 4:
                        while drakkars[k][l][-1] != current_num:
                            temp = drakkars[k][l].pop()
                            print(1, k + 1, l + 1, len(playground) + 1)
                            playground.append(temp)
                        print(1, k + 1, l + 1, 0)
                        current_weight += 1
                        drakkars[k][l].pop()

                        if current_weight == cart_weight:
                            print(3)
                            current_weight = 0
                        continue

        if any([len(x) for j in drakkars for x in j]) and not any([current_num in x for j in drakkars for x in j]):
            if current_weight > 0:
                print(3)
                current_weight = 0
            current_num += 1
            k = 0

    if current_weight > 0:
        print(3)
    print(0)

#
# 1 3
# 5
# 3 1 2 3
# 3 3 3 3
# 3 1 3 3
# 3 2 1 3
# 3 2 3 3