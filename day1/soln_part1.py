"""
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.

The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.
"""

def result(mass: int) -> int:
    return mass // 3 - 2


assert result(12) == 2
assert result(14) == 2
assert result(1969) == 654
assert result(100756) == 33583

with open('input.txt') as f:
    data = [int(item.strip()) for item in f]

print(sum([result(mass) for mass in data]))
