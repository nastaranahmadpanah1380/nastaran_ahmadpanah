import random

n = int(input("لطفا طول آرایه را وارد کنید"))
m = int(input("بازه اعداد تا چه عددی باشد"))
numbers = random.sample(range(0, m), n)

print(numbers)