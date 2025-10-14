# Macrosoft
In this task we are tasked with counting calories of pizzas that calorie counting maniacs want to order.

We are presented with a website and a server. When connecting to the server we receive a message which states the size and base of the pizza along with its toppings. Then we are asked for the calorie count. Testing this server a bit it looks like we only ever get Medium sized pizzas, so let's start by only solving for that size. 

If we take a look at the website we can see the menu which includes all pizzas and their toppings and in the footer there is a button labeled _Nutritional Values_ which provides us with the nutritional information of all pizzas on the menu in a PDF file. 

Using this information we can easily figure out the calories of all bases by looking at the nutritional information of _The Plain Jane_ pizza since it has no toppings. Next we have to figure out the calories of each of the toppings. We can easily figure out the calorie values of pepperoni and mushrooms since _Pepperoni Classic_ and _Mushroom Magic_ only have those toppings added to the base. As an example we can figure out that the mushroom topping is 20 calories since.

```
Classic Medium Mushroom Magic - Classic Medium The Plain Jane = 720 - 700 = 20
```

It is possible to solve for each of the toppings by continuing this manual approach but it quickly turns into an annoying task. However from doing this we realize that the pizzas can be modeled as linear equations with the toppings being the unknowns ad coefficients being the amount of each topping, for example a Bacon (double) has a coefficient of 2.

This means we can set this up as a system of linear equations and solve for $x$ in $Ax = b$. In this equation $A$ is a matrix where each row is a **Classic Medium** pizza from the menu and each column is a topping and the value is the amount of each topping, 0 meaning it isn't on the pizza, 1 meaning it is, and 2 meaning it is doubled. $b$ is a vector which contains the calories of each of the menu pizzas. Finally $x$ is a vector representing the calorie count of each of the toppings.

However the system is inconsistent since $A$ is overdetermined, however we can remove The Plain Jane since it has no toppings and we are only interested in the calorie count of the toppings. This means we can instead solve for $x$ in $A'x = b'$ where $A'$ is the same matrix excluding The Plain Jane and $b'$ is a modified vector where we subtract the base from each of the values, leaving only the calories of the toppings. 

Now we just have to get the toppings from the website (either through the UI or through the JSON document), the calorie counts from the PDF, set up the system of equations and we can solve the system with help from [SymPy's](https://docs.sympy.org/latest/index.html) `linsolve` function.

```python
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
```

And we get the following solution:
```
ham             60
pineapple       40
bacon           180
pepperoni       150
spicy beef      130
ground beef     110
extra cheese    120
chicken         90
mushrooms       20
onions          15
green peppers   A - 45
black olives    85 - A
fresh tomatoes  12
green olives    A - 20
feta cheese     A + 15
spinach         63 - A
sweetcorn       80 - A
anchovies       A
jalapenos       5
```

We can see that most of the unknowns are solved but that there are still a number of unknowns which depend on the value of anchovies. We can reduce inequalities and figure out the range of possible values for anchovies. This can be easily done with the `reduce_inequalities` function from `SymPy`. 

```python
anchovies = list(set(tuple(x.free_symbols) for x in solution))[0]

inequalities = []
for expr_for_topping in solution:
    if expr_for_topping != S.Zero:
        inequalities.append(expr_for_topping > 0)

anchovies_bounds = reduce_inequalities(inequalities, anchovies).as_set()
```

And we get the following $45 < anchovies < 63$. This means there are only 7 values for us to try, assuming a valid solution is a integer. We can see that all the solved toppings are integers and using the "nice number" heuristic for constructed problems we can confidently assume that there are no fractionals expected of us. In any case these are just 7 values to try so we can easily bruteforce this, evaluate the values for each possible value for anchovies and try, if it fails increment the number and try again. 

After some attempts we land on anchovies being 55 calories and are able to solve all of the pizza counting questions presented by the server, giving us the flag. 
