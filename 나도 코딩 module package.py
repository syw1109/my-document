
# ### 5. 모듈

# #theater module 이라는 .py 모듈 파일을 만들었다

# import theater_module
# from travel import thailand
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(2)


# import theater_module as mv  #별명으로 씀

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(2)

# from theater_module import *   # 모듈에 있는 모든것을 쓰겠다
# price(3)
# price_morning(4)
# price_soldier(2)


# from theater_module import price, price_morning
# price(5)
# price_morning(6)

# from theater_module import price_soldier as price
# price(5)  # = price_soldier


# #### 6. 패키지 모듈의 모음
# import travel.thailand   #thailand 모듈이나 패키지만 import 가능. class, 함수는 바로 못함
# trip_to = travel.thailand.ThailandPackage()  # ThailandPackage 는 class
# trip_to.detail()

# from travel.thailand import ThailandPackage  # 이렇게 from [thailand] 패키지 import [ThailandPackage] Class 
# trip_to = ThailandPackage() 
# trip_to.detail() 

# from travel import vietnam
# trip_to = vietnam.vietnamPackage
# trip_to.detail() 


class Thailandpackage:
    def detail(self):
        print("태국 5박6일 패키지")
    __name__:str    
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이문장은 모듈을 직접 실행할 떄만 실행돼요")
    trip_to = Thailandpackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
    
    
    
    
#### 8. pip로 패키지를 설치할수 있다
# 구글에 pypi 검색시 패키지 검색 가능
beautifulsoup : 웹스크래핑에 많이 사용됨

### 9. 내장 함수
# 구글에 list of python builtins 검색
# 내장 함수 확인 가능


### 10. 외장 함수   임포트 해서 사용
# list of python modules 검색