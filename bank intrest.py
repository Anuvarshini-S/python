def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time (years): "))

si = simple_interest(p, r, t)
total = p + si

print("\n----- Bank Interest Details -----")
print("Simple Interest :", si)
print("Total Amount    :", total)