hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter Rate:"))
if h > 40  :
    ratel = (rate * 1.5) * (h-40)
    pay = ((h-5)*rate) + ratel
    print (pay)
