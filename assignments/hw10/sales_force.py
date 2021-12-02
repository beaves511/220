"""
Name: Eric Beaver
sales_force.py

Problem: create a sales_force class

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from sales_person import SalesPerson


class SalesForce:
    """
    class representing a SalesForce with a list of SalesPerson
    """

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        """
        adds data of employee to list called self.sales_people
        :param file_name:
        """
        with open(file_name, 'r') as in_file:
            for line in in_file:
                parts = line.split(', ')
                obj = SalesPerson(int(parts[0]), parts[1])
                p_parts = parts[2].split()
                for num in p_parts:
                    obj.enter_sale(float(num))
                self.sales_people.append(obj)

    def quota_report(self, quota):
        """
        returns list where each element is a list of name, id, sales, and boolean quota
        :param quota:
        :return re_list:
        """
        re_list = []
        for people in self.sales_people:
            temp_list = [people.get_id(), people.get_name(),
                         people.total_sales(), people.met_quota(quota)]
            re_list.append(temp_list)
        return re_list

    def top_seller(self):
        """
        return list of top seller(s)
        :return max_l:
        """
        max_l = [self.sales_people[0]]
        max_val = self.sales_people[0].total_sales()
        for people in range(1, len(self.sales_people)):
            if self.sales_people[people].total_sales() == max_val:
                max_l.append(self.sales_people[people])
            if self.sales_people[people].total_sales() > max_val:
                max_val = self.sales_people[people].total_sales()
                for i in max_l:
                    max_l.remove(i)
                max_l.append(self.sales_people[people])
        return max_l

    def individual_sales(self, employee_id):
        """
        returns person with given employee id
        :param employee_id:
        :return employee:
        """
        for people in range(len(self.sales_people)):
            if self.sales_people[people].get_id() == employee_id:
                return self.sales_people[people]
        return None
