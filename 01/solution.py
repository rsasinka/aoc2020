
with open("inpoot.txt", "r") as inpoot:
    numbers = list(map(int, inpoot.readlines()))

    for num in numbers:
        for n in numbers:
            # print(num, n, num + n)
            if num + n == 2020:
                print(num, n, num * n)
                break



    for num in numbers:
        for nu in numbers:
            for n in numbers:
            # print(num, n, num + n)
                if num + nu + n == 2020:
                    print(num, nu, n, num * n * nu)
