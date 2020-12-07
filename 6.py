
car = ['제네시스','아반테','쏘나타']

print("======================자동차 모터쇼!=======================")

Audience = input("자동차 모터쇼 몇명 또는 입장권 몇장갖고오셨습니까?")

for motor_show in range(int(Audience)):
    print(Audience+"명접수됬습니다. 입장권드리겠습니다.!")
    break
for i in car :
    print("자동차 모토쇼 리스트 알려드리겠습니다.!")
    print('.'.join(car)) # join 함수 리스트 출력가능하게 해주고 , 리스트 특정 구분자를 포함해서 문자열 변환해주는 함수
    break







