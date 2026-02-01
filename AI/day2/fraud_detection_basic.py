transactions = [120, 150, 130, 2000, 170, 160]

threshold = 500

for amount in transactions:
    if amount > threshold:
        print("Suspicious transaction detected:", amount)
