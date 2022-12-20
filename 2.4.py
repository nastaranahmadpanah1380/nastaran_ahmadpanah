number = []

while True:
    
    a = input("write Exit or number: ")
    
    if a == "Exit":
        sum_total = sum(number)
        print("sum = ", sum_total)
        break
    number.append(float(a))