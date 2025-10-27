def run_vending_machine(inputs):
    #this function is purely for testing
    amount_due = 50
    for user_input in inputs:
        try:
            coin = int(user_input)
        except ValueError:
            # Ignore invalid inputs
            continue
        if coin not in (5,10,25):
            # Ignore invalid coin denominations
            continue
        amount_due -= coin
        if amount_due <= 0:
            break
    return abs(amount_due)

def main():
    #this function is for user interaction (OG function)
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        user_input = input("Insert Coin: ")
        try:
            coin = int(user_input)
        except ValueError:
            print("Invalid coin.")
            continue
        if coin not in (5, 10, 25):
            print("Invalid coin value.")
            continue
        amount_due -= coin

    print(f"Change Owed: {abs(amount_due)}")

if __name__ == "__main__":
    main()

#testing push for github actions CI/CD


