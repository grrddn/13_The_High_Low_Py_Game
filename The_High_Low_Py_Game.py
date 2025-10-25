import random

celebrities = [
    {
        'name': 'Ronaldo',
        'followers': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Katy Perry',
        'followers': 90,
        'description': 'Singer',
        'country': 'California'
    },
    {
        'name': 'Colapinto',
        'followers': 15,
        'description': 'Driver',
        'country': 'Argentina'
    },
    {
        'name': 'Checo',
        'followers': 85,
        'description': 'F1 Driver',
        'country': 'Mexico'
    },
]


def variable_a():
    x = random.randint(0, 3)
    return x


def variable_b():
    y = random.randint(0, 3)
    return y


def print_variable_a(x):
    return print(
        f"Compare A: {celebrities[x]['name']} a {celebrities[x]['description']} from {celebrities[x]['country']}")


def print_variable_b(y):
    return print(
        f"Compare B: {celebrities[y]['name']} a {celebrities[y]['description']} from {celebrities[y]['country']}")


def higher_lower():
    x = variable_a()
    a = celebrities[x]['followers']

    user_is_correct = True
    score = 0
    while user_is_correct == True:

        y = variable_b()
        while x == y:
            y = variable_b()
        b = celebrities[y]['followers']
        print_variable_a(x)
        print("    VS     ")
        print_variable_b(y)

        guess = input("Who has more followers? Type 'A' or 'B': \n").lower()

        if guess == 'a' and a > b:
            score += 1
            print(f"You're right\nYour current score is {score}\n")
            user_is_correct = True
        elif guess == 'b' and b > a:
            score += 1
            print(f"You're right\nYour current score is {score}\n")
            user_is_correct = True
            x = y
            a = celebrities[x]['followers']
        else:
            print(f"You're wrong\n\nYour final score is {score}\n")
            user_is_correct = False


print("""

WELCOME TO THE Higher_Lower PY GAME!!!!!

""")
higher_lower()