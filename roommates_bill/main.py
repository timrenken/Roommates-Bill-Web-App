#! python3

from room import Bill, Roommate
from reports import PdfReport


service = input("What bill is this for? ")
amount = float(input("How much is the bill for? "))
period = input("For what period is this bill for? ")

name1 = input("What is your name? ")
days_in_house1 = int(input("How many days were you home? "))

name2 = input("What is the name of your other roommate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house? "))

the_bill = Bill(service,amount,period)
roommate1 = Roommate(name1,days_in_house1)
roommate2 = Roommate(name2,days_in_house2)

print(f"{roommate1.name} pays: ${roommate1.pays(the_bill, roommate2)}")
print(f"{roommate2.name} pays: ${roommate2.pays(the_bill, roommate1)}")

pdf_report = PdfReport(filename=f"{the_bill.period}-bill.pdf")
pdf_report.generate(roommate1, roommate2, the_bill)