def playgame():
    min = 1
    max = 100
    count = 0
    import random
    target = random.randint(min,max)
    print(target)

    print("====game====\n")
    while True:
        try:
            keyin = int(input(f"guess number {min}~{max}: "))
        except:
            print("wrong format")
            count +=1
            print(f"total {count} times")
        else:
            count +=1
            if keyin >= min and keyin <= max:
                if keyin == target:
                    print(f'Correct, the number is: {target}')
                    print(f"total {count} times")
                    break
                elif keyin > target:
                    print(f"Smaller, total {count} times")
                    max = keyin -1
                elif keyin < target:
                    print(f"larger, total {count} times")
                    min = keyin + 1
            else:
                print("wrong range")
                print(f"total {count} times")

while (True):
    playgame()
    playagain = input("again? y,n")
    if playagain == 'n':
        break

print("game over")