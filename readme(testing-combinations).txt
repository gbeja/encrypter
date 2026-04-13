🍽️ Meal Combination Generator
📌 Overview

This Python program generates all possible combinations of meals, drinks, and desserts using nested loops. It demonstrates the concept of a Cartesian product in programming.

⚙️ How It Works

The program iterates through three lists:

Meals
Drinks
Desserts

For every meal, it pairs with every drink and every dessert, producing all possible combinations.

💻 Code Example
meal = ["pizza", "burger", "chicken"]
drink = ["coke", "fanta", "sprite"]
dessert = ["ice cream", "cake", "donut"]

for m in meal:
    for d in drink:
        for ds in dessert:
            print(f"I want to eat {m} and drink {d} and eat {ds}")
▶️ Output Example
I want to eat pizza and drink coke and eat ice cream
I want to eat pizza and drink coke and eat cake
I want to eat pizza and drink coke and eat donut
...
📁 Project Structure
project/
│
├── meals.py
└── README.md
🚀 Features
Generates all meal-drink-dessert combinations
Simple nested loop logic
Beginner-friendly Python example
Easy to modify and extend
🔮 Possible Improvements
Add random meal generator
Allow user input for menu items
Export combinations to a file (CSV/TXT)
Convert to web app or API
Use itertools.product for cleaner implementation

⚠️ Note

This is a learning project meant to demonstrate loops and combinations, not a production system.
