# #목차
# 1.주석
# 2.데이터 타입
# 3.변수
# 4.표준출력
# 5.표준입력
# 6.if
# 7.반복문 for
# 8.while문
# 9.자료구조_리스트
# 10.자료구조_튜플
# 11.자료구조_딕셔너리
# 12.자료구조_셋
# 13.리스트컴프리헨션
# 14.문자열 처리
# 15.함수
# 16.파일 입출력
# 17.모듈과 패키지
# 18.객체와 클래스




##1.주석
# 주석(comment): 사용자가 코드 상에 메모를 작성할 수 있도록 제공하는 문법
# 주석을 사용하는 방법: 샵(#)으로 시작하시면 됩니다. 파이썬 해석기는 샵으로 시작하는 문장 또는 코드를
# 무시하기 때문입니다.

#샵 다음의 공백을 사용할 필요는 없습니다.
print("hello, world") # 화면에 hello, world를 출력하는 코드

# 현재 셀을 실행하는 방법 1. CTRL + ENTER
# 현재 셀을 실행하는 방법 2. ALT + ENTER -> 현재 셀을 실행 후, 새로운 셀을 생성

# 또한 주석은 특정 코드를 잠시 실행하지 않도록 할 때도 사용합니다.
# print("hello")
print("world")

# 특정 행에 대하여 주석으로 처리하는 방법: CTRL + /
#                                              ^--- 물음표 키에 있습니다.
print("apple")
# print("banana")
print("cherry")
print("durian")



##2.데이터 타입
# computer: compute + er -> 계산기

# 프로그래밍 언어: 수학을 확장한 개념

# 수학에서의 함수
# f(x) = 2x + 1 -> f(2) = 5

# 프로그래밍 언어에서의 함수: 특정 기능이 구현되어 있는 코드 덩어리
# print("hello, world")
#   ^--- 괄호 안의 값을 화면으로 출력하는 함수

# 행 번호 표시 방법: 도구 -> 설정 -> 편집기 -> 행 번호 표시 체크 -> 설정 클릭

# 데이터 타입(자료형): 값의 종류 또는 형식

# 1. 정수형
# 2. 실수형
# 3. 문자열형
# 4. 논리형

#
# 1. 정수형: 0, 양수, 음수를 포함하는 수 체계
#
print(10)
print(0)
print(-12)

# 정수형 값에 대하여 산술 연산이 가능합니다.

print(1 + 1)
#      ^--- 연산자와 피연산자 사이의 공백이나 개행은 무시됩니다.

print(1+1)
print(1
      +
      1)

# *: 곱셈 연산자
print(2 * 2)
print(2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2)

# 승수 연산자 또는 제곱 연산자: **, 밑수 ** 지수
print(2 ** 10)

# /: 나눗셈 연산자
print(5 / 3)
print(6 / 3)

# 나눗셈의 결과는 항상 실수입니다.
# //: 몫 연산자
print(5 // 3)

# %: 나머지 연산자
print(5 % 3)


# 산술 연산자에는 우선 순위가 있으며 이는 수학의 그것과 동일합니다.
print(2 + 2 * 2)

# 연산자의 우선 순위를 변경하기 위해 괄호를 사용할 수 있습니다.
# 다만 괄호는 소괄호(())만 사용이 가능합니다.
print((2 + 2) * 2)

# 괄호는 1개 이상 사용이 가능하며 중첩도 가능합니다.
print(((4 - 2) * 3) / (2 - 1))


# 123 = 1 * 10**2 + 2 * 10**1 + 3 * 10**0 = 100 + 20 + 3

# 다른 진수로의 표현 1. 2진수
# -> 1과 0을 사용하여 수를 표현하는 개념

# 10 -> 1010 = 1 * 2**3 + 1 * 2**1 = 8 + 2 = 10

# 해당 값이 2진수임을 나타내려면 접두어로 0b(binary)를 사용해야 합니다.
print(0b1010) # 파이썬은 10진수를 기본으로 사용합니다.

# 어떤 값을 2진수로 표현하려면 bin(binary) 함수를 사용해야 합니다.
print(bin(0b1010))
print(bin(10))


# 값이 커지면 커질수록 표현하기가 어려워진다는 단점이 있습니다.
print(bin(10))
print(bin(300000000000))


# 다른 진수로의 표현 2. 8진수

# 000 = 0
# 001 = 1
# 010 = 2
# 011 = 3
# 100 = 4
# 101 = 5
# 110 = 6
# 111 = 7

# 10 = 12 -> 1 * 8**1 + 2 * 8**0 = 8 + 2

# 해당 값이 8진수임을 나타내려면 접두어로 0o(octal)를 사용해야 합니다.
print(0o12)

# 어떤 값을 8진수로 표현하려면 oct(octal) 함수를 사용해야 합니다.
print(oct(0o12))
print(oct(10))


# 다른 진수로의 표현 3. 16진수

# 0000 = 0
# 0001 = 1
# 0010 = 2
# 0011 = 3
# 0100 = 4
# 0101 = 5
# 0110 = 6
# 0111 = 7
# 1000 = 8
# 1001 = 9
# 1010 = 10
# 1011 = 11
# 1100 = 12
# 1101 = 13
# 1110 = 14
# 1111 = 15

#  2진수: 01
#  8진수: 01234567
# 10진수: 0123456789
# 16진수: 0123456789101112131415
#                   A B C D E F

# 해당 값이 16진수임을 나타내려면 접두어로 0x(hex)를 사용해야 합니다.
print(0xA)
print(0xa) # 알파벳 대소문자를 구분하지 않습니다.

# 어떤 값을 16진수로 표현하려면 hex 함수를 사용하면 됩니다.
print(hex(0xA))
print(hex(10))


# 다른 진수로의 변화는 2진수, 8진수, 16진수만 가능합니다.
# 진수 또는 진법은 값에 대하여 다른 표현 방법일 뿐이므로 산술 연산에 사용될 수 있습니다.
print(10 + 0xA + 0b1010 + 0o12)


#
# 2. 실수형(부동소수점): 정수와 소수를 포함하는 수체계
#
print(3.14)
print(0.0)
print(-10.25)


# 정수와 마찬가지로 산술 연산이 가능합니다.
print(1.1 + 1.1)
print(1.1 - 1.1)
print(1.1 * 1.1)
print(1.1 ** 2)
print(1.1 / 1.1)
print(1.1 // 1.1)
print(1.1 % 1.1)


# 주의! 실수는 정수와는 다르게 다른 진수로의 표현을 지원하지 않습니다.
# -> 실수는 10진수로만 표현할 수 있습니다.
print(0xA.A)


# 과학적 표기법 또는 지수 표기법: 100.25 = 1.0025 * 10 ** 2

print(30000000000)
print(3 * 10 ** 10) # 단점 1. 코드가 장황해 집니다.
                    # 단점 2. 불필요한 연산이 발생합니다.

# 30000000000.0
# 밑수를 10이라고 가정하여 생략하고 지수만 표기합니다.
print(3.0e+10) # 3.0 * 10 ** 10 -> 과학적 표기법의 특성상 항상 실수로 표현됩니다.
print(3.0e10)  # 지수가 양수라면 덧셈 기호를 생략할 수 있습니다.
print(3e10)    # 소수 부분이 0이라면 이를 생략할 수 있습니다.


print(0.0001) # 1.0 * 10 ** -4
print(1.0e-4) # 지수가 음수인 경우, 부호를 생략할 수 없습니다.
print(1e-4)


# 값이 매우 크거나 또는 매우 작은 경우, 사용자의 의도와 상관 없이 지수 표기법으로 표현합니다.
print(1e15)
print(1e16) # 지수가 16 이상인 경우에는 지수 표기법으로 표현됩니다.
print(1e-4)
print(1e-5) # 지수가 -5 이하인 경우에는 지수 표기법으로 표현됩니다.


#
# 3. 문자열형: 문자가 연속되어 나열된 것(교안 64페이지)
#

# hello -> 1101000 1100101 1101100 1101100 1101111

# 사용 방법: 문장 또는 단어를 동일 인용 부호를 사용하여 감싸면 됩니다.
print("hello")
print('hello')

# 주의! 서로 다른 인용 부호를 사용하면 오류가 발생합니다.
#print("hello')


# 동일 기능의 서로 다른 인용 부호를 제공하는 이유
# hello, "world"
#print("hello, "world"")


# 문자열 안에 큰 따옴표를 포함하고 싶다면 작은 따옴표를 사용하시면 됩니다.
print('hello, "world"')

# 문자열 안에 작은 따옴표를 포함하고 싶다면 큰 따옴표를 사용하시면 됩니다.
print("hello, 'world'")



# 참고! 인용 부호와 고려하지 않고 포함하는 방법
# 백슬래시(\)를 사용하시면 됩니다.
#          ^--- 원화 기호

print("hello, \"world\"")
print('hello, \'world\'')

# 백슬래시 자체를 출력하고 싶은 경우
print("hello\\")


# 문자열에 대하여 제한적인 산술 연산자를 허용합니다.
# 다만 이는 수치 연산이 아니라 문자열 조작 연산입니다.
print("hello" + "world") # strcat("hello", "world")
# print("hello" - "world") # ERROR

print("hello" * 3)
# 덧셈 연산: 문자열을 연결
# 곱셈 연산: 문자열을 반복하여 연결


# apple
# banana
# cherry
# durian
print("apple")
print("banana")
print("cherry")
print("durian")


# 삼중 인용부호: 입력된 그대로 표현하기 위해 사용되는 문자열
print("""apple
banana
cherry
durian""")


print('''apple
banana
cherry
durian''')


print("""hello
world            goodbye
"goodbye", 'byebye'""")



#
# 4. 논리형: 진리 값을 표현하기 위한 타입
#

# 10 > 3 -> 참
# 10 < 3 -> 거짓

# 거짓은 0으로 표현
# 참은 0이외의 모든 수(0.14, -20, 300, ...)로 하되 참을 표현할 때는 대푯값으로 1을 사용

# 10 < 3 -> 0
# 10 > 3 -> 1

# 0 -> 1-1? 10<3?
# 1 -> 1+0? 10>3?

# 참과 거짓을 표현하기 위해 1과 0을 사용하는 것은 경우에 따라 매우 모호할 수 있습니다.
# 파이썬에서는 이를 해결하기 위해 참과 거짓에 대하여 숫자가 아닌 단어를 사용하기로 결정합니다.
# 참: True
# 거짓: False

print(True)
print(False)

# 주의! 단어의 첫 문자는 반드시 대문자이어야 합니다.


# 논리형 값도 산술 연산에 사용될 수 있습니다. 이는 내부적으로 여전히 1과 0으로 해석되기 때문입니다.
print(True + True)
print(True - True)


# 논리형의 사용 1. 비교 연산의 결과로 사용
print(10 > 3)  # 초과
print(10 < 3)  # 미만
print(10 >= 3) # 이상
print(10 <= 3) # 이하
print(10 == 3) # 같음
print(10 != 3) # 같지 않음


# 논리형의 사용 2. 논리 연산자의 피연산자로 사용 -> 제어구조




3.변수
# 변수(variable): 값을 저장하는 상자

# 생성 방법
# 변수명 = 값 ------------> 변수명은 상자의 이름으로 생각하시면 됩니다.
#       ^--- 대입 연산자: 해당 연산자를 기준으로 오른쪽의 값을 왼쪽의 변수에 저장하는 연산자

# 대입 연산자의 앞과 뒤에 공백은 무시됩니다.

# 변수 작명 규칙

# 1. 알파벳 대소문자와 숫자를 사용할 수 있습니다.
# age = 0
# age2023 = 0

# 2. 숫자로 시작할 수는 없습니다.
# age2023 = 0 OK
# 2023age = 0 ERROR

# 3. 대소문자를 구분합니다.
# age와 AGE는 서로 다른 변수입니다.

# 4. 특수 문자(+,-,*,! 등)와 공백은 사용할 수 없습니다.
# my-age = 20 ERROR
# my age = 20 ERROR

# 5. 단, 밑줄(_) 문자는 허용합니다. 밑줄 문자로 시작할 수도 있으며 단독으로도
# 사용할 수 있습니다.
# _ = 20
# _age = 30

# myage = 20
# myAge = 20  -> camel case
# my_age = 20 -> snake case

# 6. 예약된 키워드(True, False, if, for...)는 사용할 수 없습니다.


age = 20
#   ^--- 대입 연산자 앞 뒤의 공백은 무시됩니다.

# 변수에 저장된 값을 사용하는 방법은 단순히 변수명을 사용하시면 됩니다.
# 변수가 사용된 자리에는 변수가 가진 값으로 치환되기 때문입니다.
print(age) # -> print(20)

# 변수는 파이썬이 제공하는 모든 타입의 값을 저장할 수 있습니다.
x = 10
print(x)

x = 3.14
print(x)

x = "hello"
print(x)

x = True
print(x)

# 저장된 값이 계속 변할 수 있다하여 이를 변수라고 합니다.

# 참고! 변수는 비어 있는 상태로 생성할 수 없습니다.
name # ERROR

# 불가피하게 비어 있는 변수를 만들고 싶다면 None 키워드를 사용하시면 됩니다.
name = None # None의 의미는 값이 없다는 의미의 특수 키워드
print(name)

# 변수는 연산자와 함께 사용될 수 있습니다.
x = 20
y = 3

print(x + y) # -> print(20 + 3) -> print(23)
print(x - y)
print(x * y)
print(x ** y)
print(x / y)
print(x // y)
print(x % y)

# 변수의 증감
age = 0
print(age)

age = age + 1 # -> age = 0 + 1 -> age = 1
print(age)

# 복합 대입 연산자(+=, -=, *=, **=, /=, //=, %=)
age += 1
print(age)

# 참고! 파이썬은 증감 연산자(++, --)는 지원하지 않습니다.
# age += 1, age -= 1
# ++, --
++age
print(age)

# 값의 종류 확인
x = 10
print(x)

x = "10"
print(x)


# 값의 종류를 확인하려면 type 함수를 사용하시면 됩니다.
x = 10
print(type(x)) # int -> integer의 약자로 정수형

x = 3.14
print(type(x)) # float -> 실수형(float point, 부동 소수점)

x = "hello"
print(type(x)) # str: string의 약자로 문자열형

x = True
print(type(x)) # bool: boolean의 약자로 논리형

# a = 10
# b = 20
# c = 30
# d = 40
# e = 50

# 파이썬에서는 다수의 변수에 값들을 한 번에 대입할 수 있습니다.
a,b,c,d,e = 10,20,30,40,50  # 튜플의 언패킹

print(a)
print(b)
print(c)
print(d)
print(e)

# 주의! 위 방법을 사용할 때, 왼쪽 변수의 갯수와 오른쪽 값의 갯수가 일치하지 않으면
# 오류가 발생합니다.
# a,b,c = 10,20
a,b = 10,20,30


a = 10,20,30 # ?
print(a)




# 4.표준 출력
#표준 출력 :값을 모니터에 전송하는 개념
#print 함수를 사용하여 2개 이상의 값을 한번에 출력하려면 쉼표를 사용하면 된다
a=10
b=20
c=30

print(a,b,c) 
#괄호안에 공백과 탭, 개행은 무시됩니다
print(a,
      b,  c)

#분리자
#공백이 아닌 다른문자를 사용하려면 sep 변수를 사용하면 된다
#공백도 문장이며 다른문자와 차이는 눈에 보이지 않는 점이다, 공백을 문자열로 표현하려면 " " 
print(10,20,30)
print(10,20,30,sep='x')

print(10,20,30,sep='@$')

#만약 분리자를사용하고 싶지 않다면 아무 문자도 포함되지 않은 문자열을 사용하면된다, "" 공백문자도 없음
print(10,20,30,sep='')

#제어문자
#1 개행문자 \n (newline)
print("hello\nworld")

#2. 탭 문자: \t(tab)
print("hello\tworld")

#3. 백스페스 문자 : \b(backspace)
print("hello\bworld")

#분리자에 제어 문자 사용 가능
print(10,20,30,sep="\n")
print(10,20,30,sep="\t")

#1개 이상 사용가능
print(10,20,30,sep="\t\t")

#조합 가능
print(10,20,30,sep="\t\n")

# print 함수는 모든 값을 출력한 후, 개행을 수행합니다
print(10)
print(20)
print(30)

#종료자: 모든 값을 출력한 후, 마지막으로 출력할 문자열을 설정하는 변수(end)
print(10) # -> print(10,end="\n")
print(20,end="!")
print(30,end="\t")
print(40,end="")
print(50)

#종료자에 1개이상의 문자 (제어 문자 포함) 사용 가능
#서로 다른 제어 문자를 사용할 수 있습니다

#연습 문제1
name="홍길동"
age=20
#위 변수를 사용하여 다음과 같이 출력해 보세요
#이름: 홍길동, 나이: 20
print("이름:",name, ", 나이:",age) #일반적인 답변, 쉼표 앞에 공백이 있음 -> 이름: 홍길동 , 나이: 20


print("이름: ",name,", 나이", age, sep="") # sep=""


name="홍길동"
age=20

print("이름: "+ name + ", 나이: " + age) # 오류 발생  age가 정수라서 문자열로 바꾸어야 함, 특정type 으로 바꾸어주는 함수 이용

# 변환함수 : 어떤 값을 특정type 으로 바꾸어주는 함수 이용
#1. int
#2. float
#3. str
#4. bool



#1. int() : 정수 타입으로 변환
print(int(3.4))
print(int(True),int(False)) #참 :1, 거짓 : 0
print(int("1")) #문자 1을 정수 1로 변환

x=1 # x라는 변수에 1을 저장하는 코드, 계산용 숫자 1
y="1" # y변수에 49를 저장하는 코드. 컴퓨터상에서는 49라고 인식, 문자 1은 내부적(아스키 ASCII 코드)으로 49로 저장됨, 숫자1을 표현하는 문자
print(int(y)) #49라는 문자값을 1로 변환하라는 의미

print(ord("1")) # ord : ordinary 원래의 값으로 표현 49

print(int("x")) # ?, 모든 문자를 숫자로 바꿀수 있는 것은 아니다. 숫자로 이루어진 문자열만 숫자로 바꿀 수 있다

#다른 진수의 패턴으로 이루어진 문자열에 대하여 정부 변환을 하려면 base변수에 해당 진수를 전달하면 됩니다
print(int("A",base=16))
print(int("1010",base=2))
print(int("0xb",base=16))

print(int("3.14")) # 실수로 된 문자열이지만, "."  이 숫자가 아니라서 변환이 안된다

# 2. float() : 어떤 값을 실수 타입으로 변환하는 함수
print(float(3))
print(float(True),float(False))
print(float("3.14"))
print(float("10"))

print(int(float("3.14"))) #3.14문자열을 진짜 실수로 바꾸어준 다음 int로 정수형 변환

#주의! 문자열에 숫자가 아닌 문자가 포함된 경우 오류가 발생합니다, 단, 점(.)은 예외 입니다

#실수는다른 진수에 대한지원이 되지 않음으로 오류가 발생합니다
print(float("A",base=16))

print(float(int("A",base=16)))

#3. str() 어떤 값을 문자열로 변환하는 함수
print(str(3))
print(str("3.14"))
print(str("True"))

# print 함수는 문자열을 출력한다. print(3) 2진수로 저장된다. 아스키코드로 51로 전송해서 모니터에는 3이라는 문자열을 출력한다

# 4. bool() 어떤 값을 진리 값으로 변환하는 함수, 0이외의 모든 수는 참True, 0은 거짓
print(bool(0))
print(bool(1))
print(bool(-10))

print(bool("")) # ? 빈 문자열도 거짓으로 해석, 
print(bool("ㅁ")) # 문자가 1개 이상 포함된경우 참으로 해석
print(bool(" ")) # 공백 도 문자입니다

#연습 문제
name="홍길동"
age=20

# print("이름: "+ name + ", 나이: " + age) 
# 오류 발생  age가 정수라서 문자열로 바꾸어야 함, 특정type 으로 바꾸어주는 함수 이용

print("이름: "+ name + ", 나이: "+str(age))

name="홍길동"
age=20

print("이름: ",name,", 나이: ", age, sep="")
print("이름: "+ name + ", 나이: "+str(age))
# 변수가 많아지면 복잡해질 것 이다

#형식 문장열의 사용(C style)
name="홍길동"
age=20

# usage: "형식 문자를 포함한 문자열" % (값, ...)
print("이름: %s, 나이: %d" %(name, age))  # name은 문자열로 %s (string), age는 10진수로 %d (dacimal 10진 정수)

#만약 출력할 값이 1개라면 뒤의 소괄호를 생략할 수 있습니다
print("이름: %s" %name)

#형식 함수 (메서드)의 사용 -> 파이선 3.0이상에서만 사용 가능 (2는 없음 이제)
name="홍길동"
age=20
#                                    0     1
print("이름: {0}, 나이: {1}".format(name, age))  #첫번쨰 괄호에 {} 0, 두번째 괄호에 {} 1을 치환한다
# 만약 format함수에 전달된 순서로 출력한다면 번호를 생략할 수 있다
print("이름: {}, 나이: {}".format(name, age))

#번호를 제공하는 이유 1) 출력 순서를 고려하지 않고 값을 함수에 전달하기 위해, 
print("이름: {1}, 나이: {0}".format(age, name))

#번호를 제공하는 이유 2) 값의 중복 전달을 피하기 위해
print("이름: {0}, 나이: {1}, 이름: {0}".format(name, age))

#참고자료 형식 문자열(f-string)의 사용 -> 파이썬 3.6 이상에서만 사용 가능
#버전 확인
import sys
print(sys.version)  # 3.8.10 -> 3.6이상 버전


name="홍길동"
age=20

print("이름: {}, 나이: {}".format(name, age)) # 기존 문자열 (3.0)
print(f"이름: {name}, 나이: {age}")           # 형식 문자열 

# 중괄호 안에 변수가 값 뿐만 아니라 수식도 넣을 수 있습니다
dan = 2
num = 9
print(f"{dan} x {num} ={dan * num}")

# 숫자의 출력형식 지정 1. 특정 진수로의 출력
print("{0:d}".format(10)) # d : decimal의 약자로 10진 정수로 출력
print("{0}".format(10)) # d : 10진수가 기본이므로 이를 생략할 수 있습니다.

print("{0:b}".format(10)) # b : binary의 약자로 2진수로 출력
print("{0:o}".format(10)) # o : octal의 약자로 8진수로 출력
print("{0:x}".format(10)) # x : hex의 약자로 16진수로 출력
print("{0:X}".format(10)) #

# #을 추가하면 해당 진수의 접두어가 자동 추가된다
print("{0:#b}".format(10)) # b : binary의 약자로 2진수로 출력
print("{0:#o}".format(10)) # o : octal의 약자로 8진수로 출력
print("{0:#x}".format(10)) # x : hex의 약자로 16진수로 출력
print("{0:#X}".format(10)) #


# 숫자의 출력형식 지정 2. 폭 지정 후 정렬하기 기능
print("{0:d}".format(10))  
print("{0:<10d}".format(10)) #폭 10으로 지정 , 왼쪽정렬 <

print("|{0:d}|".format(10))  # 폭이 있는지 확인하려고 | 막대를 세움
print("|{0:<10d}|".format(10)) # 10d : 폭 10으로 지정 , < : 왼쪽정렬 
print("|{0:>10d}|".format(10)) # 10d :폭 10으로 지정 , > : 오른쪽정렬 
print("|{0:10d}|".format(10)) # 10d :폭 10으로 지정 , 꺽쇠 생략시 : 오른쪽정렬이 기본 
print("|{0:^10d}|".format(10)) # 10d :폭 10으로 지정 , ^ : 가운데 정렬 
print("|0123456789|") #10개

# 출력 형식 지정 3. 정렬 시, 폭은 기본적으로 공백 문자로 채워집니다
# 공백이 아닌 다른 문자를 사용 할 수 있습니다
print("{0:0>10d}".format(10))
print("{0:*>10d}".format(10))
print("{0:#>10d}".format(10))

print("{0:.3f}".format(0.123487))

print("{0:,}".format(7458200))

print("{0:.1%}".format(0.3258))

print("{0:.1e}".format(9250000))
print("{0:.3e}".format(9250000))
print(f"{9250000:.3e}")



#5 표준 입력
# 표준 입력 : 키보드로 부터 데이터를 입력 받는 것
# 표준 입력을 수행하려면 imput 함수를 사용하면 됩니다

# 사용 방법
# 변수명 = input()

# input함수는 사용자가 엔터를 입력하기 전까지 대기하고 있다가 사용자가 엔터를 입력하는 순간
# 엔터를 입력하기 전까지의 모든 입력된 문자를 문자열에 저장하여 돌려줍니다

#사용자로부터 이름을 입력 받아 그 값을 출력하는 코드
name = input()
print("->", name)

# 위의 코드의 경우 뭘 입력하라는건지가 없고 그냥 입력칸만 뜬다. 입력 칸에 대한 설명 문구가 필요하겠다.
print("이름을 입력해주세요")
name = input()
print("->", name)

#입력 시 메시지를 출력하려면 괄호 안에 메시지를 전할하시면 됩니다
name = input("이름을 입력해주세요")
print("->", name)

# 연습문제1, 사용자로 부터 정수 하나를 입력 받아 그 값을 제곱하여 출력하는 코드를 구현해보세요. 이 때, 정수만 입력된다고 가정합니다
# 예) 정수 입력 : 2 -> 4

number = input("정수 입력해주세요")
print("", number**2)

# input함수는 사용자가 엔터를 입력하기 전까지 대기하고 있다가 사용자가 엔터를 입력하는 순간
# ***엔터를 입력하기 전까지의 모든 입력된 문자를 문자열에 저장하여 돌려줍니다. 문자열이라서 제곱이 안된다 -> 입력된 문자열을 정수로 바꾸어 줘야한다

# 연습문제1, 사용자로 부터 정수 하나를 입력 받아 그 값을 제곱하여 출력하는 코드를 구현해보세요. 이 때, 정수만 입력된다고 가정합니다
# 예) 정수 입력 : 2 -> 4

number = input("정수 입력해주세요")
number = int(number)
print("", number**2)

num = int(input("정수 입력"))
print(num**2)

# 연습문제2 사용자로 부터 원의 반지름을 입력 받아 원의 넓이를 출력하는 프로그램을 구현해 보세요
# 이 떄, 반지름은 정수 또는 실수만 입력된다고 가장하고 원주율은 3.14로 합니다
# 원의 넓이를 구하는 공식 : 반지름 * 반지름* 원주율
# 예) 반지름 입력 : 2 -> 원의 넓이 : 12.56

r = float(input("반지름 입력")) #float 정수, 실수 구분없이 숫자에서 만능
print(r*r*3.14)

#사용자로 부터 자연수를 입력받아 짝수이면 True, 홀수이면 False를 출력하는 코드 구현. 자연수만 입력
#예) 자연수 입력 : 2 -> True, 자연수 :3 -> False
# True
num = int(input("자연수 입력"))
result = (num%2) == 0
print(result)





#if절
# 제어구조 또는 제어문 : 코드에 대한 실행의 흐름을 제어하기 위해 제공되는 문법
#1. 분기
# - 조건에 따른 분기
# - 값에 따른 분기

#2. 반복
# - 조건에 따른 반복
# - 값에 따른 반복

# 조건에 따른 분기: if -> 조건이 참일 때, 특정 코드를 수행하는 문법
# 사용방법
# if 조건식: <-- 반드시 끝에는 콜론을 입력해야 합니다.
#파이썬은 들여쓰기로 나눈다

# if age > 19:
#     print("성인 입니다.");  권장 들여쓰기 4칸(몇칸 해도 괜찮다, 규칙만 맞게해라)


             

# 사용자로부터 정수를 입력 받아 그 값이 0인지아닌지를 판별하는 코드를 구현해 봅니다

num = int(input("정수 입력: "))

if num == 0:
  print("zero")

if num != 0:
  print("not zero")  

#연습 문제1. 사용자로부터 자연수를 입력 받아 그 값이 짝수 인지 홀수인지를 판별하는 프로그램을 구현해 보세요
# 이때 입력은 자연수만 된다고 가정합니다

num = int(input("자연수 입력"))
result = (num%2) == 0

if result == True:
  print("짝수")

if result == False:
  print("홀수")  



#선생 답안
num = int(input("자연수 입력"))

if (num%2) == 0:  # 괄호를 써주는게 좋다. 대입 연산자는 우선순위가 뒤라서 괄호 안써도 상관없는데 혹시나 원하는 연산이 먼저 안일어날 수도 있다. 
  print("짝수")

if (num%2) != 0:
  print("홀수")  

#참고 우선 연산자 순위 https://dojang.io/mod/page/view.php?id=2461 but 그냥 괄호 써라! 헷갈리지 말고

#이전의 코드는 경우에 따라 불필요한 연산이 발생할 수 있다는 단점이 있습니다
# 이를 해결하기 위해 파이썬에서는 if - else 라는 상호베타적인(두 조건이 동시에 일어나지 않음) 구문을 활용한다

num = int(input("자연수 입력"))

if (num%2) == 0:  # 괄호를 써주는게 좋다. 대입 연산자는 우선순위가 뒤라서 괄호 안써도 상관없는데 혹시나 원하는 연산이 먼저 안일어날 수도 있다. 
  print("짝수")

else:
  print("홀수")  

#사용자로부터 정수를 입력 받아 그 값이 0, 양수, 음수인지를 판단하는 프로그램을 생각해 봅시다 (3개의 사건은 상호베타가 아니다)
num = int(input("정수 입력"))

if num == 0:
  print("zero")
if num > 0:
  print("positive")  
if num < 0:
  print("negative")  

#이전의 코드는 경우에 따라 불필요한 연산이 발생할 수 있다는 단점이 있습니다
# 이를 해결하기 위해 파이썬에서는 분기를 중첩할 수 있다. 분기문 안에 분기를 또 집어 넣는다. but 코드의 중첩이 발생하면 가독성이 떨어진다.

num = int(input("정수 입력"))

if num == 0:
  print("zero")
else:
  if num > 0:
    print("positive")  
  else:
    print("negative") 

#이전의 코드는 코드의 중첩이 발생하면서 가독성이 떨어집니다.
# 이를 해결하기 위해 파이썬에서는 다중 분기를 제공합니다 
# if 조건식1:
#    조건식1이 참일때 수행할 코드
# elif 조건식2:                     <--- else if = elif
#    조건식2이 참일때 수행할 코드
# elif 조건식3:                     
#    조건식3이 참일때 수행할 코드
# ....
# else:                     
#    어떠한 조건식도 만족하지 않을때 수행할 코드

num = int(input("정수 입력"))

if num > 0:
  print("positive")
elif num < 0:
  print("negative")  
else:
  print("zero")

# 연습문제 3. 사용자로 부터 나이를 입력 받아 출력하는 프로그램을 구현해 보세요
# 이 때 나이는 정수만 입력된다고 가정
# 나이의 유효 범휘는 0 ~ 150하며 이를 벗어날 경우, 오류 메세지를 출력합니다
# 당신의 나이는(0~150)세 입니다.
# 당신의 나이는(-2)세 입니다. -> 잘못 입력했습니다.

num = int(input("나이 입력 : "))

if 0 < num < 150:
  print("당신의 나이는 :",num, "세 입니다")
else:
  print("잘못 입력했습니다")


#선생답변
num = int(input("나이 입력 : "))

if num < 0:
  print("잘못 입력하셨습니다")
elif num >150:
  print("잘못 입력하셨습니다")  #코드의 중복이 발생
else:
  print(f"당신의 나이는 {num}세 입니다.")  

#논리 연산자: 논리값을 피연산자로 하는 연산자, 논리곱 연산자
# 1. and
# 2. or
# 3. not
# 1. and : 2개의 피연산자 모두 참인 경우에만 참을 반환하고 그렇지 않은 경우에는 거짓을 반환하는 연산자
print(True and True)
print(False and True)
print(True and False)
print(False and False)

#논리 연산자: 논리값을 피연산자로 하는 연산자, 논리합 연산자
# 1. and
# 2. or
# 3. not
# 2. or : 2개의 피연산자 모두 참인 경우에만 참을 반환하고 그렇지 않은 경우에는 거짓을 반환하는 연산자
print(True or True)
print(False or True)
print(True or False)
print(False or False)

# 3. not : 반전 연산자
print(not True)
print(not False)

num = int(input("나이 입력 : "))

if num < 0 or num > 150:
  print("잘못 입력하셨습니다")
else:
  print(f"당신의 나이는 {num}세 입니다.")  

num = int(input("나이 입력 : "))

if 0 <= num <= 150
  print(f"당신의 나이는 {num}세 입니다.") 
else
  print("잘못 입력하셨습니다")

 


 #7 반복문
 # 자료구조
# 데이터 그리고 데이터에 적용할 수 있는 함수나 명령의 모음 -> 장바구니
# 파이썬의 기본으로 제공하는 자료 구조
#1. 리스트
#2. 튜플
#3. 딕셔너리
#4. 셋

# 1. 리스트 : 데이터의 추가된 순서가 유지되고 중복을 허용하는 자료구조
# 리스트 생성하는 방법
# [값, 값1, 값2, 값3,...]
#  리스트 안에 값들을 원소, 요소, 항목이라고 함
print([1,2,3,4]) #순서 유지, 중복 허용

#파이썬에서 제공하는 모든 타입의 값을 저장할 수 있습니다
print([10,3.14,"hello",True,[1,2,3]])

# 값(원소) 기반의 반복 -> 자료구조 안에 있는 원소의 갯수만큼 반복을 수행, 원소 타입은 상관없다. 갯수가 중요하다
# for 변수명 in 리스트:
# ....반복할 코드
# ....반복할 코드

# hello  x 5번 반복
for i in [1,2,3,4,5]:  # i말고 다른 변수 써도 된다,
  print(i, "hello")


for x in [10,3,14,"hello",False]:  # i말고 다른 변수 써도 된다,
  print(x, "hello") 

#연습문제 1 사용자로부터 구구단의 단을 입력 받아 해당 단을 출력하는 코드를 구현해 보세요
# 이때 2~9 사이 값만 입력된다고 가정

dan = int(input("단 입력(2~9) : "))  #나의 오답
for i in [1,2,3,4,5,6,7,8,9]: 
  print(f{dan} "x" i = {dan*i} )

#선생 답변
dan = int(input("단 입력(2~9) : "))
for i in [1,2,3,4,5,6,7,8,9]:  
  print(f"{dan}x{i}={dan*i}")

# 원소 갯수 너무 많아지면 어떻게 반복 시킬까? 수의 집합을 생성해주는 함수를 이용
# range : 정수 집합을 생성하는 함수
# usage : range(start, stop, step)
# start : 시작값, stop : 끝 값(포함되지 않음) -> [start, stop) 반개 구간
# step : 값 사이 간격

for x in range(1,11,1): #10까지 포함 할수 있도록 하는 자연수
  print(x, end=" ")


##연습문제 2 사용자로부터 구구단의 단을 입력 받아 해당 단을 출력하는 코드를 구현해 보세요
# 이때 2~9 사이 값만 입력된다고 가정. range 함수 사용

dan = int(input("단 입력(2~9) : "))
for i in range(1,10,1):  
  print(f"{dan}x{i}={dan*i}")

#range함수 특징1. 간격이 1이라면 생략할 수 있다
for i in range(0,5):  
  print(i, "hello")




#2. range함수 특징 간격이 생략되어있고 시작값이 0이라면 생략할 수 있다
for i in range(5):  
  print(i, "hello")

#만약 반복을 N번 하려면 range(N) 으로 사용하시면 됩니다



#연습문제 3 구구단 2단~9단 출력하기. 단과 단 사이에 빈 줄 삽입
for i in range(2,10):
  for n in range(1,10):
    print(i,"x",n)                  #나의 답변

#선생 답변
for dan in range(2,10):
  print(f"< {dan}단 >")  
  print(f"{dan} x 1 = {dan*1} ")
  print(f"{dan} x 2 = {dan*2} ")
  print(f"{dan} x 3 = {dan*3} ")
  print(f"{dan} x 4 = {dan*4} ")  
  print(f"{dan} x 5 = {dan*5} ")
  print(f"{dan} x 6 = {dan*6} ")  
  print(f"{dan} x 7 = {dan*7} ")
  print(f"{dan} x 8 = {dan*8} ")             
  print()  # 빈 줄 추가

#상기 코드 반복문도 중첩 활용해서 코드 간략화 해보자
for i in range(2):
  for j in range(3):
    print("hello")  # -> hello는 6번이 나옴.

#연습문제 4 다음의 코드를 실행하지말고 분석하여 출력결과를 예측해보세요

for i in range(3):
  print(i, "->",end=" ")  #end가 없으면 개행이 된다. end="\n" 이렇게 써도 개행과 같다.모든 값을 출력한 후, 마지막으로 출력할 문자열을 설정하는 변수(end)

  for j in range(4):
    print(j, end=" ")

  print() #빈줄 삽입 , ? 빈줄 삽입 넣었는데 빈줄 삽입이 안되지

  # 0-> 0 1 2 3

  # 1-> 0 1 2 3 

  # 2-> 0 1 2 3 

#연습문제 3-2 구구단 2단~9단 출력하기. 단과 단 사이에 빈 줄 삽입, 2중 for 루프 활용

for dan in range(2,10):
  print(f"< {dan}단 >")  
  for i in range(1,10):
    print(f"{dan} x {i} = {dan*i}")          
  print()  # 빈 줄 추가



#8 while문
# while : 조건 기반의 반복문, 조건식이 참인 동안 계속 반복된다
# 사용방법
# while 조건식:
# ......조건식이 참인 동안 반복할 코드
# ......조건식이 참인 동안 반복할 코드

# hello x 3

for cnt in range(3):
  print(cnt, "hello")
print() #띄워쓰기

# while의 경우, 파이썬이 반복을 제어하지 않으므로 이를 직접 수행해야 합니다.
cnt = 0 # 반복의 횟수를 기록하기 위한 변수
while cnt < 3: 
  print(cnt, "hello")
  cnt += 1

##연습문제 1 사용자로부터 구구단의 단을 입력 받아 해당 단을 출력하는 코드를 구현해 보세요
# 이때 2~9 사이 값만 입력된다고 가정. range 함수 사용
# while문 활용 할 것

dan = int(input("단 입력(2~9) : "))
i = 1
while i < 10: 
  print(f"{dan}x{i}={dan*i}")
  i += 1

# 연습 문제: 사용자로부터 구구단의 단을 입력 받아 해당 단을 출력하는 프로그램을
# 구현해 보세요. 이 때, 구구단의 단은 2부터 9사이의 값만 입력된다고 가정합니다.
# 그리고 while 루프를 사용해야 합니다.

# 구구단 입력(2~9): 2
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 9 = 18

dan = 2

num = 1
while num < 10:
  print(f"{dan} x {num} = {dan*num}")

# 무한 반복 코드

# while True:
# ....무한반복할코드
# ....무한반복할코드

# break: 반복을 즉시 중단하고 반복문을 탈출하는 키워드

# 메뉴 주문 시스템을 생각해 봅니다.

while True:
  print("# 메뉴 #")
  print("1. 짜장")
  print("2. 짬뽕")
  print("3. 탕슉")
  print("--------")
  num = input("입력(0.주문완료): ")

  # ...
  if num == "0":
    print("주문이 완료되었습니다. 감사합니다.")
    break

# 반복(for, while)의 흐름을 제어하는 키워드
# 1. break: 반복을 즉시 중단하고 반복문을 탈출하는 키워드
# 2. continue: 반복을 즉시 중단하고 그 다음 반복을 수행하는 키워드

# 1부터 10까지의 자연수 중 짝수만 출력하는 프로그램을 생각해 봅시다.
for n in range(1,11):
  if (n % 2) == 0:  # 짝수
    print(n, end=" ")

print()
for n in range(1,11):
  if (n % 2) != 0:
    continue
    
  print(n, end=" ")

#연습 문제 숫자 알아맞추기 게임

#숫자 알아맞히기 게임을 시작합니다
#1부터 100사이의 값을 입력해 주세요
#입력 50
#50보다는 큽니다
#입력 75
#75보다는 작습니다
#입력 63
# 정답입니다. 3번만에 맞추셨습니다.

import random
print(random.randint(1,100))



# 1부터 100사이의 값 중 임의의 정수를 구하는 방법, 랜덤 주사위~

import random
# random.randint(시작 값 ,끝 값)  끝 값까지 포함
r = random.randint(1,100)

while True: 
  i = int(input("숫자 입력(1~100) : "))
  if i > r:
    print(f"{i} 보다 작습니다")
  elif i < r:
    print(f"{i} 보다 큽니다")
  else:
    print(f"{i} 정답 입니다")
    break    



# 1부터 100사이의 값 중 임의의 정수를 구하는 방법, 랜덤 주사위~ 선생답변
import random
# random.randint(시작 값 ,끝 값)  끝 값까지 포함
answer = random.randint(1,100)

cnt = 0
while True: 
  num = int(input("숫자 입력(1~100) : "))
  cnt += 1
  if  num > answer:
    print(f"{num}보다는 작습니다.")
  elif  num < answer:
    print(f"{num}보다는 큽니다.") 
  else:
    print(f"정답입니다. {cnt}번 만에 맞추셨습니다")
    break    

# while도 중첩이 가능합니다.



# 9.자료형 리스트
#컴프리헨션(comprehension)
# 자료구조
# 데이터와 데이터에 적용할 수 있는 함수나 연산의 모음을 의미한다
# 장바구니

# 파이썬이 기본적으로 제공하는 자료구조
# 1. 리스트
# 2. 튜플
# 3. 딕셔너리
# 4. 셋

#리스트 : 데이터의 추가된 순서가 유지되고 중복을 허용하는

#리스트를 생성하는 방법
#1. 비어있는 리스트를 생성
l = []
print(l)

#2.초깃값을 사용한 생성
# [값, 값1, 값2, 값3,...]
#  ^--원소, 요소, 항목
print([1,2,3,4])

print([4,1,3,2]) #순서
print([1,1,1,1]) #중복

#파이썬에서 제공하는 모든 타입의 값을 저장할 수 있다. True, "hello", [1,2,3]
print([1,1,1,True, "hello", [1,2,3]])

# 인덱싱 인덱스를 사용하여 특정 원소를 참조하는 기능
#각 원소에 가상의 번호를 부여한다. 
#    -8 -7 -6 -5 -4 -3 -2 -1  음의 인덱싱
#     0  1  2  3  4  5  6  7 <-- 인덱스. 리스트의 시작점과 떨어진 거리. 첫번째는 0, 두번째는 1 ,,,
l = [11,22,33,44,55,66,77,88]
print(l)

#usage: 리스트명[인덱스]
print(l[0])
print(l[7])

#!주의 : 존재하지 않는 원소에 대하여 인덱싱을 수행하면 오류가 발생한다

# 현재 리스트에 원소가 몇개인지 알아야된다, 실시간 자료를 어떻게 알 수 있을까?
# 자료구조 안의 갯수를 알려주는 함수 : len()
print(len(l))

# 리스트의 원소의 갯수가 N개 일때, 마지막 인덱스는 N-1(0~(n-1))
print(l[len(l)-1]) # 마지막 원소 참조

print(l[-1]) #마지막 원소 -1로 사용   # -8 -7 -6 -5 -4 -3 -2 -1
#!주의 : 존재하지 않는 원소에 대하여 인덱싱을 수행하면 오류가 발생한다

# 현재 리스트에 원소가 몇개인지 알아야된다, 실시간 자료를 어떻게 알 수 있을까?
# 자료구조 안의 갯수를 알려주는 함수 : len()
print(len(l))

# 슬라이싱(slicing) : 인덱스를 사용하여 일부 연속된 구간이나 일정 간격으로 원소를 참조할 수 있는 기능
#    -8 -7 -6 -5 -4 -3 -2 -1  음의 인덱싱
#     0  1  2  3  4  5  6  7 <-- 인덱스. 리스트의 시작점과 떨어진 거리. 첫번째는 0, 두번째는 1 ,,,
l = [11,22,33,44,55,66,77,88]
print(l)

# usage : 리스트명 [시작 인덱스:마지막 인덱스:간격]  , 마지막 인덱스는 포함되지 않는다

print(l[1:6:1])
print(l[1:6:2])

print(l[5:8:1]) #마지막 인덱스를 포함 시키기 위해서 마지막 인덱스보다 큰 다음 인덱스인 8을 사용했다.(100넣어도 된다) 리스트의 마지막 원소를 포함하기 위함
print(l[5:100:1])

#간격이 1이라면 이를 생략 할 수 있습니다
print(l[0:8:])
print(l[0:8]) # : 콜론도 생략 가능
print(l[0:]) #마지막 원소를 포함하는 경우라면 마지막 인덱스를 생략할 수 있습니다, 콜론은 생략하면 인덱스 l[0]이 돼서 안됨
print(l[:]) # 시작 인덱스가 0이라면 이를 생략할 수 있다
#생략은 순서는 상관없음. 필요에 맞게 생략하면 된다
print(l[::2])
print(l[:2:])

# 슬라이싱의 경우, 잘못 사용하면 오류가 발생하는것이 아니라 비어있는 리스트가 반환됩니다
print(l[5:0:2])

#음수 인덱싱 슬라이싱
print(l[-1:-7:-1])
print(l[-1::-1])
print(l[::-1])

#원소의 갱신
l=[11,22,33,44]

#usage : 리스트명[인덱스] = 값
l[0] = 0
l[-1] = 0
print(l)

#리스트 끝에 추가 : append(값)
l=[11,22,33,44]
l.append(100)
l.append(200)

print(l)

#임의의 위치에 삽입 : insert(인덱스, 값)
#  0  1   2  3
l=[11,22,33,44]
l.insert(2,100)
print(l)

#리스트에 대해서 덧셈, 곱셈 연산자를 사용할 수 있습니다
print([1,2,3]+[4,5,6])  # 두 리스트를 연결
print([1,2,3]*3)  #리스트를 반복하여 연결

# 기존 리스트에 새로운 리스트를 추가: extend(리스트)
l = [1,2,3]
l.extend([111,222,333])
print(l)

#리스트 삭제
#1. 인덱스를 사용한 삭제: del
l=[1,2,3,4]
del l[0]
del l[-1]
print(l)

# 2. 값을 사용한 삭제 : remove(값)
l=["apple", "banana", "cherry","durian","apple"]
l.remove("apple")  #앞에 사과만 삭제된다. 처음으로 일치하는 원소만 삭제한다

print(l)

# 3. 값의 추출(잘라내기) : 뽑아낸다 손에 들고 있다 : pop(인덱스)
l=["apple", "banana", "cherry","durian","apple"]
value = l.pop(0)
print(value, l)
print(value)
print(l)

value = l.pop() # 인덱스 생략시 마지막 원소가 추출된다
print(value, l)

# 검색 수많은 데이터중 원하는 값만 찾아내는 기능
l=["apple", "banana", "cherry","durian","apple"]
# 1. count(값): 전달된 값과 일치하는 모든 원소의 갯수를 반환
print(l.count("apple")) # --> 2개
print(l.count("cherry"))  # --> 1개
print(l.count("orange"))  # --> 0개

# 검색 수많은 데이터중 원하는 값만 찾아내는 기능
l=["apple", "banana", "cherry","durian","apple"]
# 2. index(값): 전달된 값과 처음으로 일치하는 원소의 인덱스 반환 
print(l.index("banana")) # --> 1
print(l.index("apple")) # --> 0

l=["apple", "banana", "cherry","durian","apple"]
#위 리스트에서 Cherry라는 값이 존재하는지의 유무를 확인하고 만약 존재한다면 존재합니다하고 출력하고 
# 그렇지 않다면 존재하지 않습니다라고 출력하는 코드

if l.count("cherry") > 0:
  print("exist")
else:
  print("not exist") 

# 멤버십 연산자 : 자료구조 내에 특정 값이 존재하는지의 유무를 논리값으로 반환합니다
# usage: 값 in 자료구조

if "cherry" in l:
  print("exist")
else:
  print("not exist")  

# hello -> 5행으로 추출하려면

#C언어 에서는 문자를 인덱싱으로 접근
#        01234
# str = "hello"
# for (size_t i = 0; i < strlen(str); i+=1){
#    printf(str[i])
#}

#문자열은 문자의 리스트

for ch in "hello":
  print(ch)

l=[1,3,5,7,9,2,4,6,8]
# 오름차순 정렬

l.sort()
print(l)

l.sort(reverse=True) #내림차순 정리
print(l)




#10. 자료 튜플
#튜플(tuple) : 수정이 불가능한 리스트
#비어있는 튜플 
t=()
print(type(t),t)

#초깃값을 사용한 생성
t = (1,2,3,4)
print(t)

print((4,1,3,2)) # 추가된 순서가 유지
print((1,1,1,1)) # 중복 허용

#리스트와 마찬가지로 파이썬이 제공하는 모든 타입의 값을 저장 할 수 있습니다.

#인덱싱과 슬라이싱 지원
t=(1,2,3,4)
print(t[-1])
print(t[:])

#튜플은 삭제나 수정이 불가
t=(1,2,3,4)
# del t[0]  삭제 불가
# t.append(10)   추가 불가
# t[-1] = 0  변경 불가

#원소가 1개인 자료구조를 생각해 봅니다
l = [0]
print(type(l),l)

t = (0)
print(type(t),t)  #튜플은 튜플로 인정하지 못하는 이유는 기존의 산술 연산체계 때문이다. 괄호가 먼저 계산되는 산술 연산체계
# print((2+2)*2)  print((4)*2) -> print((4,4))

#원소가 1개인 튜플을 생성하려면 원소 뒤에 쉼표를 사용해야 합니다.
t =(0,)
print(type(t),t)

# 원소뒤에 쉼표가 있으면 튜플이라는것을 식별 할 수 있음으로 소괄호 () 를 생략할 수 있다
y=0,
print(type(y),y)

t=1,2,3,4,
print(type(t),t)

#원소가 2개 이상의 경우에는 마지막 쉼표를 생략할 수 있다
t=1,2,3,4
print(type(t),t)

t = (1,2,3,4,5)
a = t[0]
b = t[1]
c = t[2]
d = t[3]
e = t[4]
print(a,b,c,d,e)

#위에 조잡하다. 언패킹 unpacking 기능 활용, 리스트도 가능합니다
a,b,c,d,e = t
print(a,b,c,d,e)

# unpacking 을 할 때 주의할 점은 변수의 갯수와 원소의 갯수가 일치해야 하며 일치하지 않으면 오류가 발생합니다

# 언패킹 unpacking 기능 활용
# a = 10
# b = 20
# c = 30
# d = 40
# e = 50

# 파이썬에서는 다수의 변수에 값들을 한 번에 대입할 수 있습니다.
a,b,c,d,e = 10,20,30,40,50  # 튜플의 언패킹

print(a)
print(b)
print(c)
print(d)
print(e)


#11. 자료형 딕셔너리
# 딕셔너리(dict) : 주로 검색을 위해 사용되는 자료구조 , 영한 사전
# 중복을 허용하지 않고 추가된 순서도 유지되지 않음

#영한사전 : apple -> 사과
#          표제어     뜻

#딕셔너리 :  키      벨류
#딕셔너리는 키-벨류 원소로 하는 자료 구조


#[] : 리스트
#() : 튜플
# {} :딕셔너리
# 비어있는 딕셔너리 생성
d = {}
print(type(d),d)

# 초깃값을 사용한 생성
# 키 : 주로 문자열 사용
# 벨류 :

d = {"kor":10, "eng":20,"math":30}
print(d)

daniel = {"name":"daniel", "age":20, "is_adult":True}
print(daniel)

#검색. 국어, 영어, 수학 점수
d = {"kor":10, "eng":20,"math":30}

#키를 사용하여 인덱싱
print(d["kor"])
print(d["eng"])

# 존재하지 않는 키 사용하면 오류
print(d["art"])

#키를 활용하는 방법은 반복루프 사용
d = {"kor":10, "eng":20,"math":30}

for key in d:
  print(type(key),key,d[key])

print(d.keys())  #키만 확인
print(d.values()) #벨류만 확인
print(d.items())  #키와 벨류 모두를 확인

d = {"kor":10, "eng":20,"math":30}

# 원소 수정
d["kor"] = 90
print(d)

#존재하지 않는 키 대입 수행시 원소가 추가됩니다.
d["art"] = 100
print(d)

#원소 삭제
del d["art"]
print(d)

# 원소 추출
math = d.pop("math")
print(math, d)

# 모든 원소 삭제
d.clear()
print(d)


d = {"kor":10, "eng":20}

# 딕셔너리 안의 원소들에 대하여 한 번에 업데이트 하는 방법
d.update({"kor":100, "eng":100})
print(d)

# 딕셔너리 안의 원소들에 대하여 한 번에 업데이트 하는 방법, 존재하지않은 키의 업데이트하면 해당 원소 추가된다
d.update({"kor":100, "eng":100, "math":70})
print(d)


#12. 자료형 셋
# 셋(set): 수학에서 집합의 개념을 구현한 자료구조
# 집합의 특성으로 인해 중복을 허용하지 않고 순서도 유지되지 않음
# [] : 리스트
# () : 튜플
# {} : 딕셔너리
# 셋은 자신을 표현하는 기호가 없습니다

# 비어 있는 셋을 생성할 수 없습니다
#함수를 사용하면 비어있는 셋을 생성할수 있습니다.
s=set()
print(type(s),s)

#초깃값을 사용한 생성
s = {1,2,3,4}  #중복허용안하고 순서도 유지되지 않음(딕셔너리와 공통점), 셋이 딕셔너리를 빌려서 썼다
#딕셔너리와 차이는? 딕셔너리에서 벨류를 뺀 값이다
print(type(s),s)

print({4,1,3,2}) #추가된 순서가 유지되지 않음
print({1,1,1,1}) #중복도 허용 되지 않음

#파이썬에서 제공하는 모든 타입의 값을 저장할 수 있습니다
print({10,3.14,"hello",True})

#추가된 순서가 유지되지 않으므로 인덱싱이 불가능 합니다
s = {1,2,3,4}
print(s[0]) # ??

# 어떠한 데이터에서 중복된 값을 제거할 때 주로 사용
s = "hello, world"
print(set(s))

#셋은 집합 연산을 제공합니다.
# 1. 교집합
# 2. 합집합
# 3. 차집합

a = {1,2,3,4}
b = {3,4,5,6}

# 1. 교집합
print(a & b)

# 2. 합집합
print(a | b)

# 3. 차집합
print(a - b)



#13.리스트 컴프리헨션
#연습 문제

# 1부터 10까지의 자연수에 대하여 각 값을 제곱합 결과를 원소로 하는 리스트를 생성해 보세요
# [1,4,9,16,25,36,49,64,81,100]

l = []
for i in range(1,11):
  l.append(i**2)
print(l)  




#리스트 컴프리헨션 : 수식과 반복문을 사용해서 리스트를 초기화 하는 문법
l = [num**2 for num in range(1,11)] #num을 제곱한 요소로 리스트를 초기화 할거야
print(l)

# 1부터 10까지 자연수 중 짝수에 대하여 제곱한 결과를 원소로 하는 리스트를 생성해보세요

l = [num**2 for num in range(1,11) if (num % 2)==0] #num을 제곱한 요소로 리스트를 초기화 할거야, + 짝수 조건 추가
print(l)

l = []
for n in range(1,11):
  if (n%2)==0:
    l.append(n**2)

print(l)  



#14. 문자열 처리
 s = "apple banana cherry durian"

# s.split() # 스플릿이라는 함수안에 어떤 구분자로 문자열을 쪼갤 것인가. 단어사이에 공백이 있다. 공백을 기준으로 단어를 쪼개자

result = s.split(" ")
print(result)

s = "apple, banana, cherry, durian"
print(s.split(", "))


s = "apple, banana, cherry, durian"
print(s.split(", ", maxsplit=2))  # maxsplit =2 앞에 2개만 쪼개 준다. 뒤에는 안쪼갬

#연습문제
# 위 번호에서 국가번호를 제외한 나머지만 출력해 보세요

phone = "+82-010-1234-5678"
print(phone.split("+82-")) # 내 오답

#선생 답변
print(phone.split("-", maxsplit=1)[-1])  # ['+82', '010-1234-5678'] 두개 원소(+82, 번호)가 나와서 마지막 인덱스를 [-1] 선택해서 번호만 나왔음
print(phone.split("-", maxsplit=1))

#2. 불필요한 문자 제거
print("@@@@@@@@@@@@@@@@@@Python".lstrip("@"))  # 불필요한 문자 @가 왼쪽에 있다.  leftside strip : lstrip

print("Python@@@@@@@@@@@@@@@@@@".rstrip("@"))  # 불필요한 문자 @가 오른쪽에 있다.  rightside strip : rstrip

print("@@@@@Python@@@@@@@@@@@@@@@@@@".strip("@"))

s = "!@#$%^  %^%@#%#@%@#$@$@#$Hello, Python^$@$@#%#!#?#@$@"
print(s.strip("!@#$%^&*() "))

#3. 문자열 연결하기

s= "apple"+ ", " + "banana" + ", "+ "cherry" + ", " + "durian"
print(s)

#문자열 연결 join
l = ["apple","banana","cherry","durian"]
print(", ".join(l))
print(" ".join(l))

# 문자열: 문자열 또한 원소가 문자인 자료구조
# 따라서 각 문자에 대한 인덱스가 존재합니다
#    01234
s = "hello"
print(s[0])
print(s[-1])

#검색 1. find
#  0123456789ABCD
s="hello, python!"

print(s.find("python"))  # 처음 시작하는 문자열의 시작 인덱스를 반환한다. p : 7인덱스
print(s.find("o"))
print(s.find("java")) #일치 하는 것 없을 때

# 4. 특정 문자열로 시작하거나 끝나는 경우
fname = "hello.pdf"

print(fname.endswith("pdf"))  # pdf로 끝나는지 확인

URL = "http://192.168.0.1"
print(URL.startswith("http")) # 시작이 http 프로토콜이 맞는지 확인

# 5. 문자열 치환
s= 'Python is fast. Python is friendly. Python is open.'
print(s.replace('Python','Ipython'))
print(s.replace('Python','Ipython',2))

dan = input("구구단 입력(2~9): ")

if not dan.isdigit():   #문자열 구성 함수 isdigit() 숫자로만 이루어져있는지. 교재 참고 
  print("잘못 입력하셨습니다")
else:
  print("구구단 출력...")

# 문자열의 대소문자 변경
s= "HeLLo"

print(s.lower())
print(s.upper())



#15. 함수
# 함수 : 특정 기능이 구현되어 있는 코드 덩어리
#함수의 정의 : 함수를 만든다는의미
# def 함수명(변수,...):  <- 콜론으로 끝나야 합니다
# ...함수 코드 
# ...함수 코드 
# 함수명은 아무거나 해도 되지만 관례적으로 동사로 시작한다 

# 사용자로 부터 횟수를 입력 받아 횟수 만큼 화면에 hello를 출력하는 함수를 구현
def print_hello(count):   #함수 정의시, 괄호 안에 변수 매개변수(파라미터)라고 합니다.
  for _ in range(count):   <--for 다음 언더바
    print("hello")

# 함수 호출 : 함수를 사용한다는 의미
# 함수 호출 방법 : 함수명(값,...)
#                      ^--- (소괄호) 함수 호출 연산자

print_hello(3) #함수  호출 시, 괄호 안에 값을 인자(argument)라고 합니다.

#연습 문제
#구구단의 단을 함수의 인자로 전달하여 특정 단을 출력하는 함수를 구현해보세요. 입력값은 2~9사이값만 전달된다고 가정
#그리고 함수 이름은 display_dan으로 합니다
# display_dan(2)
#<2단>
# 2 x 1 = 2

def display_dan(count):   #함수 정의시, 괄호 안에 변수 매개변수(파라미터)라고 합니다.
  for i in display_dan(count):
    print(f"<{count}단>")

#선생 답변
def display_dan(dan):
  print(f"<{dan}단>")

  for num in range(1,10):
    print(f"{dan}")

# 강사 답변
# 연습 문제 1. 구구단의 단을 함수의 인자로 전달하여 특정 단을 출력하는 함수를 구현해 보세요.
# 이 때, 입력된 값은 2~9사이의 값만 전달된다고 가정합니다.
# 그리고 함수의 이름은 display_dan으로 합니다.

# display_dan(2)

# < 2단 >
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 9 = 18


def display_dan(dan):
  print(f"< {dan}단 >")

  for num in range(1,10):
    print(f"{dan} x {num} = {dan*num}")


display_dan(2)

#함수의 반환
def add(a, b):
  return a + b # usage : return 값

result = add(1,1)  #함수 내에서 return키워드 사용하면 함수가 호출된 자리에는 그 값으로 치환 됩니다.
                   # --> result = 1+1 = 2
print(result)  


a = 5
b = 3
q =a//b  #몫
r= a%b # 나머지
print(q,r)

#몫과 나머지 한번에 계산할수 있는 함수 제공
q,r = divmod(5,3)
print(q,r)

def mydivmod(a,b):
  return a//b, a%b #다수의 값을 반환하려면 쉼표로 구분 해주시면 됩니다, 
                   #쉼표를 통해 두개의 값을 반환해준 것이다(튜플)

q,r = mydivmod(5,3)  #결국 이건 튜플이다. 쉼표를 통해 두개의 값을 반환해준 것이다
print(q,r)

#참고, return 키워드는 값을 반환하는 용도 뿐만 아니라 함수를 즉시 종료할 때도 사용됩니다.

def print_age(age):
  if age < 0:
    print("잘못 입력하셨습니다.")
    return # 위 코드만 진행하고 리턴으로 함수 빠져나감
  print(f"당신의 나이는 {age}세 입니다")

  #break는 반복문 중단, 리턴은 함수를 즉시 종료하는 키워드인데 값을 반환하면서 종료합니다.
print_age(15)
print_age(-1) # 사용자의 부주의로 잘못 입력된 값  

#스코프(scope) : 어떤 이름(함수나 변수의 이름)을 참조할 수 있는 영역
# 변수의 위치가 함수 외부 : 전역, 함수 내부 : 지역
#1. 전역스코프 : 함수나 클래스 외부 영역
# -> 코드 어디에서나 참조 가능한 영역

g = "global" # 전역 변수 : 전역 스코프에서 생성된 변수 (함수 안에 들어있지 않다)

def foo():
  # 2.지역 스코프 : 함수 내부 영역 (함수 안에 들어있다)
  #-> 함수 내부에서만 참조 가능한 영역
  l = "local" # 지역 변수 : 지역 스코프에서 생성된 변수


# 스코핑 룰 : 어떤 이름을 찾는 순서   지역 - 전역 - 파이썬 내부(Built-in) : LGB Rule

x="global"
def goo():
  print(x) # x는 함수내부에 존재하지 않는다. -> 전역변수에 있는 변수이구나하고 밖에서 찾음. 
           # print라는 이름은 함수내부에 없다. print는 뭐지? -> 전역 스코프에도 print라는 이름이 없다. -> 원래는 오류가 뜰테지만,
           # 지역에도 없고, 전역에도 없으면 파이썬 내부에서 찾는다. 파이썬 내부에 print라는 함수가 있다 -> print 함수 실행   

goo()

x ="global"

def bar():
  x = "local"   # x를 만들고 있음, 지역변수를 생성하는 코드
  print(x) # 이 x는 로컬로 인식한다. 밖에 있는 전역 변수와는 다른 변수다.

bar()
print(x) # 로컬이 안되고 글로벌이 나온다.    

x ="global"

def bar():
  global x # 지역 변수 x를 전역변수 x로해석해 달라는 의미
  x = "local"   # x를 만들고 있음, 지역변수를 생성하는 코드
  print(x) # 이 x는 로컬로 인식한다. 밖에 있는 전역 변수와는 다른 변수다.

bar()
print(x) # 로컬이 안되고 글로벌이 나온다.    

#반복문을 계속 쓰지 않기 위해서 함수로 사용

def display_menu():
print("#게임 메뉴")
print("#1. 시작하기")
print("#2. 시작하기")
print("#3. 시작하기")
print("#4. 시작하기")

display_menu()
display_menu()

# 람다 함수 : 람다 표현식이라고 표현하는게 더 적합해보이는 함수
# 람다 함수 : 이름이 없는 함수
#            1) 무조건 한 줄로 작성
#            2) 반드시 값을 반환

# 람다 함수 정의 방법
# lambda 매개변수, ...: 반환값   
#                         ^--- 주의! return 키워드를 사용할 필요가 없으며 사용하셔도 안된다 

# 일반 함수 정의
def square(x):
  return x**2

#람다 함수의 정의
lambda x: x**2   #이름이 없다  

# 일반 함수와 람다 함수 호출하기
def square(x):
  return x**2

result = square(2)
print(result)


lambda x: x**2   
#람다함수 호출하려면 함수만들면서 써야한다 (즉시호출)
result = lambda x: x**2(4)  #2라는 정수에 (4)를 붙인 것이다. 함수가 아니라서 호출 할 수 없다고 뜬다, 에러


#2라는 정수에 (4)를 붙인 것이다. 함수가 아니라서 호출 할 수 없다고 뜬다
# 람다함수에 소괄호를 씌운다
lambda x: x**2   
#람다함수 호출하려면 함수만들면서 써야한다 (즉시호출), 잘 사용하지는 않음. 일반함수와 비교해서 개념만 알면 될 듯
result = (lambda x: x**2)(4)  
print(result)

#일반함수 : 이름이 있다. 프로그램이 종료될 때까지 존재함
#람다함수 : 이름이 없다. 문장의 끝을 만나면 파괴됨

# 만약 람다 함수의 수명을 늘리려면 변수에 대입하면 됩니다
sqr = lambda x: x**2
print(sqr(2))

#람다의 존재의미를 알아보자. 
#수학점수, 30점이하 과락
maths = [10,20,30,40,50,60]

for math in maths:
  if (math<=30):
    print(math, "failed")

# filter(): 자료구조의 원소들 중 조건이 참인 원소만 걸러내는 함수

maths = [10,20,30,40,50,60]

#filter는 매개 변수가 1개인 함수를 받는데 반드시 그 값은 참 또는 거짓이어야 합니다
def bypass(item):
  return True
for math in filter(bypass, maths):  #여과기로 통과 시킴. 이렇게 하면 다 통과시키니 아래와같이 걸러 낼 수 있게 하자.
  print(math, "failed")


print(" ") # 위 아래 코드 차이알기 위해서 "개행 띄우기"

def is_faled(item):
  return item <=30

for math in filter(is_faled, maths):  #여과기로 걸러낸다.
  print(math, "failed")

# 코드가 복잡하다

# 코드가 복잡하다 --> 람다의 목적, 의미가 여기서
#잠깐 쓰고 버릴 함수를 람다로 대체하면 코드가 간결해진다

maths = [10,20,30,40,50,60]
for math in filter(lambda x: x <=30,maths): # def filter(a, b)  
  print(math, "failed")

import numpy as np # 고속연산에서는 numpy사용, 빠르게 동작

result = (lambda : 3.141592)()
print(result)

#매개 변수 두개 사용
result = (lambda a, b : a+b)(1,1)
print(result)

# 내장 함수 : 파이썬이 제공하는 함수
# print, input, int, float, str, bool, type, len, set, ...




#16. 파일 입출력
# 파일을 읽거나 쓰려면 먼저 파일을 열어야  (교안 119페이지)
# 화면 좌측에 폴더 모양의 "파일" 을 클릭해서 여세요
# usage : open(파일위치, 모드)

# 모드
# 파일을 텍스트 파일로 열 것인지, 2진 데이터로 열 것인지 결정해주어야 한다.
# t : text의 약자로 해당 파일을 텍스트 파일로 열겠다는 의미 -> 텍스트 파일 열 때
# b : binary의 약자로 해당 파일을 있는 그대로 열겠다는 의미 -> 이외의 파일을 열 때 (이미지, 동영상 등,,,) -> 초급 과정에서는 다루지 않는다

# r : read의 약자로 파일을 읽기 모드로 열겠다는 의미
# w : write의 약자로 파일을 쓰기 모드로 열겠다는 의미

# "tr", "tw" -> 문자 순서는 상관 없습니다. tr = rt :text read

# 파일을 열 때, 텍스트 모드가 기본이므로 이를 생략할 수 있습니다. 텍스트가 많기 때문에
# "r", "w"  --> 텍스트 파일 읽기, 쓰기 모드

# 또한, 읽기 모드가 기본이므로 이를 생략할 수 있습니다. tr일 경우 아무것도 안써도 된다.




# 파일을 열기
# f = open("hello.txt","tr") #tr text read로 열어달라. --. t생략 가능, r 생략 가능
f = open("hello.txt")

#파일 사용
# 파일 사용 후 닫지 않으면 다른 사람이 사용할 수가 없다. 파일 사용 후 반드시 닫아주어야 함.
f.close()

# 파일 읽기 1.read : 파일의 모든 내용을 읽어와서 문자열로 저장 후, 반환합니다.
# 파일이 너무 크면 문제가 된다
f = open("hello.txt") # "tr"
contensts= f.read()
f.close()

print(contensts)


# 파일 읽기 2. redadline : 라인 단위로 파일을 읽어와서 문자열로 저장 후, 반환 합니다.
# 라인이 몇개인지 모르겠는데 ,얼마나 수행을 해야하나?
# 얼마인지는 모르겠으나 일단은 무한반복으로 읽어보자

f = open("fruits.txt")

while True:
  line = f.readline()
  if line =="": # 더이상 읽을 행이 없는 경우, 빈 문자열이 반환됩니다
    break

  print(line)

f.close()
#fruits 파일에 apple치고 enter치면서 개행 문자가 포함된다. 빈줄이 포함되어 있다.
#개행이 필요없으면  print(line, end="") 이렇게 치면 된다



f = open("fruits.txt")

for line in f:
  print(line, end="")
f.close()  

#파일 읽기 3. readlines : 라인 단위로 한 번에 읽어와 리스트로 반환합니다
f = open("fruits.txt")

lines = f.readlines()
f.close() 

print(lines)

#파일 쓰기

# f = open("test.txt","tw")
f = open("test,txt","w") # 파일을 쓰기 모드로 열 때, 해당 파일이 존재하지 않으면
                         # 생성해 줍니다

for num in range(1,10):
  f.write(f"2 x {num} = {2*num}\n")
#                               ^---  행 단위로 출력하려면 개행을 사용해야 합니다.
f.close()


# 파일 쓰기를 수행할 때, 주의할 점!!!
# 쓰기의 모드의 특징은 기존 파일이 존재할 경우 해당 파일을 덮어써버린다. 복구 불가
# 덮어쓴 파일은 복구하기 어렵다.
f = open("fruits.txt","w")

for num in range(1,10):
  f.write(f"2 x {num} = {2*num}\n")
                             
f.close()

#모드
# a: append 의 약자로 기존 파일이 존재하면 파일의 끝에 추가합니다 "ta"
# x: exclusive의 약자로 기존 파일이 존재하면 오류가 발생합니다. "tx"
# 그래서 "tw"로 열지말고 "tx"로 여는게 좋다

f = open("hello.txt") # "tr"
contensts= f.read()
f.close()

print(contensts)

# 위 코드에서 실수로 파일을 닫아주지 않는다면? f.close()
# with 블럭 사용

with open("hello.txt") as f:
  print(f.read())

# with 블럭을 벗어나는 순간 파이썬이 close함수를 자동으로 호출해줍니다. 
# 이렇게 사용하면 알아서 닫아준다. close



#17. 모듈과 패키지
# 모듈(module) :변수나 함수 또는 클래스들을 모아 놓은 단순 파이썬 파일

# 모듈 사용 이유
# 1. 코드의 중복 제거
# 2. 유지 보수가 용이
# 3. 논리적 오류(버그)가 감소
# 4. 파일 단위로 작업하므로 공동으로 개발 가능
# ...

# math.py -> 파이썬이 제공하는 수학 모듈

# 1. 모듈 불러오기

# usage: import 모듈명  <- 확장자는 기술하지 않습니다
# import math.py

# 파이썬 공식 사이트 가서 - Documentation -Python 3 Resource - Library -math 모듈 정보 볼 수 있다.
import math

# print(pi)
# 모듈 안의 요소를 사용하려면 반드시 모듈명과 함꼐 사용해야 합니다.

print(math.pi)
print(math.factorial(5))

from os import fchmod
# 모듈 안의 요소를 직접 불러올 수 있습니다
# usage : from 모듈명 import 변수명
# usage : from 모듈명 import 함수명
# usage : from 모듈명 import 클래스명

from math import pi
from math import factorial
print(pi)
print(factorial(5))

# 여러개면 일일이 여러줄을 쳐야하는데 쉼표 쓰면 간단하게 처리할 수 있습니다
# usage : from 모듈명 import 변수명, 함수명, 클래스명 ,...

from math import pi, factorial
print(pi)
print(factorial(5))

#모듈 안의 요소를 한 번에 불러올 수 있습니다.

from math import *

print(pi)
print(factorial(5))
print(e)

from math import factorial
print(factorial(5))

#모듈명 뿐만 아니라 요소에도 별칭을 부여할 수 있습니다
# 사용법
# usage : from 모듈명 import 변수명 as 별칭
# usage : from 모듈명 import 함수명 as 별칭
# usage : from 모듈명 import 클래스명 as 별칭


from math import factorial as fact # 모듈명은 요소에도 별칭을 부여할 수 있다
print(factorial(5))

# 불러온 모듈을 내릴 수 있습니다.
import math # 파이썬 메모리안에 내용을 지운다는 것이지 해당 모듈(math.py)를 삭제 하는 것은 아니다
del math

print(pi)

del math

#모듈안에 요소들 이름 확인 하는 방법

import math
dir(math)



#18. 객체와 클래스
# everything is object!

print(10)
print("hello".upper())

# 학생의 점수를 관리하는 학사 관리 프로그램을 생각해 봅니다.
name = "daniel"
kor = 10
eng = 20
math = 30

tot = kor + eng + math
avg = tot / 3

print(name, tot, avg)

# 여기서 한 명의 학생이 더 추가되었다고 가정합니다.
name = "daniel"
kor = 10
eng = 20
math = 30
tot = kor + eng + math
avg = tot / 3
print(name, tot, avg)

name = "susan"
kor = 20
eng = 30
math = 40
tot = kor + eng + math
avg = tot / 3
print(name, tot, avg)

# 이전의 코드는 치명적인 문제가 있는데 기존 학생의 정보가 손실된다는 것입니다.
# 이를 해결하기 위해 변수를 재사용하는 것이 아니라 새로운 변수를 사용하도록 합니다.
name1 = "daniel"
kor1 = 10
eng1 = 20
math1 = 30
tot1 = kor1 + eng1 + math1
avg1 = tot1 / 3
print(name1, tot1, avg1)

name2 = "susan"
kor2 = 20
eng2 = 30
math2 = 40
tot2 = kor2 + eng2 + math2 # ...
avg2 = tot2 / 3
print(name2, tot2, avg2)

# 이전의 코드는 총점과 평균을 계산하는 코드가 반복(중복)되고 있다는 단점이 있습니다.
# 그리고 수식이 그대로 노출되어 있어 코드의 가독성도 떨어지게 됩니다.
# 이러한 문제를 해결하기 위해 함수를 도입합니다.

def total(a, b, c):
  return a + b + c

def average(tot, cnt):
  return tot / cnt

name1 = "daniel"
kor1 = 10
eng1 = 20
math1 = 30
tot1 = total(kor1, eng1, math1) # kor1 + eng1 + math1
avg1 = average(tot1, 3) # tot1 / 3
print(name1, tot1, avg1)

name2 = "susan"
kor2 = 20
eng2 = 30
math2 = 40
tot2 = total(kor1, eng2, math2) # ??
avg2 = average(tot2, 3)
print(name2, tot2, avg2)

# 이전의 코드는 학생 데이터가 서로 개별적으로 취급되어 데이터가 혼용될 수 있다는
# 치명적인 문제가 있습니다. 이를 해결하기 위해 밀접하게 관련된 데이터를 하나로 묶어서
# 처리합니다.

def total(st):
  return st["kor"] + st["eng"] + st["math"]

def average(st):
  return (st["kor"] + st["eng"] + st["math"]) / st["cnt"]

daniel = {"name":"daniel", "kor":10, "eng":20, "math":30, "cnt":3}
tot1 = total(daniel)
avg1 = average(daniel)
print(daniel["name"], tot1, avg1)

susan = {"name":"susan", "kor":20, "eng":30, "math":40, "cnt":3}
tot2 = total(susan)
avg2 = average(daniel) # ??
print(susan["name"], tot2, avg2)

# 이전의 코드는 학생 데이터와 그리고 데이터를 처리하는 함수가 이원화되어 있어
# 계산이 올바르게 되지 않을 수 있다는 치명적인 문제가 있습니다.
# 이를 해결 하기 위해 데이터와 이를 처리하는 함수를 하나로 묶도록 합니다.

def total(st):
  # 객체로부터 데이터를 참조하는 방법: 객체명.변수명
  return st.kor + st.eng + st.math

def average(st):
  return (st.kor + st.eng + st.math) / st.cnt

# 파이썬에서는 데이터와 이를 처리하는 함수를 하나로 묶을 수 있도록 
# 클래스라는 문법을 제공합니다.

# 클래스를 정의하는 방법
# class 클래스명:
# ....관련코드
# ....관련코드

class Student: # 클래스명은 함수 또는 변수와 구분하기 위해 관례적으로 대문자로 시작합니다.
  pass # 그냥 지나가달라는 의미

# 클래스와 객체의 관계
# 클래스                 객체
# 상자를 만드는 기계       상자

# 클래스로부터 객체를 생성 방법
# 객체를저장하는변수명 = 클래스명()
daniel = Student()

# 객체에 데이터를 추가하는 방법
# 객체명.변수명 = 값
daniel.name = "daniel"
daniel.kor = 10
daniel.eng = 20
daniel.math = 30
daniel.cnt = 3
tot1 = total(daniel)
avg1 = average(daniel)
print(daniel.name, tot1, avg1)

susan = Student()
susan.name = "susan"
susan.kor = 20
susan.eng = 30
susan.math = 40
susan.cnt = 3
tot2 = total(susan)
avg2 = average(susan)
print(susan.name, tot2, avg2)

class Student:
  # 클래스 안의 정의된 함수들은 반드시 첫 번째 매개변수를 예약석으로 남겨두어야 합니다.
  # 이는 객체 안의 함수가 호출될 때, 파이썬이 그 함수의 첫 번째 인자로 객체의 정보를 전달하기 때문입니다.
  # 파이썬에서는 이와 같이 함수가 호출될 때, 객체의 정보와 함께 호출되는 함수를 기존 함수와 구분하기 위해
  # (인스턴스)메서드라고 부릅니다.
  # 파이썬에서는 객체를 저장하는 변수를 기존 다른 매개변수와 구분하기 위해 관례적으로
  # self라는 변수명을 사용합니다.
  def total(self):
    return self.kor + self.eng + self.math

  def average(self):
    return (self.kor + self.eng + self.math) / self.cnt 

daniel = Student()
daniel.name = "daniel"
daniel.kor = 10
daniel.eng = 20
daniel.math = 30
daniel.cnt = 3

# 객체 안의 함수를 호출하는 방법: 객체명.함수명()
tot1 = daniel.total()   # total(daniel)
avg1 = daniel.average() # average(daniel)
print(daniel.name, tot1, avg1)

susan = Student()
susan.name = "susan"
susan.kor = 20
susan.eng = 30
susan.math = 40
susan.cnt = 3
tot2 = susan.total()
avg2 = susan.average()
print(susan.name, tot2, avg2)

# 이전의 코드는 과목명이 이미 내부적으로 결정되어 있어 과목명을 모르면
# 학생 클래스를 사용할 수 없다는 치명적인 문제가 있습니다.
# 이를 해결하기 위해 객체의 상태를 초기화하는 메서드를 추가합니다.

class Student:
  def total(self):
    return self.kor + self.eng + self.math

  def average(self):
    return (self.kor + self.eng + self.math) / self.cnt 

  def initialize(self, name, kor, eng, math):
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.cnt = 3

daniel = Student()
daniel.initialize("daniel", 10, 20, 30) # initialize(daniel, "daniel", 10, 20, 30, 3)
tot1 = daniel.total()
avg1 = daniel.average()
print(daniel.name, tot1, avg1)

susan = Student()
susan.initialize("susan", 20, 30, 40)
tot2 = susan.total()
avg2 = susan.average()
print(susan.name, tot2, avg2)

# 이전의 코드는 객체를 생성한 후에 초기화 메서드를 호출하지 않으면 객체를 사용할 수 없다는
# 치명적인 문제가 있습니다.
# 이를 해결하기 위해서 초기화 메서드를 자동으로 호출하는 문법을 도입합니다.

# 파이썬에서는 객체가 생성될 때, 자동으로 호출되는 메서드를 제공하는데 이를
# 생성자(constructor)라고 합니다. 파이썬에서 생성자의 이름은 __init__입니다.
class Student:
  def total(self):
    return self.kor + self.eng + self.math

  def average(self):
    return (self.kor + self.eng + self.math) / self.cnt 

  def __init__(self, name, kor, eng, math):
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.cnt = 3

daniel = Student("daniel", 10, 20, 30)
tot1 = daniel.total()
avg1 = daniel.average()
print(daniel.name, tot1, avg1)

susan = Student("susan", 20, 30, 40)
tot2 = susan.total()
avg2 = susan.average()
print(susan.name, tot2, avg2)

class Test:
  def __init__(self, a, b, c):
    print("Test.__init__(%d, %d, %d)" % (a,b,c))

test = Test(10,20,30)

# object -> 사물, 물건 -> 객체

# 사물이나 물건은 2가지 속성으로 추상화 할 수 있습니다.
# 1. 상태, 속성
# 2. 기능, 행위

# ex) 볼펜
# 1. 상태나 속성: 검정색, 모나미, 0.7mm => 변수
# 2. 기능이나 행위: 쓰다, 그리다        => 함수


      

