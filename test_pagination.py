pagination = 0
while True:
    print("Simulation API avec un offset de ", pagination)
    pagination = pagination + 100
    if pagination >= 1500:
        break
    