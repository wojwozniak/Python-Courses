# FCC Course: Scientific Computing with Python
# Project: Budget App
# Author: Wojciech Woźniak
# Date: 12.05.2023


# Definition of Category class
class Category:

    # Constructor of Category class
    def __init__(self, label):
        # Sets the label of the category and creates an empty ledger for it
        self.label = label
        self.ledger = []

    # get_balance() method

    def get_balance(self):
        # Calculates the current balance of the category by summing up all amounts in the ledger
        current_sum = 0
        for element in self.ledger:
            current_sum += element['amount']
        return current_sum

    # check_funds() method

    def check_funds(self, amount):
        # Checks if the amount is less than or equal to the current balance of the category
        # Returns True if yes, False otherwise
        return amount <= self.get_balance()

    # deposit() method

    def deposit(self, amount, description=""):
        # Adds a deposit entry to the ledger for the given amount and description
        self.ledger.append({"amount": amount, "description": description})

    # withdraw() method

    def withdraw(self, amount, description=""):
        # Checks if the amount is less than or equal to the current balance of the category
        # If yes, adds a withdrawal entry to the ledger for the given amount and description, and returns True
        # If no, returns False
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    # transfer() method

    def transfer(self, amount, obj):
        # Checks if the amount is less than or equal to the current balance of the category
        # If yes, adds a transfer entry to both the current category and the target category's ledgers,
        # and returns True. If no, returns False.
        if self.withdraw(amount, "Transfer to " + obj.label):
            obj.deposit(amount, "Transfer from " + self.label)
            return True
        else:
            return False

    # __str__() method

    def __str__(self):
        # Create top string - 30 characters long with label in the middle
        output = f"{self.label.center(30, '*')}\n"
        # Calculate the total amount by summing all the amounts in the ledger
        total = sum(item['amount'] for item in self.ledger)
        # Iterate over each item in the ledger and add it to the output
        for item in self.ledger:
            # Add the description of the item, left-justified and truncated to 23 characters
            output += f"{item['description'][:23].ljust(23)}"
            # Add the amount of the item, right-justified with a width of 7 and 2 decimal places
            output += f"{item['amount']:>7.2f}\n"
        # Add the total amount to the output
        output += f"Total: {total:.2f}"
        # Return the final output string
        return output


# Definition of create_spend_chart() function
def create_spend_chart(categories):
    # Initialize variables and output
    total_expenses = 0
    category_expenses = []
    category_labels = []
    max_label_length = 0
    output = "Percentage spent by category\n"

    # Calculate total expenses for each category and find length of longest label
    for category in categories:
        category_expense = sum([-transaction['amount']
                               for transaction in category.ledger if transaction['amount'] < 0])
        total_expenses += category_expense

        if len(category.label) > max_label_length:
            max_label_length = len(category.label)

        category_expenses.append(category_expense)
        category_labels.append(category.label)

    # Convert expenses to percentages and pad labels
    category_expenses = [(expense / total_expenses) *
                         100 for expense in category_expenses]
    category_labels = [label.ljust(max_label_length, " ")
                       for label in category_labels]

    # Build chart with 10% increments
    for percentage in range(100, -1, -10):
        output += str(percentage).rjust(3, " ") + '|'
        for expense in category_expenses:
            output += " o " if expense >= percentage else "   "
        output += " \n"

    # Add label row to chart
    output += "    " + "---" * len(category_labels) + "-\n"
    for i in range(max_label_length):
        output += "    "
        for label in category_labels:
            output += " " + label[i] + " "
        output += " \n"

    return output.strip("\n")
