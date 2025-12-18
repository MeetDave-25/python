def da(amt):
    return amt*0.05
def hra(amt):
    return amt*0.10
def pf(amt):
    return amt*0.12
def itax(amt):
    return amt*0.08

salary = int(input("enter your salary : "))
da = da(salary)
hra = hra(salary)
pf = pf(salary)
itax = itax(salary)

print("Salary :", salary)
print("DA :", da)
print("HRA :", hra)
print("PF :", pf)
print("ITAX :", itax)