def computepay(total_hrs,total_rate):
    h = float(total_hrs)
    r = float(total_rate)
    if h > 40 :
        gross_pay = (40 * r) + ((h - 40) * r * 1.5)
    else:
        gross_pay = h * r
    return gross_pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs,rate)
print("Pay",p)
