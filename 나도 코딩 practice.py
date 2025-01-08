### 1 함수

# def profile(name, age, main_lang):
#   print(name, age, main_lang)


# profile(name="유재석",age=50,main_lang="파이선")

# 2가변인자를 이용한 함수 호출
def profile(name, age, lang1, lang2,lang3):
  print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end= " " 프린트문이 끝날떄 줄바꿈 하지 않고 띄워쓰기하고 끝남
  print(lang1, lang2, lang3)
  
profile("유재석",20,"P","J","C") # 언어 늘어나면 어떡하나?
profile("김태호",20,"K","S","")  # 빈값 일일이 입력해야하나?

# 가변인자 사용
def profile(name, age, *language):
  print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
  for lang in language:
    print(lang)
  print()
  
  
profile("유재석",20,"P","J","C","JAVA","C++") # 언어 늘어나면 어떡하나?
profile("김태호",20,"Kotlin","Swift")  # 빈값 일일이 입력해야하나?  


# 지역변수 함수가 시작될떄만 생기고 사라지는것
# 전역변수는 모든곳에서 부를수 있는것
# gun=10

# def checkpoint(soldiers): #경계근무
#   gun = gun-soldiers        #여기에 나온 건은 지역변수라서 정의가 안된것이다. 함수 구문 안에 gun=10 을 넣어줘야한다
#   print("[함수 내] 남은 총 : {0}".format(gun))
  
  
# print("전체 총 : {0}".format(gun))
# checkpoint(2) #2명이 경계근무 나감
# print("남은 총 : {0}".format(gun))


gun=10

def checkpoint(soldiers): #경계근무
  global gun #전역 공간에 있는 gun을 사용
  gun = gun-soldiers        #여기에 나온 건은 지역변수라서 정의가 안된것이다. 함수 구문 안에 gun=10 을 넣어줘야한다
  print("[함수 내] 남은 총 : {0}".format(gun))
  
  
print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경계근무 나감
print("남은 총 : {0}".format(gun))

# 이렇게 하면 구문이 복잡해짐. -> 리턴을 받아서 깔금하게 만들어야함
# 외부에서 gun=10 함수를 가져와서 gun = checkpoint_ret(gun,2)에 넣고 함수에서 gun을 계산함
def checkpoint_ret(gun,soldiers):
  gun=gun-soldiers
  print("[함수 내] 남은 총 : {0}".format(gun))
  return gun

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경계근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))


# #퀴즈 표준체중 프로그램
# 남자 : 키(m) *키(m)*22
# 여자 : 키(m)*키(m)*21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
# 함수명 : std_weight
# 전달값 : 키, 성별 height, gender
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다

# def std_weight(height, gender):
#   if gender = "여자":
#     std = height*height*21
#   if gender = "남자":
#     std = height*height*22
#   return std  

# std_weight("키와 성별은 무엇입니까?"input(height,gender))
# print("키 {0}cm {1}의 표준 체중은" std "kg 입니다")
  
   
#1. 코딩 답변   
# def std_weight(height, gender):  # 키 m 단위(실수), 성별 "남자" / "여자"
#     """
#     표준 체중을 계산하는 함수
#     :param height: 키(cm)
#     :param gender: 성별 ("남자" 또는 "여자")
#     :return: 표준 체중(kg)
#     """
#     height_m = height / 100  # cm를 m로 변환
#     if gender == "남자":
#         return round(height_m * height_m * 22, 2)
#     elif gender == "여자":
#         return round(height_m * height_m * 21, 2)
#     else:
#         return None

# # 사용자 입력 받기
# height = int(input("키를 입력하세요 (cm): "))
# gender = input("성별을 입력하세요 (남자/여자): ")

# # 표준 체중 계산
# weight = std_weight(height, gender)

# # 결과 출력
# if weight is not None:
#     print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")
# else:
#     print("올바른 성별을 입력해주세요 (남자 또는 여자).")   
    
    
# 2.선생님 답변

def std_weight(height, gender): 
  if gender =="남자":
    return height*height*22
  else:
    return height * height*21
  
height = 175  #cm 단위
gender = "남자"
weight = round(std_weight(height/100, gender),2)   # round(x,2) 소수점 둘째 자리까지 표시   

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender,weight))


# 함수 문의
# get_ma44S 함수에서 return의 의미와 역할은 다음과 같습니다:
# return의 의미:
# return은 함수의 실행 결과를 호출한 곳으로 반환하는 역할을 합니다13. 이 함수에서는 계산된 44일 이동 평균값(ma44S)을 함수 외부로 전달합니다.
# return이 없을 경우의 문제:
# return이 없으면 함수는 암시적으로 None을 반환합니다3. 이 경우, 함수를 호출한 코드에서 이동 평균값을 사용할 수 없게 되어 원하는 결과를 얻지 못합니다.
# return 0의 의미:
# return 0은 주로 함수가 정상적으로 종료되었음을 나타내는 데 사용됩니다24. 하지만 이 함수에서는 실제 계산된 이동 평균값을 반환해야 하므로 return 0은 적절하지 않습니다.



### 2 표준 입출력
print("Python", "JAVA", sep=",", end="?")  # END : 원래는 줄바꿈인데 입력된걸로 바꿔줌 -> ?
print("무엇이 더 재밌을까요?")

score_file = open("score.txt","w",encoding="utf8")
print("수학 : 0", file=score_file)
print("영우 : 50", file=score_file)
score_file.close()

# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학 : 80 ")
# score_file.write("코딩 : 100 ")


score_file = open("score.txt","r",encoding="utf8")
while True:
  line = score_file.readline()
  if not line:
    break
  print(line)
score_file.close()

# 이 코드는 "score.txt" 파일을 읽고 그 내용을 한 줄씩 출력하는 프로그램입니다. 코드의 각 부분을 설명하겠습니다:
# score_file = open("score.txt","r",encoding="utf8"):
# "score.txt" 파일을 읽기 모드("r")로 열고, UTF-8 인코딩을 사용합니다.
# while True::
# 무한 루프를 시작합니다. 파일의 모든 줄을 읽을 때까지 계속됩니다.
# line = score_file.readline():
# 파일에서 한 줄을 읽어 line 변수에 저장합니다.
# if not line::
# 파일의 끝에 도달하면 readline()은 빈 문자열을 반환합니다. 이때 루프를 종료합니다.
# print(line):
# 읽은 줄을 출력합니다.
# score_file.close():
# 파일 사용이 끝나면 파일을 닫습니다.

# readline()은 파일에서 한 줄씩 텍스트를 읽어오는 파이썬 메서드입니다. 이 메서드의 주요 특징은 다음과 같습니다:
# 파일에서 한 번에 한 줄만 읽습니다14.
# 읽은 줄의 끝에 개행 문자("\n")를 포함합니다14.
# 더 이상 읽을 줄이 없으면 빈 문자열('')을 반환합니다2.
# readline() 메서드는 다음과 같은 상황에서 유용합니다:
# 대용량 파일을 처리할 때 메모리를 효율적으로 사용할 수 있습니다.
# 파일의 내용을 한 줄씩 순차적으로 처리해야 할 때 적합합니다.

# 이 코드는 파일의 끝에 도달했는지 확인하는 중요한 부분입니다. 여기서 if not line: break의 의미는 다음과 같습니다:
# line이 빈 문자열('')일 때 조건이 참이 됩니다.
# 파일을 읽을 때 readline() 메서드는 파일의 끝에 도달하면 빈 문자열을 반환합니다1.
# not line은 line이 빈 문자열일 때 True가 됩니다7.
# 따라서 이 조건문은 파일의 끝에 도달했을 때 루프를 종료(break)하라는 의미입니다.

# 퀴즈
# 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
# 보고서는 아래와 같은 형태로 출력되어야 합니다
# - x주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차 부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일명은 '1주차.txt', '2주차.txt',... 와 같이 만듭니다.  

# GPT답변
# for week in range(1, 51):
#     with open(f"{week}주차.txt", "w", encoding="utf8") as report_file:  #with 쓰면 close 안써도 됨
#         report_file.write(f"- {week}주차 주간보고 -\n")
#         report_file.write("부서 :\n")
#         report_file.write("이름 :\n")
#         report_file.write("업무 요약 :\n")

# print("모든 주간 보고서 파일이 생성되었습니다.")

# for 루프를 사용하여 1부터 50까지의 숫자를 반복합니다.
# 각 반복에서 "{week}주차.txt" 형식의 파일명으로 새 파일을 생성합니다.
# with 문을 사용하여 파일을 열고 자동으로 닫습니다.
# write() 메서드를 사용하여 보고서 템플릿을 파일에 작성합니다.
# 각 줄 끝에 \n을 추가하여 새 줄을 만듭니다.
# 모든 파일 생성이 완료되면 완료 메시지를 출력합니다.
# 이 프로그램을 실행하면 현재 디렉토리에 '1주차.txt'부터 '50주차.txt'까지의 파일이 생성됩니다. 각 파일은 지정된 형식의 보고서 템플릿을 포함하게 됩니다.

###3 class
#퀴즈
# 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

# (출력예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
# class House:  
#   #매물 초기화
#   def __init__(self, location, house_type, deal_type, price, completion_year):
#     pass
  
#   #매물 정보 표시
#   def show_detail(self):
#     pass
  
# #GPT 답변  
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     # 매물 정보 표시
#     def show_detail(self):
#         print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}년")

# # 매물 정보 생성
# houses = []
# houses.append(House("강남", "아파트", "매매", "10억", 2010))
# houses.append(House("마포", "오피스텔", "전세", "5억", 2007))
# houses.append(House("송파", "빌라", "월세", "500/50", 2000))

# # 매물 정보 출력
# print(f"총 {len(houses)}대의 매물이 있습니다.")
# for house in houses:
#     house.show_detail()  
    
# #나도 코딩 답
# house =[]
# house1=House("강남", "아파트", "매매", "10억", 2010)
# house2=House("마포", "오피스텔", "전세", "5억", 2007)
# house3=House("송파", "빌라", "월세", "500/50", 2000)

# house.append(house1)
# house.append(house2)
# house.append(house3)


# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()  


### 4. 예외처리
# try:
#   print("나누기 계산기")
#   num1=int(input("숫자 입력 : "))
#   num2=int(input("숫자 입력 : "))
#   print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
  
# #숫자말고 다른글자 입력시 에러 뜬다. 그때 에러 구문이 아닌 except 아래로 넘어감  
# # try 내부 구문은 에러발생시 except ValueError로 넘어간다
# # 0으로 나누면 zerodivisionerror 발생
  
# except ValueError:
#   print("값이 잘못된 에러 발생")  
  
  
# except ZeroDivisionError:
#   print("0으로 나눴을때 에러 발생")  
  
# except:
#   print("위의 에러 이외 모든 에러 알 수 없는 에러 발생")  
  
  
  
