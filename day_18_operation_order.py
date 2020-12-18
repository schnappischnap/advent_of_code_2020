from math import prod


def part_1(data):
    def calculate(expr):
        while "(" in expr:
            start = expr.index("(")
            for i, c in enumerate(expr[start:], start=start):
                if c == "(":
                    start = i
                elif c == ")":
                    value = str(calculate(expr[start+1:i]))
                    expr = expr[:start] + [value] + expr[i+1:]
                    break
        
        total = int(expr[0])
        for op, i in zip(expr[1::2], expr[2::2]):
            if op == "+":
                total += int(i)
            elif op == "*":
                total *= int(i)
        return total
    
    return sum(calculate(line.replace("(", "( ").replace(")", " )").split())
               for line in data) 


def part_2(data):
    def calculate(expr):
        while "(" in expr:
            start = expr.index("(")
            for i, c in enumerate(expr[start:], start=start):
                if c == "(":
                    start = i
                elif c == ")":
                    value = str(calculate(expr[start+1:i]))
                    expr = expr[:start] + [value] + expr[i+1:]
                    break

        while "+" in expr:
            i = expr.index("+")
            value = str(int(expr[i-1]) + int(expr[i+1]))
            expr = expr[:i-1] + [value] + expr[i+2:]

        return prod(int(c) for c in expr[::2])

    return sum(calculate(line.replace("(", "( ").replace(")", " )").split())
               for line in data)





if __name__ == '__main__':
    with open('day_18_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
