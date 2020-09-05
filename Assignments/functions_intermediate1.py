import random
def randInt(min= 0, max= 100):
    if min > max:
        return "Min is greater than min"
    if max < 0:
        return "Max is less than 0"
    num = random.random() * (max-min) + min
    return num

print(randInt())            # should print a random integer between 0 to 100
print(randInt(max=50))      # should print a random integer between 0 to 50
print(randInt(min=50))      # should print a random integer between 50 to 100
print(randInt(min=50, max=500)) # should print a random integer between 50 and 500
print(randInt(min=50, max=5))
print(randInt(min=-50, max=-5))