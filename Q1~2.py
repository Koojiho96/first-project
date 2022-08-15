# 추가 해보기
# 1번 문제 "도형 넓이 구하기"
print(a)

def circle(r):
  pi = 3.14
  return r*r*pi

def tri(b,h):
  return b * h / 2
  
def rec(w,h):
  return w*h

def srec(l):
  return l * l

print('''
==========도형 목록==========
1. 원
2. 삼각형
3. 직사각형
4. 정사각형
=============================
''')

select = int(input('도형 목록 중 번호를 선택하세요'))

if select == 1:
  r = int(input('반지름 입력'))
  value = circle(r)
  print(f'길이가 {r}인 원 넓이는 약 {value}입니다.')

if select == 2:
  b, h = map(int,input('밑면,높이입력').split())
  value = tri(b,h)
  print(f'밑변{b},높이{h}인 삼각형 넓이는 약 {value}입니다.')

if select == 3:
  w, h = map(int,input('좌,우 입력').split())
  value = rec(w,h)
  print(f'좌우가 각각 {w,h}인 사각형은 약 {value}입니다.')

if select == 4:
  l = int(input('정사각형 길이 입력'))
  value = srec(l)
  print(f'길이가 {l}인 정사각형 넓이는 {value}입니다.')



#===========================#



  # 2번 문제 "반올림 계산기"

num = float(input('숫자입력'))

if  int(num - 0.5) == int(num):
  print(int(num)+1)
else:
  print(int(num))