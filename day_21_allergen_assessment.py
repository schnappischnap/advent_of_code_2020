from collections import defaultdict


def solve(data):
    possible = defaultdict(set)
    ingredient_count = defaultdict(int)

    for line in data:
        ingredients, allergens = line.split(" (contains ")
        ingredients = ingredients.split()
        allergens = allergens.strip(" \n)").split(", ")
        for allergen in allergens:
            if allergen not in possible:
                possible[allergen] = set(ingredients)
            else:
                possible[allergen].intersection_update(ingredients)
        for ingredient in ingredients:
            ingredient_count[ingredient] += 1
    
    while any(len(allergens) > 1 for allergens in possible.values()):
        for allergens, ingr in possible.items():
            if len(ingr) == 1:
                possible = {k: (v.difference(ingr) if k != allergens else v)
                            for k, v in possible.items()}

    unsafe_ingredients = [list(allergens)[0] for allergens in possible.values()]
    safe_ingredients = [ingredient for ingredient in ingredient_count.keys() 
                                   if ingredient not in unsafe_ingredients]

    part_1 = sum(ingredient_count[ingredient] for ingredient in safe_ingredients)
    part_2 = ",".join(list(item[1])[0] for item in sorted(possible.items()))

    return part_1, part_2


def part_2(data):
    return None


if __name__ == '__main__':
    with open('day_21_input.txt', 'r') as f:
        inp = f.readlines()
        part_1, part_2 = solve(inp)
        print("Part 1 answer: " + str(part_1))
        print("Part 2 answer: " + str(part_2))
