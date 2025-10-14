import os
import random
import sys

FLAG = os.environ.get("FLAG", "falg{this-is-a-broken-flag-contact-admins}")

BASES = {
    "classic": 700,
    "italian": 500,
    "pan": 1300,
}

TOPPINGS = {
    "pepperoni": 150,
    "mushrooms": 20,
    "onions": 15,
    "green peppers": 10,
    "black olives": 30,
    "green olives": 35,
    "ham": 60,
    "pineapple": 40,
    "extra cheese": 120,
    "spicy beef": 130,
    "ground beef": 110,
    "bacon": 180,
    "chicken": 90,
    "jalapenos": 5,
    "sweetcorn": 25,
    "spinach": 8,
    "feta cheese": 70,
    "anchovies": 55,
    "fresh tomatoes": 12,
}


def parse(topping):
    multiplier = 2 if "(double)" in topping else 1
    return TOPPINGS[topping.replace(" (double)", "").strip()] * multiplier


def cals(base, pizza_toppings):
    return BASES[base] + sum(parse(topping) for topping in pizza_toppings)


print("HELP! HELP! HELP! HELP! TELL ME THE CALORIES NOW!")
for _ in range(100):
    base = random.choice(list(BASES.keys()))
    toppings = []

    for _ in range(random.randint(0, 19)):
        topping = random.choice(list(TOPPINGS.keys()))
        toppings.append(
            f"{topping} (double)"
        ) if random.random() < 0.02 else toppings.append(topping)

    print(
        f"Medium {base} pizza with {', '.join(toppings) if toppings else 'no toppings'}"
    )

    try:
        user_input = int(input("Calories: "))
        correct_cals = cals(base, toppings)

        if user_input != correct_cals:
            print("Wrong! Gains have been lost!")
            sys.exit(1)

    except ValueError:
        print("That's not how calories work!")
        sys.exit(1)


print(FLAG)
