n = int(input("Enter a counter n as an int: "))
under = 1.0
over = 1.0
for i in range(n):
    under /= 2
    over *= 2
    print(f"loop {i+1} under {under} over {over}")
