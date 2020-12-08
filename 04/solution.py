from typing import List, Dict


def load(file):
    with open(file, "r") as f:
        return [x for x in f.readlines()]


def transform_entries_into_dic(lines: List[str]):
    res = []
    tmp = {}
    for l in lines:
        if l == '\n':
            res.append(tmp)
            tmp = {}
            continue
        entries = l.split(" ")
        for e in entries:
            entry = e.split(":")
            tmp[entry[0].strip()] = entry[1].strip()
    return res


def check_passport(passport : Dict):
    # cid opt ?
    demanded_entries = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    for d in demanded_entries:
        if d not in passport.keys():
            print(passport)
            print("Length - ", str(len(passport.keys())))
            print("Missing - ", d )
            print("=============================")
            if d == "cid":
                return True
            return False
    return True


def check_all_entries(passports):
    valid_counter = 0
    for p in passports:
        if check_passport(p):
            valid_counter += 1
    return valid_counter


def main():
    all_entries_dic = transform_entries_into_dic(load("inpoot.txt"))
    count = check_all_entries(all_entries_dic)
    return count


if __name__ == '__main__':
    print(main())
