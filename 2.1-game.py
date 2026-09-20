import random

MAX_POINTS = 21

def draw_card(sum:int) -> int:
    result: int = random.randint(1,11)
    sum += result
    print(f"Drew {result}, new total: {sum}")
    return sum

def try_luck():
    print("\nGame start!")
    sum: int = 0
    bust: bool = False

    sum = draw_card(sum)

    # a for loop with like 100 iterations would be more lore-accurate here
    while bust == False:
        choice = int(input("Draw again? (1/0): "))
        if choice == 1:
            sum = draw_card(sum)

            if sum > MAX_POINTS:
                print("You lose!")
                bust = True

        else:
            print(f"Final total: {sum}")
            break

play_again: int = 1
while play_again == True:
    try_luck()

    play_again = int(input("\nPlay again? (1/0): "))