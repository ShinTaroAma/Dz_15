
class Employee:
    
    def __init__(self, name, second_name, mobile_number, email, payment_per_one_day):
        self.name = name
        self.second_name = second_name
        self.mobile_number = mobile_number
        self.email = email
        self.payment_per_one_day = payment_per_one_day


    @staticmethod
    def work(self):
        print("I come to the office")

    def payment_diff(Recruiter_payment, Programmer_payment):
        return max(Recruiter_payment, Programmer_payment)

    


    def check_salary(self, work_days, payment_per_one_day, no_payment_days):
        self.day = work_days
        self.payment_per_one_day = payment_per_one_day
        self.no_payment_days = no_payment_days

        return (work_days - no_payment_days) * payment_per_one_day



class Recruiter(Employee):
    hired_this_month = 0

    
    def work(self):
        return "I come to the office and start hiring"

    def __str__(self):
        return f"Должность:{self.name} {self.second_name}"
    
    

class Programmer(Employee):
    tech_stack = ""
    closed_this_month = 0

    
    def work(self):
        return "I come to the office and start coding"

    def __str__(self):
        return f"Должность:{self.name} {self.second_name}"


prog = Programmer("Roma", "Momot", 33456, "sup@gmail.com", 50.00)

