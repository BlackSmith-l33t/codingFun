## 마르코프 체인


from fractions import Fraction # 분수 표현 함수


#A = Fraction(1,3)
#B = Fraction(1,3)
#C = Fraction(1,3)

# A, B, C의 초기값
Ak = 1/3
Bk= 1/3
Ck = 1/3

# 점화식

Ak1 = 0.1*Ak + 0.6*Bk + 0.4*Ck
Bk1 = 0.5*Ak + 0.1*Bk + 0.5*Ck
Ck1 = 0.4*Ak + 0.3*Bk + 0.1*Ck



print("%4.3f, %4.3f, %4.3f" % (Ak1, Bk1, Ck1))


      

