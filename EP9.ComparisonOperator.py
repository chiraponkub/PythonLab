#ตัวดำเนินการเปรียบเทียบ

# นำข้อมูลอย่างน้อย 2 คำตอบ => จริง / เท็จ
# ชนิดข้อมูลเหมือนกัน
# คำตอบ 2 คำตอบ => จริง / เท็จ

x,y,z = 2,5,4

print("ค่า x = ", x )
print("ค่า y = ", y)
print("ค่า x มากกว่า y หรือไม่ ? : ", x>y)
print("ค่า x น้อยกว่า y หรือไม่ ? : ", x<y)
print("ค่า x เท่ากับ y หรือไม่ ? : ", x==y)
print("ค่า x ไม่เท่ากับ y หรือไม่ ? : ", x!=y)


# หรือ 
print("ค่า x มากกว่า หรือ เท่ากับ ค่า y หรือไม่ ?", x>=y)
print("ค่า x น้อยกว่า หรือ เท่ากับ ค่า y หรือไม่ ?", x<=y)

# และ
print("ค่า x มากกว่า y และ y มากกว่า z หรือไม่ ? : ", x>y>z)
print("ค่า x น้อยกว่า y และ y น้อยกว่า z หรือไม่ ? : ", x<y<z)
print("ค่า x เท่ากับ y และ y เท่ากับ z หรือไม่ ? : ", x==y==z)