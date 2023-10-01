""" """
MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    score = int(input("Enter score: "))
    get_valid_score(score)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            if score < 0 or score > 100:
                print("Invalid score")
                score = int(input("Enter score: "))
            print("Score is valid")
        elif choice == "P":
            determine_result(score)
            print(determine_result(score))
        elif choice == "S":
            print(score_as_stars(score))
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished.")


def get_valid_score(score):
    while score < 0 or score > 100:
        print("Invalid score, try again")
        score = int(input("Enter score: "))
    return score


def determine_result(score):
    if score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    elif score <= 100:
        return "Excellent"
    else:
        return "Invalid score"


def score_as_stars(score):
    return '*' * score


main()
