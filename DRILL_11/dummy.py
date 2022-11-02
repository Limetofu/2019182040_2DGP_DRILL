# class Star:
#     type = "star"
#     x = 100

#     def change():
#         x = 200
#         print('x is', x)

# print('x is', Star.x)
# Star.change()

# star = Star() # 굳이 객체를 생성하는 것도 가능?
# print('x is', star.x) # 객체 변수로 액세스하지만, 뭘로 귀착? 클래스 변수 x를 가리킨다.
# # star.change()

class Player:
    name = 'Player'

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

player = Player()
player.where()

print(Player.name) # 클래스 변수 추력
print(player.name) # name이라는 객체 변수가 없으면, 같은 이름의 클래스 변수가 선택

Player.where(player) # 이게 원칙적인 파이썬에서의 멤버 함수 호출
player.where()       # ==> Player.where(player) 과 동일

