# ayo what up peeps
# it's yo boy
# nubs
import random

def multiply(x, y):
    return x * y

def cool(name):
    if name is "Vero":
        print("You are cool.")
    elif name is "Ali":
        print("You're ok level cool.")
    else:
        print("You are not cool.")


# cool('Ali')
"""
names = ["Jack", "Adam", "Michael"]

 for name in names:
    print("My name is {}.".format(name))
"""


flip_amounts = 1000
total_heads = 0
total_tails = 0


for i in range(flip_amounts):
    # this can either be 0 or 1
    flip_result = random.randrange(2)
    if flip_result == 0:
        total_heads += 1
        print("You got Heads.")
    elif flip_result ==1:
        total_tails += 1
        print("You got Tails.")

print("You got a total of: {} heads.\n".format(total_heads))
print("You got a total of: {} tails.\n".format(total_tails))
