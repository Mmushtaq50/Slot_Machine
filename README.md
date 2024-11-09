# Slot_Machine
A Python-based slot machine game where users deposit money, choose the number of lines to bet on, and place bets per line. The game simulates a 4x4 grid spin, displays the results, and calculates winnings based on matching symbols. Perfect for anyone wanting to experience a virtual slot machine!

Overall Plan of the Code
The code simulates a slot machine game where:
    The user deposits money to play.
    They select the number of lines they want to bet on.
    They place a bet per line, and the total bet is deducted from their balance.
    A "spin" generates random symbols in a 4x4 grid (since we’re using 4 rows and 4 columns).
    The result is displayed, and winnings (if any) can be calculated based on matches.

Function-by-Function Breakdown:
----------------------------------------------------------------------------------------------
symbol_count:
  This dictionary defines the number of each symbol in the “pool” that the machine can pull from. By assigning different 
   counts, you control how likely each symbol is to appear in the columns.
   symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
    }
----------------------------------------------------------------------------------------------
get_slot_machine_spin:
This function randomly generates a "spin" by creating columns of symbols based on symbol_count.
Steps:
    Create a list of all possible symbols: all_symbols has each symbol repeated according to its count in symbol_count.
    Generate columns: For each column, pick symbols randomly (without replacement) from all_symbols. This simulates the “spin.” 
----------------------------------------------------------------------------------------------
print_slot_machine:
This function displays the columns in a grid format so that the player can see the result of their spin.
Steps:
    For each row in the columns, print symbols horizontally with | between them for formatting.
----------------------------------------------------------------------------------------------
deposit:
Handles user deposits. It repeatedly prompts the user until they enter a valid positive integer.
----------------------------------------------------------------------------------------------
get_number_of_lines:
Allows the user to choose how many lines they want to bet on. The value must be between 1 and MAX_LINES.
----------------------------------------------------------------------------------------------
get_bet:
This function asks the player how much they want to bet per line. It ensures the bet is within the allowed range (MIN_BET to MAX_BET).
----------------------------------------------------------------------------------------------
main:
This is the main game loop where everything comes together.
Steps:
    Get the deposit amount.
    Ask for the number of lines to bet on.
    Ask for the bet per line, then calculate the total_bet.
    Check if the total_bet exceeds the balance; if not, proceed.
    Call get_slot_machine_spin to generate a spin.
    Print the result with print_slot_machine.
----------------------------------------------------------------------------------------------

    In the slot machine game, the idea is that for you to win, the same symbol (like "A", "B", "C", "D") must appear in the same column for the number of lines you bet on. Here's a summary:

    Matching Symbols in a Column: The game checks if all symbols in a specific column are the same for the given row. For instance, if the first column has the symbols ["A", "A", "A", "A"], this is a match for all 4 rows, meaning it is a winning column.

    Matching Symbols Across the Chosen Number of Lines: The number of lines you choose to bet on determines how many rows you are betting across. The game will check if the symbols in the same row across all the columns are the same.

For example:

    If you bet on 2 lines:
        The first line (row 1) will check if symbols in each column of that row are the same.
        The second line (row 2) will check for the same condition.
    If the symbols match on those lines, you win, and your winnings are based on the symbol's value.

To clarify the winning condition:

    You win if you have matching symbols across all columns for the chosen line.
    If you have matching symbols in a column, it counts as a win for the lines where the symbols align.
