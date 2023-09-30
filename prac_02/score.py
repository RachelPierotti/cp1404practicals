"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    """Score status determination"""
    score = float(input("Enter score: "))
    determine_score_status(score)
    print(determine_score_status(score))


def determine_score_status(score):
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


main()
