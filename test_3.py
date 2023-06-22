"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python โดยห้ามใช้ math.factorial เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว

"""
fac = 1
zero = 0
number = int(input("Enter number: "))

for i in range(number):
    fac = fac * (number-i)

str_fac = str(fac)
for i in range(len(str_fac)):
    if str_fac[(len(str_fac)-1) - i] == "0":
        zero += 1
    else:
        break
        
print(f"{number}! = {fac} มีเลข 0 ต่อท้าย {zero} ตัว")


# end

