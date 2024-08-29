# Demo_software
snyk
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# รับค่าคะแนนจากผู้ใช้
score = float(input("กรุณาใส่คะแนนของคุณ: "))

# คำนวณเกรด
grade = calculate_grade(score)

# แสดงผลเกรด
print(f"เกรดของคุณคือ: {grade}")

