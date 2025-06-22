# Minecraft Pickaxe Durability Calculator

A simple web-based tool to calculate the probabilities associated with Minecraft pickaxe durability, specifically factoring in the "Unbreaking" enchantment. Have you ever wondered if your Unbreaking III pickaxe will survive mining 10,000 blocks? This tool can tell you!

## Live Demo

You can try out the calculator directly in your browser using the link below:
* [Main Page](https://svyrydov-ihor.github.io/mc-pickaxe-calculator/)
* [Probability Calculator](https://svyrydov-ihor.github.io/mc-pickaxe-calculator/probability.html): Calculate probability of not breaking pickaxe after mining specified amount of blocks.

## How it works

This project uses a combination of standard HTML for the user interface and Python for the core logic. The statistical calculations are performed by a Python script that is executed in the browser using PyScipt.

The formula for a tool with Unbreaking echantment is that it has a `1 / (level + 1)` chance that using the tool reduces durability.
