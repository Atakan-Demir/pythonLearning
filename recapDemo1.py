import random

lights = ["red","yellow","green"]

x = random.randint(0,2)
currentLight = lights[x]

print(currentLight)

if currentLight == "red":
    print("STOP!")
elif currentLight == "yellow":
    print("READY!")
elif currentLight == "green":
    print("GO!")