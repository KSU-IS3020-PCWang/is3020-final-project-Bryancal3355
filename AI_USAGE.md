# AI Improvement Record

## Original Development

Explain how you developed the original version and describe any AI assistance used before the first required commit. AI use during this stage should be minimal.
## Original Development

I started from my Final Project Proposal, which outlined the required
functions: add_transaction, view_transactions, calculate_category_totals,
check_budget_status, save_transactions, load_transactions,
delete_transaction, and main_menu. I used Claude to help generate the
initial implementation of these functions based on my proposal's Python
Concepts and Data Plan section. I reviewed the generated code, ran it in
PyCharm, and tested each menu option (adding, viewing, deleting
transactions, checking totals and budget status, and confirming data
saved to and loaded from the CSV file correctly) before making the
"Original working version before AI improvement" commit.
## AI Tools Used
Claude
List each AI tool used while improving the application.

## Improvements Requested

Describe the important prompts or requests you gave the AI. Do not paste a complete chat transcript.
After my original version was working and committed, I asked Claude to
review the code and improve it. Specifically, I asked for:
- Docstrings and comments explaining what each function does
- Better input validation (e.g., rejecting negative amounts)
- A way to reduce repeated try/except code used for validating numbers
- One of the optional features listed in my proposal to be added
## Changes Accepted

For each major accepted change, explain what changed, why you accepted it, and how you verified that you understood it.
- Added docstrings to every function. I accepted this because the
  rubric requires major functions to be explained with comments or
  docstrings, and it makes the code easier to read.
- Added a get_valid_amount() helper function used by add_transaction and
  get_budget to validate numeric input and reject negative numbers. I
  accepted this because it removed duplicated try/except logic. I
  verified it worked by testing invalid text, negative numbers, and
  valid numbers in both places it's used.
- Added a get_valid_index() helper function shared by delete_transaction
  and edit_transaction to validate the transaction number entered by the
  user. I verified it by testing a valid number, an out-of-range number,
  and non-numeric text.
- Added edit_transaction(), a new feature that lets the user update a
  transaction's description, amount, or category without deleting and
  re-adding it. This was listed as an optional improvement in my
  original proposal, so I accepted it. I tested it by editing an
  existing transaction's amount and category and confirming the changes
  were saved correctly in transactions.csv.
- Replaced the long if/elif chain in main_menu with a dictionary that
  maps each menu choice to its function. I accepted this because it
  shortened the menu logic and made it easier to add the new edit
  option. I verified it by testing all seven menu options and confirming
  each one still triggered the correct function.

## Changes Rejected or Revised

Describe any AI suggestion you rejected or modified and explain why.
I did not reject any of the suggested changes. All of the improvements
matched what I had asked for, and I tested each one myself in PyCharm
before including it in the final version to make sure I understood how
it worked and that it didn't break anything from the original version.

## What I Learned

Explain what you learned by reviewing and applying the AI-assisted improvements.
I learned how helper functions like get_valid_amount() and
get_valid_index() can remove repeated code, since the same validation
logic was originally copy-pasted in more than one function. I also
learned how a dictionary can replace a long if/elif chain by mapping
menu choices directly to functions, which I hadn't used before. Writing
docstrings for each function also helped me think more clearly about
what each function was actually responsible for before I added new
features.