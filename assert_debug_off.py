x = 30
y = 20
z = 10

max_value = z if z > y else y if y > z else x

assert max_value == 30
