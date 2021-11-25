## 마르코프 체인 프로그램 작성


A = []
B = []
C = []

# 초기 값

A.append(1/3)   
B.append(1/3)
C.append(1/3)

count = int(input("진행 회차를 입력하세요 : "))
print("")

# 점화식 코드
for k in range(count + 1) :           
    A.append(0.1*A[k] + 0.6*B[k] + 0.4*C[k])  ## 점화식을 배열에 저장
    B.append(0.5*A[k] + 0.1*B[k] + 0.5*C[k])
    C.append(0.4*A[k] + 0.3*B[k] + 0.1*C[k])
       
    print("K = %d      |    " % k, end = "")
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
    
    
                       
# 수렴값 정의 / 설정한 수렴값 범위에 있는 값을 저장
j = 0
collect_A = 0   
collect_B = 0
collect_C = 0

for i in range(count) :
    j = j + 1
    if ((A[j] - A[i]) <= 0.00015) :
        collect_A = collect_A + 1
        print(A[j] - A[i])
    if ((B[j] - B[i]) <= 0.00015) :
        collect_B = collect_B + 1
    if ((C[j] - C[i]) <= 0.00015) :
        collect_C = collect_C + 1

      
print("수렴값 중첩 A : %d개" % collect_A)
print("수렴값 중첩 B : %d개" % collect_B)
print("수렴값 중첩 C : %d개" % collect_C) 
            

 

 
