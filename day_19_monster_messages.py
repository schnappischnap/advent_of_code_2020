import re


def part_1(data):
    rules = dict()
    for line in data[:131]:
        rule_id, rule = line.split(":")
        rules[int(rule_id)] = rule.split()

    def expand_rule(rule_id):
        rule = rules[rule_id]
        expanded = ""
        for c in rule:
            if c.startswith('"'):
                return c[1]
            if c == "|":
                expanded += "|"
            else:
                expanded += f"({expand_rule(int(c))})"
        return f"({expanded})"

    pattern = "".join(expand_rule(0))
    return sum(re.fullmatch(pattern, line.strip()) is not None
               for line in data[132:])


def part_2(data):
    rules = dict()
    for line in data[:131]:
        rule_id, rule = line.split(":")
        rules[int(rule_id)] = rule.split()

    def expand_rule(rule_id):
        if rule_id == 8:
            return f"{expand_rule(42)}+"
        if rule_id == 11:
            # Don't know how big the range needs to be, but 10 worked for my input.
            return "|".join(f"{expand_rule(42)}{{{n}}}{expand_rule(31)}{{{n}}}"
                            for n in range(1, 10))

        rule = rules[rule_id]
        expanded = ""
        for c in rule:
            if c.startswith('"'):
                return c[1]
            if c == "|":
                expanded += "|"
            else:
                expanded += f"({expand_rule(int(c))})"
        return f"({expanded})"

    pattern = expand_rule(0)
    return sum(re.fullmatch(pattern, line.strip()) is not None
               for line in data[132:])


if __name__ == '__main__':
    with open('day_19_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
