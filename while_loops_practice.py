# Brayden Waugh
# 25 September 2017

done = False
while not done:
    print("1 - Sum of even numbers from 1 to 100")
    print("2 - Sum of squares of the numbers from 1 to 15")
    print("3 - Exit")
    answer = int(input("Please select an action: "))
    if answer == 1:
        print("Processing option 1...")

        num = 0
        total = 0

        while num <= 100:
             if num % 2 == 0:
                total = total + num
             num += 1
        print(total)
        print("")
    elif answer == 2:
        print("Processing option 2...")

        num = 0
        total = 0

        while num <= 15:
            total = total + num ** 2
            num += 1
        print(total)
        print("")
    elif answer == 3:
        print("Exiting...")
        done = True
    else:
        print("Invalid choice")
        print("")