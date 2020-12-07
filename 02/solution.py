def load(file):
    with open(file, "r") as f:
        return f.readlines()


def checker(line: str):
    line_sep = line.split(" ")

    min_n = int(line_sep[0].split("-")[0])
    max_n = int(line_sep[0].split("-")[1])
    letter = line_sep[1][0]
    # 3-10 h: xcvxkdqshh
    password = line_sep[2].strip()
    return min_n <= password.count(letter) <= max_n


def checker_part2(line: str):
    line_sep = line.split(" ")
    min_n = int(line_sep[0].split("-")[0]) - 1
    max_n = int(line_sep[0].split("-")[1]) - 1
    letter = line_sep[1][0]
    password = line_sep[2].strip()

    if min_n > len(password) or max_n > len(password):
        return False

    pos1 = password[min_n] == letter
    pos2 = password[max_n] == letter
    # print(pos1, pos2, pos1 != pos2)
    return pos1 != pos2  # xor


def part1():
    passwords = load("inpoot.txt")
    counter = 0
    for p in passwords:
        if checker(p):
            counter += 1
    print("valid passwords - " + str(counter))


def part2():
    passwords = load("inpoot.txt")
    counter = 0
    for p in passwords:
        if checker_part2(p):
            counter += 1
    print("part2 valid passwords - " + str(counter))

if __name__ == '__main__':
    part2()
    # print(checker_part2("1-3 c: abc"))
    # print(checker_part2("1-4 a: abc"))