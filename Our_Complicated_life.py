#Constants: Loans
CAR_LOAN_PRINCIPAL=3246.55          #logged on 03/12/2016
CAR_LOAN_INTEREST=2.9               #2.9% interest rate
FED_LOAN1_PRINCIPAL=14954.13        #logged on 03/12/2016
FED_LOAN2_PRINCIPAL=5931.40         #logged on 03/12/2016
FED_LOAN_INTEREST_RATE=5.625        #5.625% interest rate
ECSI_LOAN_PRINCIPAL=72980.24        #logged on 03/12/2016, payment 1th of month
ECSI_LOAN_INTEREST_RATE=5.61        #5.61% interest rate
HOUSE_LOAN_PRINCIPAL=183905         #logged on 03/12/2016, payment 1th of month
HOUSE_LOAN_INTEREST_RATE=3.875      #3.875% interest rate
#variables
#Capitol_One_Credit_Card= int(input("How much is due on the Capitol One CC?: "))
                                    #payment 25th of month
#Amex_Credit_Card= int(input("How much is due on the AMEX CC?: "))
                                    #payment 16th of month
#Car_Loan_Monthly_Payment=int(input("What are you paying on Peppy?: "))
                                    #payment 15th of month
#Fed_Loan1_Monthly_Payment=int(input("What are you paying on Fed Loan 1?: "))
                                    #payment 21st of month
#Fed_Loan2_Monthly_Payment=int(input("What are you paying on Fed Loan 2?: "))
                                    #payment 21st of month
#ECSI_Monthly_Payment=int(input("What are you paying on ECSI Loan?: "))
                                    #payment 1st of month
#House_Monthly_Payment=int(input("What are you paying on House?: "))
                                    #payment 21st of month
#Functions
#How long is loan going to last
#def lenght_of_loan(PRINCIPAL,ANNUAL_INTEREST_RATE,DURATION):
def remaining_balance(PRINCIPAL,ANNUAL_INTEREST_RATE,DURATION,NUMBER_OF_PAYMENTS):
    n=DURATION*12
    if ANNUAL_INTEREST_RATE==0:
        bALANCE=PRINCIPAL*(1-(NUMBER_OF_PAYMENTS/n))
    else:
        r=(ANNUAL_INTEREST_RATE/100)/12
        bALANCE=PRINCIPAL*(((1+r)**n)-((1+r)**NUMBER_OF_PAYMENTS))/(((1+r)**n)-1)
    return bALANCE
def monthly_loan_payment(PRINCIPAL,ANNUAL_INTEREST_RATE,DURATION):
    n=DURATION*12
    if ANNUAL_INTEREST_RATE!=0:
        r=(ANNUAL_INTEREST_RATE/100)/12
    else:
        r=PRINCIPAL/n
    mONTHLY_pAYMENT=PRINCIPAL*(r*((1+r)**n)/(((1+r)**n)-1))
    return mONTHLY_pAYMENT
PRINCIPAL=CAR_LOAN_PRINCIPAL
ANNUAL_INTEREST_RATE=CAR_LOAN_INTEREST
DURATION=int(input('Enter loan duration in years: '))
mONTHLY_pAYMENT=monthly_loan_payment(PRINCIPAL,ANNUAL_INTEREST_RATE,DURATION)
print('LOAN AMOUNT: ',PRINCIPAL,' INTEREST RATE (PERCENT): ',ANNUAL_INTEREST_RATE)
print('DURATIION (YEARS): ',DURATION,' MONTHLY PAYMENT: ',int(mONTHLY_pAYMENT))
for YEARS in range(1,DURATION+1):
    NUMBER_OF_PAYMENTS=YEARS*12
    TOTAL_PAYMENT=(mONTHLY_pAYMENT*YEARS)*12
    y=remaining_balance(PRINCIPAL,ANNUAL_INTEREST_RATE,DURATION,NUMBER_OF_PAYMENTS)
    print('YEARS: ',YEARS,' BALANCE: ',int(y),' TOTAL PAYMENTS: ',int(TOTAL_PAYMENT))
