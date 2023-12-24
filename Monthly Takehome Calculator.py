'''
QUESTION
A newspaper vendor received 20,000 naira monthly and 10% commission of total monthly sales exceeding 100,000. Write an algorithm to compute the total monthly takehome
'''
salary = 20000
TMS = int(input("Total monthly sales= "))
#to compute commission
comm = 0
if TMS <= 100000:
    comm = 0
else:
    comm = 0.1 * (TMS - 100000)
TMT = salary + comm
print(f"Total Monthly Takehome:  {TMT}")