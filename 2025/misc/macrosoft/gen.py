KJ_MULTIPLIER = 4.184

bases = {
    "Classic": {"calories": 700, "fat": 30, "carbs": 80, "protein": 20},
    "Italian": {"calories": 500, "fat": 20, "carbs": 60, "protein": 15},
    "Pan": {"calories": 1300, "fat": 60, "carbs": 150, "protein": 35},
}

toppings = {
    "Pepperoni": {"calories": 150, "fat": 12, "carbs": 1, "protein": 7},
    "Mushrooms": {"calories": 20, "fat": 0.3, "carbs": 3, "protein": 1},
    "Onions": {"calories": 15, "fat": 0.1, "carbs": 3, "protein": 0.5},
    "Green Peppers": {"calories": 10, "fat": 0.1, "carbs": 2, "protein": 0.3},
    "Black Olives": {"calories": 30, "fat": 2.5, "carbs": 1, "protein": 0.3},
    "Green Olives": {"calories": 35, "fat": 3, "carbs": 1, "protein": 0.3},
    "Ham": {"calories": 60, "fat": 3, "carbs": 1, "protein": 8},
    "Pineapple": {"calories": 40, "fat": 0.1, "carbs": 10, "protein": 0.5},
    "Extra Cheese": {"calories": 120, "fat": 9, "carbs": 1, "protein": 7},
    "Spicy Beef": {"calories": 130, "fat": 9, "carbs": 2, "protein": 10},
    "Ground Beef": {"calories": 110, "fat": 8, "carbs": 1, "protein": 9},
    "Bacon": {"calories": 180, "fat": 15, "carbs": 1, "protein": 10},
    "Chicken": {"calories": 90, "fat": 5, "carbs": 0, "protein": 10},
    "Jalapenos": {"calories": 5, "fat": 0.1, "carbs": 1, "protein": 0.2},
    "Sweetcorn": {"calories": 25, "fat": 0.5, "carbs": 5, "protein": 1},
    "Spinach": {"calories": 8, "fat": 0.1, "carbs": 1, "protein": 1},
    "Feta Cheese": {"calories": 70, "fat": 6, "carbs": 1, "protein": 4},
    "Anchovies": {"calories": 55, "fat": 3, "carbs": 0, "protein": 9},
    "Fresh Tomatoes": {"calories": 12, "fat": 0.1, "carbs": 2.5, "protein": 0.5},
}

pizzas = [
    {
        "name": "The Plain Jane",
        "toppings": [],
    },
    {
        "name": "Pepperoni Classic",
        "toppings": ["Pepperoni"],
    },
    {
        "name": "Mushroom Magic",
        "toppings": ["Mushrooms"],
    },
    {
        "name": "Cheesus Crust",
        "toppings": ["Extra Cheese"],
    },
    {
        "name": "Garden Delight",
        "toppings": [
            "Mushrooms",
            "Onions",
            "Green Peppers",
            "Black Olives",
            "Fresh Tomatoes",
        ],
    },
    {
        "name": "Aloha Special",
        "toppings": ["Ham", "Pineapple"],
    },
    {
        "name": "Carnivore Carnival",
        "toppings": ["Pepperoni", "Ham", "Spicy Beef", "Bacon", "Ground Beef"],
    },
    {
        "name": "Volcano Blast",
        "toppings": ["Spicy Beef", "Jalapenos", "Onions"],
    },
    {
        "name": "Pepperoni Overload",
        "toppings": ["Pepperoni", "Pepperoni"],
    },
    {
        "name": "Cluck & Oink",
        "toppings": ["Chicken", "Bacon"],
    },
    {
        "name": "Greek Getaway",
        "toppings": [
            "Black Olives",
            "Green Olives",
            "Feta Cheese",
            "Spinach",
            "Fresh Tomatoes",
        ],
    },
    {
        "name": "Salty Sailor",
        "toppings": ["Anchovies", "Black Olives"],
    },
    {
        "name": "Sweet Heat Wave",
        "toppings": ["Pineapple", "Jalapenos", "Chicken"],
    },
    {
        "name": "Trio Treat",
        "toppings": ["Pepperoni", "Mushrooms", "Onions"],
    },
    {
        "name": "Quad Combo",
        "toppings": ["Ham", "Green Peppers", "Sweetcorn", "Extra Cheese"],
    },
    {
        "name": "Spinach Feta Fusion",
        "toppings": ["Spinach", "Feta Cheese", "Onions"],
    },
    {
        "name": "Rancher's Choice",
        "toppings": ["Ground Beef", "Sweetcorn", "Green Peppers"],
    },
    {
        "name": "Bacon Bonanza (double)",
        "toppings": ["Bacon", "Bacon"],
    },
    {
        "name": "Lean & Green Bird",
        "toppings": ["Chicken", "Fresh Tomatoes", "Spinach", "Green Olives"],
    },
    {
        "name": "The Kitchen Sink",
        "toppings": [
            "Pepperoni",
            "Mushrooms",
            "Onions",
            "Green Peppers",
            "Black Olives",
            "Ham",
            "Pineapple",
            "Spicy Beef",
            "Bacon",
            "Jalapenos",
        ],
    },
]


def calc_macro(macro, base, size, toppings_list):
    size_multiplier = 1 if size == "Med" else 1.5
    return bases[base][macro] * size_multiplier + sum(
        toppings[topping][macro] * size_multiplier for topping in toppings_list
    )

pizzas = sorted(pizzas, key=lambda x: x["name"])
typst_dict = ["("]
for pizza in pizzas:
    typst_dict.append(f'"{pizza["name"]}": (')
    print(f"{pizza["name"]} - {", ".join(pizza["toppings"])}")
    for base, calories in bases.items():
        for size in ["Med", "Large"]:
            calories = calc_macro("calories", base, size, pizza["toppings"])
            kj = calories * KJ_MULTIPLIER
            fat = calc_macro("fat", base, size, pizza["toppings"])
            carbs = calc_macro("carbs", base, size, pizza["toppings"])
            protein = calc_macro("protein", base, size, pizza["toppings"])
            typst_dict.append(f'("{base}", "{size}", {calories}, {kj}, {fat}, {carbs}, {protein}), ')
            print(f"\t{base} {size}: {calories} - {fat} - {carbs} - {protein}")
    typst_dict.append("),\n")

typst_dict.append(")")
print("".join(typst_dict))
