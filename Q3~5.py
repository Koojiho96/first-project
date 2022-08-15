# 3번 문제 " 회문"

word = input("단어를 입력해주세요 : ")

if word == word[::-1]:
    print(word + "는 회문입니다")
#   print("{0}은 회문입니다".format(word))
else:
    print(word + "는 회문이 아닙니다")



#===========================#



# 4번 문제 " 자리수의 합"


num1 = input().split()
sum1= []
for i in num1:
    sum = 0
    for j in range(len(i)):
        sum += int(i[j])
    sum1.append(sum)

#answer = sum1.index(max(sum1))
#print(num1[answer])
print(num1[sum1.index(max(sum1))])



#===========================#



# 5번 문제 " 뒤집은 정수"

a,b = input().split()

a_r = a[::-1]
b_r = b[::-1]
c_r = str(int(a_r) + int(b_r))
c = c_r[::-1]
print(c)