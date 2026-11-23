from time import sleep

print("contador bumerangue")
for i in range(1, 11):
    sleep(1)
    print("\033[H\033[J")
    print(i)

for i in range(10, 0, -1):
    sleep(1)
    print("\033[H\033[J")
    print(i)
