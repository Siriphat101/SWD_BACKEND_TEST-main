
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
NUMBERS_THAI = {
    0: 'ศูนย์',
    1: 'หนึ่ง',
    2: 'สอง',
    3: 'สาม',
    4: 'สี่',
    5: 'ห้า',
    6: 'หก',
    7: 'เจ็ด',
    8: 'แปด',
    9: 'เก้า',
    10: 'สิบ',
    100: 'ร้อย',
    1000: 'พัน',
    10000: 'หมื่น',
    100000: 'แสน',
    1000000: 'ล้าน'
}

text = ""
number = int(input("Enter number: "))


if 0<= number < 10000000:
    
    while number > 0:
        
        if number >= 1000000:
            text += NUMBERS_THAI[number//1000000] + NUMBERS_THAI[1000000] 
            number = number - (number//1000000)*1000000
            
        elif number >= 100000 and number < 1000000:
            text += NUMBERS_THAI[number//100000] + NUMBERS_THAI[100000]
            number = number - (number//100000)*100000
            
        elif number >= 10000 and number < 100000:
            text += NUMBERS_THAI[number//10000] + NUMBERS_THAI[10000]
            number = number - (number//10000)*10000
        elif number >= 1000 and number < 10000:
            text += NUMBERS_THAI[number//1000] + NUMBERS_THAI[1000]
            number = number - (number//1000)*1000
        elif number >= 100 and number < 1000:
            text += NUMBERS_THAI[number//100] + NUMBERS_THAI[100]
            number = number - (number//100)*100
        elif number >= 10 and number < 100:
            text += NUMBERS_THAI[number//10] + NUMBERS_THAI[10]
            number = number - (number//10)*10
        elif number >= 1 and number < 10:
            text += NUMBERS_THAI[number]
            number = number - number
    
    
    text = text.replace("หนึ่งสิบ","สิบ")
    text = text.replace("สิบหนึ่ง","สิบเอ็ด")
    text = text.replace("สองสิบ","ยี่สิบ")

    print(text)
    
else:
    print("Invalid !!! number range 0-9,999,999")
