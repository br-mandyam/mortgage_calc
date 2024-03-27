from tkinter import Tk, Label, Button, Entry, Frame, Scrollbar, DoubleVar, IntVar, ttk, END, W
from schedule import Schedule

class Ammortization_Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Ammortization Calculator")
        self.entry_frame = Frame(master)
        self.calculated = False
        self.loan_amount = DoubleVar()
        self.loan_length = IntVar()
        self.interest_rate = DoubleVar()
        self.loan_amount_label = Label(self.entry_frame, text='Loan Amount')
        self.loan_lentgh_label = Label(self.entry_frame, text='Lenght of Loan')
        self.interest_rate_label = Label(self.entry_frame, text='Interest Rate')
        self.calculate_button = Button(self.entry_frame, text="calculate", command=self.calculate_schedule)
        self.loan_amount = Entry(self.entry_frame,textvariable=self.loan_amount)
        self.loan_length = Entry(self.entry_frame, textvariable=self.loan_length)
        self.interest_rate = Entry(self.entry_frame,textvariable=self.interest_rate)
        self.sched_tree = ttk.Treeview(master)
        self.bottom_scroll_bar = Scrollbar(master,orient='horizontal',command=self.sched_tree.xview)

        #layout
        self.loan_amount_label.grid(row=0, column=0)
        self.loan_lentgh_label.grid(row=1, column=0)
        self.interest_rate_label.grid(row=2, column=0)
        self.calculate_button.grid(row=3,column=1)
        self.loan_amount.grid(row=0, column=1)
        self.loan_length.grid(row=1, column=1)
        self.interest_rate.grid(row=2, column=1)

        self.entry_frame.pack()
        self.sched_tree.pack(fill='both', expand=True)
        self.sched_tree.configure(xscrollcommand=self.bottom_scroll_bar.set)
        self.bottom_scroll_bar.pack(side='bottom', fill='x')


    def display_schedule(self, schedule:Schedule):
        if self.calculated == True:
            self.sched_tree.delete(*self.sched_tree.get_children())
        else:
            self.calculated = True
        cols = schedule.schedule.columns
        self.sched_tree["columns"] = list(cols)
        for i in cols:
            self.sched_tree.column(i, anchor="w")
            self.sched_tree.heading(i, text=i, anchor='w')
        for row in schedule.schedule.itertuples():
            cleaned_row = []
            for val in row:
                cleaned_row.append(round(val, 2))
            self.sched_tree.insert("",END,values=cleaned_row)



    def calculate_schedule(self):
        P = round(float(self.loan_amount.get()), 2)
        r = round(float(self.interest_rate.get()), 2)
        n = int(self.loan_length.get())
        schedule = Schedule(P, r, n)
        self.display_schedule(schedule)

if __name__ == '__main__':
    root = Tk()
    my_gui = Ammortization_Calculator(root)
    root.mainloop()