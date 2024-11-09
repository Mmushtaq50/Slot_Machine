import random
import tkinter as tk
from tkinter import messagebox

MAX_LINES = 4  # Maximum lines a player can bet on
MAX_BET = 100
MIN_BET = 1

ROWS = 4
COLS = 4

# Adjusted symbol counts to fit a 4x4 grid
symbol_count = {
    "A": 3,
    "B": 5,
    "C": 7,
    "D": 9
}

# Define payouts for each symbol
symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    result = ""
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                result += column[row] + " | "
            else:
                result += column[row] + " "
        result += "\n"
    return result


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        match = all(symbol == column[line] for column in columns)

        if match:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine Game")

        self.balance = 0
        self.lines = 0
        self.bet = 0

        # Labels and entries for deposit and bet
        self.balance_label = tk.Label(root, text="Balance: $0")
        self.balance_label.pack()

        self.deposit_label = tk.Label(root, text="Enter Deposit Amount:")
        self.deposit_label.pack()
        self.deposit_entry = tk.Entry(root)
        self.deposit_entry.pack()

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.lines_label = tk.Label(root, text=f"Enter the number of lines to bet on (1-{MAX_LINES}):")
        self.lines_label.pack()
        self.lines_entry = tk.Entry(root)
        self.lines_entry.pack()

        self.bet_label = tk.Label(root, text="Enter Bet Amount:")
        self.bet_label.pack()
        self.bet_entry = tk.Entry(root)
        self.bet_entry.pack()

        self.spin_button = tk.Button(root, text="Spin", command=self.spin)
        self.spin_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def deposit(self):
        amount = self.deposit_entry.get()
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                self.balance += amount
                self.balance_label.config(text=f"Balance: ${self.balance}")
            else:
                messagebox.showerror("Error", "Amount must be greater than 0.")
        else:
            messagebox.showerror("Error", "Please enter a valid number.")

    def spin(self):
        try:
            self.lines = int(self.lines_entry.get())
            if not 1 <= self.lines <= MAX_LINES:
                messagebox.showerror("Error", "Invalid number of lines. Enter a number between 1 and 4.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of lines.")
            return

        try:
            self.bet = int(self.bet_entry.get())
            if not MIN_BET <= self.bet <= MAX_BET:
                messagebox.showerror("Error", f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid bet amount.")
            return

        total_bet = self.bet * self.lines
        if total_bet > self.balance:
            messagebox.showerror("Error", f"You don't have enough balance. Current balance: ${self.balance}")
            return

        self.balance -= total_bet
        self.balance_label.config(text=f"Balance: ${self.balance}")

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        result = print_slot_machine(slots)
        self.result_label.config(text=result)

        winnings, winning_lines = check_winnings(slots, self.lines, self.bet, symbol_values)
        self.balance += winnings

        if winnings > 0:
            messagebox.showinfo("You Win!", f"You won ${winnings}! Winning lines: {', '.join(map(str, winning_lines))}")
        else:
            messagebox.showinfo("You Lose", "No winning lines. Try again!")

        self.balance_label.config(text=f"Balance: ${self.balance}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()
