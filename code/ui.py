from tkinter import *
#from calc import Schedule

r = Tk()
r.title('Loan Amoortization Calculator')

def create_ammortization_schedule(P, r, n):
    #sched = Schedule(P, r, n)
    #print(sched.schedule.to_string())
    #display schedule
    pass




r = Tk()
r.title('Loan Amoortization Calculator')


Label(r, text = 'Lenght of Loan').grid(row=1)
Label(r, text = 'Interest Rate').grid(row=2)

#total loan amount
#length of loan in months
#loans interest rate
loan_amount = Entry(r)
loan_lentgh = Entry(r)
interest_rate = Entry(r)

loan_amount.grid(row=0, column=1)
loan_lentgh.grid(row=1, column=1)
interest_rate.grid(row=2, column=1)


print(loan_amount)
r.mainloop()