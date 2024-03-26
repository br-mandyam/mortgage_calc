import pandas as pd

class Schedule:    
    def create_schedule(self, P, r, n):
        r = r/12
        monthly_payment = round(P*((r*pow(1+r, n))/(pow(1+r,n)-1)),2)
        interest_rate = r
        balance = P
        total_interest = 0
        total_paid = 0
        for number in range(1, n+1):
            interest = round(balance * interest_rate, 2)
            total_interest += interest
            if number < n:
                principal = monthly_payment - interest
                balance -= principal
                total_paid += monthly_payment
            else:
                principal, monthly_payment, balance = balance, balance + interest, 0
            yield number, monthly_payment, interest, principal, balance, total_interest, total_paid # I do not want to yield I want to add to a Pandas Dataframe\
        
    def __init__(self, P, r, n): #
        schedule_list = list(self.create_schedule(P,r,n))
        self.schedule = pd.DataFrame(schedule_list, columns=['Month', 'Payment', 'Interest Payment', 'Principal Payment','Balance', 'Total Interest', 'Total Paid'])

    def print(self):
        print(self.schedule.to_string())

sched:Schedule = Schedule(100000, .05, 60)
sched.print()