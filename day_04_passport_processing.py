import re


def part_1(data):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return sum(all(field in passport for field in fields)
               for passport in data.split("\n\n"))


def part_2(data):
    def is_valid(passport):
        return (1920 <= int(passport.get("byr", 0)) <= 2002 and
                2010 <= int(passport.get("iyr", 0)) <= 2020 and
                2020 <= int(passport.get("eyr", 0)) <= 2030 and
                ((passport.get("hgt", "").endswith("cm") and
                  150 <= int(passport["hgt"][:-2]) <= 193) or
                 (passport.get("hgt", "").endswith("in") and
                  59 <= int(passport["hgt"][:-2]) <= 76)) and
                passport.get("hcl", "").startswith("#") and len(passport["hcl"]) == 7 and
                passport.get("ecl", "") in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and
                len(passport.get("pid", "")) == 9)

    passports = [dict(field.split(":") for field in re.split(r"\s", passport))
                 for passport in data.split("\n\n")]

    return sum(is_valid(passport) for passport in passports)
    

if __name__ == '__main__':
    with open('day_04_input.txt', 'r') as f:
        inp = f.read()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
