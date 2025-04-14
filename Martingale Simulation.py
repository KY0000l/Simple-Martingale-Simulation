import random

def simulate_martingale(odds, starting_money, initial_bet, total_turns):
    balance = starting_money
    current_bet = initial_bet
    last_balance = starting_money

    print(f"Starting simulation with balance: ${balance:.2f}")
    print("-" * 60)

    for turn in range(1, total_turns + 1):
        if balance < current_bet:
            print(f"Turn {turn}: Not enough money to bet. Current balance: ${balance:.2f}, required: ${current_bet:.2f}")
            break

        balance -= current_bet

        if random.random() < odds:
            # win
            winnings = 2 * current_bet
            balance += winnings
            current_bet = initial_bet
        else:
            # loss
            current_bet *= 2

        change = balance - last_balance
        percent_change = (change / last_balance) * 100 if last_balance != 0 else 0

        print(f"Turn {turn:3d} - Balance: ${balance:.2f} - Change: ${change:.2f} ({percent_change:.2f}%)")

        last_balance = balance

    print("-" * 60)
    print(f"Final balance after {turn} turns: ${balance:.2f}")

if __name__ == '__main__':
    try:
        odds = float(input("Enter the odds of winning (e.g. 0.1 for 10%): "))
        starting_money = float(input("Enter starting money: "))
        initial_bet = float(input("Enter initial bet: "))
        total_turns = int(input("Enter total number of turns: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    else:
        simulate_martingale(odds, starting_money, initial_bet, total_turns)

    input("\nPress Enter to exit...")
