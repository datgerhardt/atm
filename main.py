from atm.atm import ATM


def get_amount():
    while True:
        amount = int(input("Enter amount to withdraw: "))
        if amount >= 0:
            atm = ATM(amt=amount)
            depended = atm.depense()
            atm.present(depended)
            break
        else:
            print(f'The amount GHS {amount} is less than zero')
            continue


def get_amount_by_denominations():
    denominations = {'1': 0, '2': 0, '5': 0, '10': 0, '20': 0, '50': 0, }
    for i in denominations.keys():
        x = int(input(f'Number of note for GHS {i}: '))
        if x >= 0:
            denominations[i] = x
        else:
            print(
                f'The amount GHS `{x} is less than zero'
            )
            continue
    atm = ATM()
    depended = atm.get_amt_by_denominations(denominations)
    atm.present(depended)


def main():
    print(" \t\t Welcome to ATM ")
    print("*******************************************************")
    print("Enter \n 1. To enter amount\n 2. To enter amount by denominations")
    while True:
        choice = int(input("Choice one: "))
        if choice == 1:
            get_amount()
            break
        elif choice == 2:
            get_amount_by_denominations()
            break
        else:
            continue


if __name__ == "__main__":
    main()
