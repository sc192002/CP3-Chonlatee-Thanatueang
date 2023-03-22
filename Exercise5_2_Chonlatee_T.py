v = int(input("ความเร็วที่รถเคลื่อนที่ (km)  : "))
v >= 1
t = int(input("เวลาที่รถเคลื่อนที่ (h)     : "))
t >= 1
if v >=1 and t >= 1:
    print(int(v / t), "km/h")
else:
    print("Error !")



