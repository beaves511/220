"""
NAME: Eric Beaver
interest.py

Problem: This program calculates the monthly interest charge on a credit card account.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    annual_interest = eval(input("Enter the annual interest rate: "))
    billing_cycle = eval(input("Enter the number of days in the billing cycle: "))
    net_balance = eval(input("Enter the previous net balance: "))
    amount = eval(input("Enter the payment amount: "))
    payment_day = eval(input("Enter the day of the billing cycle in which the payment was made: "))
    step_one = net_balance * billing_cycle
    step_two = amount * (billing_cycle - payment_day)
    step_three = step_one - step_two
    step_four = step_three / billing_cycle
    monthly_interest_charge = step_four * ((annual_interest / 12) / 100)
    print(round(monthly_interest_charge, 2))


if __name__ == "__main__":
    main()
