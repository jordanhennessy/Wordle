from colorama import Fore


def main():
    answer = "HELLO"
    guess = ""
    lives = 6

    while guess != answer and lives > 0:
        guess = str(input(Fore.BLUE + "Guess: ").upper())
        status = ["_", "_", "_", "_", "_"]

        try:
            if len(guess) > 5 or len(guess) < 5:
                raise Exception

            for i in range(len(guess)):
                if guess[i] in answer:
                    if guess[i] == answer[i]:
                        status[i] = str(Fore.GREEN + guess[i])
                    else:
                        status[i] = str(Fore.YELLOW + guess[i])
                else:
                    status[i] = str(Fore.RED + guess[i])

            output(status)

            lives -= 1

        except:
            print(Fore.BLUE + "Your guess must be 5 letters")

    if lives == 0:
        lose(answer)
    else:
        win(answer)


def lose(answer):
    print(Fore.BLUE + "You lost! The word was", answer, "Better luck next time")
    repeater()


def win(answer):
    print(Fore.BLUE + "Congratulations you won! The word was", answer)
    repeater()


def repeater():
    if repeat():
        main()
    else:
        input("Press enter to exit")


def repeat():
    choice = ""

    while choice.lower() != "y" and choice.lower() != "n":
        try:
            choice = input("Play again? (Y/N): ")
            if choice.lower() != "y" and choice.lower() != "n":
                raise Exception
            if choice.lower() == "y":
                return True
            else:
                return False
        except:
            print("Press Y to play or N to quit")


def output(status):
    out = ""
    for i in status:
        out += i
    print(out)


if __name__ == '__main__':
    main()
