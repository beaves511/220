"""
Name: Eric Beaver
sales_person.py

Problem: create a sales_person class

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """
    class representing a salesperson with an employee id and name
    """

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        """
        gets employee id
        :return self.employee_id:
        """
        return self.employee_id

    def get_name(self):
        """
        gets name of employee
        :return self.name:
        """
        return self.name

    def set_name(self, name):
        """
        void, sets self.name to specified parameter
        :param name:
        """
        self.name = name

    def enter_sale(self, sale):
        """
        void, adds individual sale to self.sales for employee
        :param sale:
        """
        self.sales.append(sale)

    def total_sales(self):
        """
        Calculates total sales for an employee
        :return sum_sales:
        """
        sum_sales = 0
        for i in self.sales:
            sum_sales += i
        return sum_sales

    def get_sales(self):
        """
        returns list of sales
        :return self.sales:
        """
        return self.sales

    def met_quota(self, quota):
        """
        Checks to see if employee met specified quota
        :param quota:
        :return boolean:
        """
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        """
        compares employee sales to other employee sales
        :param other:
        :return number indication:
        """
        if other.total_sales() > self.total_sales():
            return -1
        if self.total_sales() > other.total_sales():
            return 1
        return 0

    def __str__(self):
        """
        return string entry
        :return string:
        """
        return str(self.get_id()) + "-" + self.get_name() + ": " + str(self.total_sales())
