amount = int(input("Initial amount: "))
benefits = int(input("Percentage of benefits (anually): "))
yrs = int(input("Introduce how many years to look the investment: "))
importantQuestion = input("You wanna insert the same amount anually in the same index? (y/n): ")


def calcFinalAmount(money, percentage, years):
    final = money
    if importantQuestion == 'n':
        #With false important question
        for i in range(years):
            final += final*(percentage/100)
    else:
        #with true important question
        for i in range(years):
            final += final*(percentage/100)
            final += money
    
    return final

print(calcFinalAmount(amount, benefits, yrs))