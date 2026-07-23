# IS 3020 Final Project

## Student and Project Information

- Student name: Bryan Calderon  
- GitHub username: Bryan Cal 3355
- Project title: Pocket Ledger
- Application purpose: A command-line personal budget and expense tracker that lets a user log transactions, categorize spending, check remaining budget, and save/load data from a CSV file.

## How to Run the Application

Explain the required Python version, required files, and the exact steps for starting the application in PyCharm.
1. Open the project in PyCharm.
2. Run `pocket_ledger.py`.
3. Enter your monthly budget when prompted.
4. Use the menu to add, view, edit, delete transactions, view category
   totals, or check your budget status.
5. Choose option 7 to exit. All data is saved automatically to
   `data/transactions.csv`.
## Major Features

List the major user-facing features implemented in the final application.
- Add a transaction (date, description, amount, category)
- View all recorded transactions in a table
- Edit an existing transaction
- Delete a transaction
- View spending totals broken down by category
- Check remaining budget vs. monthly limit
- Transactions persist between sessions via a CSV file
## Python Concepts Used

Explain how the application uses functions, collections, conditionals, loops, file persistence, and exception handling.
- Functions to separate each piece of logic
- Lists of dictionaries to store transactions in memory
- Loops to iterate through transactions for totals, display, and search
- Conditionals to validate input and compare spending to budget
- try/except blocks to catch invalid numeric input
- File I/O (csv module) to save and load data between sessi
## Data Files

Describe each CSV or JSON file and provide a brief explanation of its fields.
`data/transactions.csv` — one row per transaction with columns:
date, description, amount, category.

## Testing Summary

Describe the major scenarios tested, including invalid input and file-related errors.
Tested adding transactions with valid and invalid amounts, deleting and
editing transactions by valid and invalid index numbers, viewing an
empty transaction list, checking budget status when under and over
budget, and confirming data persists correctly after closing and
reopening the program.
## AI Use

Complete `AI_USAGE.md` and summarize the most important AI-assisted improvements here.
See `AI_USAGE.md` for full details. Claude was used after the working
version was complete to add docstrings/comments, add input validation
helpers, and add the edit_transaction feature.