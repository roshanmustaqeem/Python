bal = 0
while bal <= 5000:
    print("whats your savings this month: ")
    bal2 = int(input())
    bal = bal + bal2
    print(f"you have reached your goal {bal}")