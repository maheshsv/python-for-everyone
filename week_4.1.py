hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if h > 40 :
    gross_pay = (40 * r) + ((h - 40) * r * 1.5)
else:
    gross_pay = h * r

print(gross_pay)
