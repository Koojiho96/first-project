# 1주차 온라인 리뷰, 15분 전 알람 setting 시간 확인

h, m = map(int, input('숫자 두 개를 입력하세요: ').split())

if  h < 0 or 23 < h or m < 0 or 59 < m:
  print("시간을 다시 입력")

elif m - 45 < 0:
  h -= 1
  m = (m+15)
  
  if h < 0:
    h = 23
    
elif m - 45 > 0:
  m = (m-45)

print(h,m)

