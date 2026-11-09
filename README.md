# Game Theory: Strategic Pricing Model

An interactive Python program that models two competing firms choosing between **High Price** and **Low Price** strategies.

## Features

- Accepts hypothetical profits for all four strategy combinations.
- Displays a payoff matrix as `(Firm A profit, Firm B profit)`.
- Finds all pure-strategy Nash equilibria.
- Handles invalid numeric input.

A Nash equilibrium occurs when neither firm can increase its profit by changing its strategy alone.

## Requirements

Python 3. No external libraries required.

## How to Run

Save the code as `pricing_game.py`, then run:

```bash
python pricing_game.py
```

Enter each firm’s payoff when prompted. The program displays the payoff matrix and any pure-strategy Nash equilibria.

## Limitations

Supports two firms with two strategies each. Mixed-strategy equilibria are not calculated.
