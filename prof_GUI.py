import random
import pygame
import sys

# Constants
MAX_LINES = 4
MAX_BET = 100
MIN_BET = 1
ROWS = 4
COLS = 4

# Symbol counts and payouts
symbol_count = {
    "A": 3,
    "B": 5,
    "C": 7,
    "D": 9
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slot Machine Game")

# Font for rendering text
font = pygame.font.Font(None, 36)


# Function to get a random slot machine spin
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


# Function to print slot machine grid with colored rectangles
def draw_slot_machine_grid(slots):
    slot_width = 75  # Adjusted to make boxes smaller
    slot_height = 75  # Adjusted to make boxes smaller
    for i in range(ROWS):
        for j in range(COLS):
            symbol = slots[j][i]
            # Choose a color for each symbol
            if symbol == "A":
                color = (255, 0, 0)  # Red
            elif symbol == "B":
                color = (0, 255, 0)  # Green
            elif symbol == "C":
                color = (0, 0, 255)  # Blue
            else:  # "D"
                color = (255, 255, 0)  # Yellow

            pygame.draw.rect(screen, color,
                             (50 + j * (slot_width + 20), 50 + i * (slot_height + 20), slot_width, slot_height))
            # Optionally, draw the symbol text on the rectangle
            symbol_text = font.render(symbol, True, (0, 0, 0))  # Black text
            screen.blit(symbol_text, (50 + j * (slot_width + 20) + 30, 50 + i * (slot_height + 20) + 25))


# Function to check winnings
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


# Function for user deposit
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")


# Function for selecting number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")


# Function for getting the bet amount
def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")


# Main function for the game
def main():
    balance = deposit()
    print(f"You have deposited ${balance}.")

    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    balance -= total_bet

    # Now initialize the Pygame window
    screen.fill((0, 0, 0))  # Clear screen

    # Get the slot machine spin
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)

    # Draw the slot machine grid
    draw_slot_machine_grid(slots)

    # Update the display
    pygame.display.update()

    # Check winnings
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    balance += winnings

    print(f"\nYou won ${winnings}.")
    if winning_lines:
        print(f"You won on lines: {', '.join(map(str, winning_lines))}")
    else:
        print("No winning lines this time.")

    print(f"Your balance is now ${balance}.")

    # Wait for a short period before quitting
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()


# Run the game
main()
