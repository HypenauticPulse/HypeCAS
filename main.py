import input

[eq, var] = input.get_input()

power = eq.split(var)[1].split(" ")[0].split("^")[1]

print(power)
