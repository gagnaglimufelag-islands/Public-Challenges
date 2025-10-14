import re
from pathlib import Path

import yaml
from pwn import *
from sympy import Eq, S, linsolve, symbols
from sympy.solvers.inequalities import reduce_inequalities

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]
PIZZA_RE = re.compile(r"^Medium ([^\s]+) pizza with (.*)$")
BASES = {
    "classic": 700,
    "italian": 500,
    "pan": 1300,
}


def attempt_solution(domain, port, cal_map):
    def parse(topping):
        multiplier = 2 if "(double)" in topping else 1
        return cal_map[topping.replace(" (double)", "").strip()] * multiplier

    r = remote(domain, port)
    r.recvline()

    while pizza := r.recvline().decode():
        if "gg{" in pizza:
            return (True, pizza)

        if pizza_match := PIZZA_RE.match(pizza):
            base = pizza_match.group(1)
            calories = 0
            toppings = pizza_match.group(2)
            if "no toppings" in toppings:
                calories = BASES[base]
            else:
                calories = BASES[base] + sum(
                    parse(topping.strip()) for topping in toppings.split(",")
                )
            r.recvuntil("Calories: ")
            r.sendline(str(calories).encode())
        else:
            print(f"Failed with Anchovies guess of {cal_map['anchovies']} calories")
            return (False, "")


def test(domain, port):
    topping_names = [
        "ham",
        "pineapple",
        "bacon",
        "pepperoni",
        "spicy beef",
        "ground beef",
        "extra cheese",
        "chicken",
        "mushrooms",
        "onions",
        "green peppers",
        "black olives",
        "fresh tomatoes",
        "green olives",
        "feta cheese",
        "spinach",
        "sweetcorn",
        "anchovies",
        "jalapenos",
    ]
    toppings = list(symbols("H Pi Ba Pe SB GB EC Ch M O GP BO FT GO Fe S Sw A J"))

    H, Pi, Ba, Pe, SB, GB, EC, Ch, M, O, GP, BO, FT, GO, FE, S_sym, Sw, A, J = toppings
    equations = [
        Eq(H + Pi, 100),
        Eq(2 * Ba, 360),
        Eq(Pe + H + SB + Ba + GB, 630),
        Eq(EC, 120),
        Eq(Ch + Ba, 270),
        Eq(M + O + GP + BO + FT, 87),
        Eq(BO + GO + FE + S_sym + FT, 155),
        Eq(Ch + FT + S_sym + GO, 145),
        Eq(M, 20),
        Eq(Pe, 150),
        Eq(2 * Pe, 300),
        Eq(H + GP + Sw + EC, 215),
        Eq(GB + Sw + GP, 145),
        Eq(A + BO, 85),
        Eq(S_sym + FE + O, 93),
        Eq(Pi + J + Ch, 135),
        Eq(Pe + M + O + GP + BO + H + Pi + SB + Ba + J, 640),
        Eq(Pe + M + O, 185),
        Eq(SB + J + O, 150),
    ]
    solution = list(linsolve(equations, toppings))[0]
    anchovies = list(set(tuple(x.free_symbols) for x in solution))[0]

    inequalities = []
    for expr_for_topping in solution:
        if expr_for_topping != S.Zero:
            inequalities.append(expr_for_topping > 0)

    anchovies_bounds = reduce_inequalities(inequalities, anchovies).as_set()
    print(anchovies_bounds)

    for val in range(anchovies_bounds.start + 1, anchovies_bounds.end):
        evaluated = [
            expr.subs(A, val) if hasattr(expr, "subs") else expr for expr in solution
        ]
        cal_map = dict(zip(topping_names, evaluated))
        succ, flag = attempt_solution(domain, port, cal_map)
        if succ:
            assert FLAG in flag, flag
            return


if __name__ == "__main__":
    test("127.0.0.1", 32000)
