
# Game Theory: Interactive Strategic Decision Model
# Two competing firms choosing pricing strategies

strategies = ["High Price", "Low Price"]
payoffs = {}

print("=" * 50)
print("GAME THEORY: STRATEGIC PRICING MODEL")
print("=" * 50)

print("\nTwo firms can choose:")
print("1. High Price")
print("2. Low Price")

print("\nEnter the payoffs for each combination.")
print("Payoffs represent hypothetical profits.\n")

# Step 1: Get user inputs
for firm_a in strategies:
    for firm_b in strategies:

        print(f"\nFirm A: {firm_a} | Firm B: {firm_b}")

        while True:
            try:
                profit_a = float(input("Firm A payoff: "))
                profit_b = float(input("Firm B payoff: "))
                break
            except ValueError:
                print("Invalid input. Please enter numbers.")

        payoffs[(firm_a, firm_b)] = (profit_a, profit_b)

# Step 2: Display payoff matrix
print("\n" + "=" * 50)
print("PAYOFF MATRIX")
print("=" * 50)

print(f"{'Firm A / Firm B':<20}{'High Price':<20}{'Low Price':<20}")

for a in strategies:
    print(f"{a:<20}", end="")
    for b in strategies:
        print(f"{str(payoffs[(a, b)]):<20}", end="")
    print()

# Step 3: Find Nash equilibria
print("\n" + "=" * 50)
print("NASH EQUILIBRIUM ANALYSIS")
print("=" * 50)

equilibria = []

for (a, b), (profit_a, profit_b) in payoffs.items():

    # Firm A's best payoff given Firm B's choice
    best_a = max(
        payoffs[(s, b)][0] for s in strategies
    )

    # Firm B's best payoff given Firm A's choice
    best_b = max(
        payoffs[(a, s)][1] for s in strategies
    )

    if profit_a == best_a and profit_b == best_b:
        equilibria.append((a, b, profit_a, profit_b))

# Step 4: Display the results
if equilibria:
    for a, b, profit_a, profit_b in equilibria:
        print(f"\nFirm A's Strategy: {a}")
        print(f"Firm B's Strategy: {b}")
        print(f"Firm A's Payoff: {profit_a:g}")
        print(f"Firm B's Payoff: {profit_b:g}")
else:
    print("No pure-strategy Nash equilibrium found.")

print("\nAnalysis complete!")