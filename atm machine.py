print('Welcome to SBI Bank')
restart = ('Y')
chances = 3
Balance = 1000
while chances >= 0:
    pin=int(input("Please enter your 4 digit pin"))
    if pin == (1234):
        print('you entered your pin Correctly\n')
        while restart not in ('n','No','no','N'):
            print('Please press 1 for your Balance\n')
            print('Please press 2 for your Withdrawal\n')
            print('Please press 3 for your Pay in\n')
            print('Please press 4 for your Return card\n')
            option = int(input('What would you like to choose?'))
            if option == 1:
                print('Your balance is Rupees', Balance,'\n')
                restart = input('Would you like to go back?')
                if restart in ('n','No','no','N'):
                    print('Thanku you for banking with SBI')
                    break
            elif option ==2:
                option = ('Y')
                Withdrawal = float(input('How much would you like to Withdrawal? \nRupees100/Rupees200/Rupees400/Rupees600/Rupees800/Rupees1000 for other 1'))
                if Withdrawal in[100,200,400,600,800,1000]:
                    Balance = Balance-Withdrawal
                    print('\nyour balance is now Rupees',Balance)
                    restart = input('what would you like to do?')
                    if restart in ('n','No','no','N'):
                        print('Thanks you for banking with SBI')
                        break
                elif Withdrawal != [100,200,400,600,800,1000]:
                    print('Invalid amount,please re-try\n')
                    restart=('y')
                elif Withdrawal==1:
                    Withdrawal=float(input('Please enter the desired amount:'))
            elif option==3:
                Pay_in = float(input('How much would you like to pay in?'))
                Balance= Balance+Pay_in
                print('\nyour balance is now Rupees',Balance)
                if restart in ('n', 'No', 'no', 'N'):
                    print('Thanku you for banking with SBI')
                    break
            elif option==4:
                print('Please wait while your card is returned....\n')
                print('Thanks you for banking with SBI')
                break
            else:
                print('Please enter a correct number. \n')
                restart=('y')
    elif pin != ('1234'):
        print('Incorrect password')
        chances = chances-1
        if chances==0:
            print('\n No more, tries,contact support')
            break














