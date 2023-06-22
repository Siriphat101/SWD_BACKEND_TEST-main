
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
number = int(input("Enter number: "))
roman = ""
if 0 < number <= 1000:
    
    while number > 0:

        if number == 1000:
            roman = "M"
            number = number - 1000
        elif number >= 500 and number < 1000:
            roman +="D"
            number = number - 500
        elif number >= 100 and number < 500:
            roman += "C"
            number = number - 100
        elif number >= 50 and number < 100:
            roman += "L"
            number = number - 50
        elif number >= 10 and number < 50:
            roman += "X"
            number = number - 10
        elif number >= 5 and number < 10:
            roman += "V"
            number = number - 5
        elif number >= 1 and number < 5:
            roman += "I"
            number = number - 1

else:
    print("Invalid !!! number range 0-1,000")
    

print("Roman number: ",roman)