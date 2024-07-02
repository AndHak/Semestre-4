print((9-3)/(2*(1+2)))

def greater_value(x, y):
    if x > y:
        return x
    else:
       return y


print(greater_value(10,3*5))

num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)

genre = "transcendental"
print(genre[:-8])
print(genre[-7:9])