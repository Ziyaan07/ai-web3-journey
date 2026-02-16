# Day 3 — Understanding Data Basics

# Example dataset (ages)
ages = [20, 22, 25, 30, 18]

# Calculate average
average_age = sum(ages) / len(ages)

print("Average age:", average_age)


# Classification example (pass/fail)

scores = [45, 80, 60, 30, 90]

for score in scores:
    if score >= 50:
        print("Pass")
    else:
        print("Fail")
