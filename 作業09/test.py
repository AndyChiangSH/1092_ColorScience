from decimal import Decimal

x = 0.1247185487026306

print(str(x))

d = Decimal(str(x))

print(round(d, 6))  # 0.124719
print(type(d))      # <class 'decimal.Decimal'>

d = float(round(d, 6))

print(d)
print(type(d))
