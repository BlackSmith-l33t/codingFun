## 마르코프 체인 프로그램 3

# 3개의 값을 저장하는 리스트 생성

A = []
B = []
C = []

# 초기 값

A.append(0.4)   
B.append(0.3)
C.append(0.3)

##count = int(input("반복 계산 횟수 : "))
##
##print("")
#
# 점화식 코드

collect_A = 0   
collect_B = 0
collect_C = 0
j = 0
k = 0 

while (1) :
        
    A.append(0.2*A[k] + 0.5*B[k] + 0.3*C[k])  ## 점화식을 배열에 저장
    B.append(0.3*A[k] + 0.1*B[k] + 0.4*C[k])
    C.append(0.5*A[k] + 0.4*B[k] + 0.3*C[k])
    
    print("K = %d     |    " % k, end = "")
    print("")
    print("___________")
    print("" "           |")
    print("" "           |")
    print("Ak : %4.3f |" % A[k])
    print("" "           |")
    print("Bk : %4.3f |" % B[k])
    print("" "           |")
    print("Ck : %4.3f |" % C[k])
    print("" "           |")
    print("____________")
    print("")

    j = j + 1
    
    if ((A[j] - A[k]) <= 0.00015) :
        collect_A = collect_A + 1
    if ((B[j] - B[k]) <= 0.00015) :
        collect_B = collect_B + 1
    if ((C[j] - C[k]) <= 0.00015) :
        collect_C = collect_C + 1
    k = k + 1
   
    if collect_A >= 10 :
        if collect_B >= 10 :
            if collect_C >= 10 :
                 break 
                       
print("수렴값 누적 A : %d개" % collect_A)
print("수렴값 누적 B : %d개" % collect_B)
print("수렴값 누적 C : %d개" % collect_C) 
            

 

 
