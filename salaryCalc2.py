# Tax calculator for Canadian and Quebec income tax 2016. 
# 
# v. 1.1
#

salary = float(input('How much is your annual salary? > '))

personalAmtQ = 11305.00 * .16
personalAmtC = 11474.00 * .15
global netPay
netpay = 0
# Quebec taxes

def QuebecTaxes(salary):
    global taxesQ
    taxesQ = 0
    global taxBracketQ
    taxBracketQ = 0

    if 0 <= salary <= 42390:
        taxesQ = (salary * 0.16) - personalAmtQ
        taxBracketQ = '16%'
    elif salary <= 84780:
        taxesQ = (6782.40 + ((salary - 42390)* .20)) - personalAmtQ
        taxBracketQ = '20%'
    elif salary <= 103150:
        taxesQ = (15260.40 + ((salary - 84780) * .24)) - personalAmtQ
        taxBracketQ = '24%'
    else:
        salary > 103150
        taxesQ = (19669.20 + ((salary - 103150) * .2575)) - personalAmtQ
        taxBracketQ = '25.75%'

# Print out results

    if taxesQ < 0:
        print('You are owed by Quebec $ {}'.format(abs(taxesQ)))
        print('You are in the {} tax bracket in Quebec'.format(taxBracketQ))
    else:
        print('You owe Quebec $ {}'.format(taxesQ))
        print('You are in the {} tax bracket in Quebec'.format(taxBracketQ))


# Canada taxes

def CanadaTaxes(salary):
    global taxesC
    taxesC = 0
    global taxBracketC
    taxBracketC = 0
   
    if 0 <= salary <= 45282:
        taxesC = (salary * 0.15) - personalAmtC
        taxBracketC = '15%'
    elif salary <= 90563:
        taxesC = (6792.30 + ((salary - 45282) * .22)) - personalAmtC
        taxBracketC = '22%'
    elif salary <= 140388:
        taxesC = (16754.12 + ((salary - 90563) * .26)) - personalAmtC
        taxBracketC = '26%'
    elif salary <= 200000:
        taxesC = (29708.62 + ((salary - 140388)* .29)) - personalAmtC
        taxBracketC = '29%'
    else:
        salary > 200000
        taxesC = (46996.10 + ((salary - 200000) * .33)) - personalAmtC
        taxBracketC = '33%'
    
# Print out results
    global taxesTotal
    taxesTotal = 0
    if taxesC < 0:
        print('You are owed by Canada $ {}'.format(abs(taxesC)))
        print('You are in the {} tax bracket in Canada'.format(taxBracketC))
    else:
        print('You owe Canada $ {}'.format(taxesC))
        print('You are in the {} tax bracket in Canada'.format(taxBracketC))

# Total taxes
def TotalTaxes():
    
    taxesTotal = round(taxesQ + taxesC, 2)
    netPay = salary - taxesTotal
    if taxesTotal < 0:
        print('The Total you are owed is $ {}'.format(abs(taxesTotal)))
        netPay = salary
    else:
        print('The Total tax you owe is $ {}'.format(taxesTotal))
    print('Net pay is $ {}'.format(netPay))


QuebecTaxes(salary)
CanadaTaxes(salary)
TotalTaxes()
