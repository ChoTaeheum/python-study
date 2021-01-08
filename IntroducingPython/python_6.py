# CHAPTER 6 클래스
# 객체는 데이터와 코드를 모두 포함한다.
# 객체는 어떤 구체적인 것의 유일한 인스턴스를 나타낸다.
# 예를 들어 값7의 정수객체는 계산을 가능하게 해주고 값8은 또 다른 객체이다.
# 'cat', 'duck' 또한 객체이고 이 객체는 capitalize()나 replace()같은 문자열 메서드를 가지고 있다.
# 쉽게 생각하면 문자열을 문자클래스에 인자값으로 받고 그 안에 있는 메서드를 사용한다고 볼 수있다.
# 아무도 생성하지 않은 새로운 객체를 생성할 때는 무엇을 포함하고 있는지 카리키는 클래스를 생성해야한다.
# 객체는 각각의 사물을 나타내고 메서드는 다른 사물과 어떻게 상호작용하는지 정의한다.
# 객체는 박스, 클래스는 박스를 만드는 틀에 비유할 수 있다.
# 예를 들어 String은 'cat' 같은 객체를 만들수 있는 내장 클래스이다. 그 밖에서 리스트, 튜플을 만드는 여러 클래스가내장되어있음
class Person():
    pass
someone = Person()

# Person()은 Person 클래스로부터 개별객체를 생성하고 someone 변수에 이 객체를 할당한다.
class Person():
    def __init__(self):
        pass
# __init__()는 클래스의 정의로부터 객체를 초기화한다.
# self인자는 객체 자신을 가리킨다. 예약어는 아니다.
class Person():
    def __init__(self, name):
        self.name = name   # name 매개변수를 초기화하는 메서드 추가
hunter = Person('Elmer Fudd')
# Person 클래스의 정의를 찾는다.
# 새 객체를 메모리에 초기화(생성)한다.
# 객체의 __init__() 메서드를 호출한다. 새롭게 생성된 객체를 self에 전달하고, 인자('Elmer Fudd')를 name에 전달한다.
# __더블 언더스코어보고 던더(dunder)라고 부른다.
# 객체에 name값을 저장한다.
# 새로운 객체를 반환한다.
# hunter에 이 객체를 연결한다.
print(hunter.name)   # Person()을 객체화한 hunter 객체의 self.name을 의미한다.
# 모든 클래스 정의에서 __init__()메서드르르 가질 필요는 없다.

# 상속
# 기존 클래스를 수정하려 하면 클래스를 더 복잡하게 만들게 될 것이고, 코드를 잘못 건드려 수행할 수 없게 만들 수도 있다.
# 그리고 같은 기능을 담당하는 기존 클래스와 새로운 클래스가 서로 다른 곳에 있기 때문에 혼란스러워진다.
# 이 문제는 상속으로 해결 가능!, 코드를 재사용하는 방법
# 우선 필요한 것만 추가/변경하여 새 클래스를 생성한다. 이것은 기존 클래스의 행동을 오버라이드(재정의)한다.
# 기존 클래스는 부모, 슈퍼, 베이스 클래스라고 한다.
# 새 클래스는 자식, 서브, 디라이브드(파생된) 클래스라고 한다.
class Car():
    pass
class Yugo(Car):
    pass
give_me_a_car = Car()
give_me_a_yugo = Yugo()
# 자식 클래스는 부모클래스를 구페화한 것이다. 객체지향 용어로 Yugo는 Car다.
# give_me_a_yugo객체는 Yugo클래스의 인스턴스이지만, 또한 Car 클래스가 할 수 있는 어떤 것을 상속받는다.
class Car():
    def exclaim(self):
        print("I'm a Car")
class Yugo(Car):
    pass
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
# 특별히 아무것도 하지 않고 Yugo는 Car로부터 exclain()메서드를 상속받았다.

# 메서드 오버라이드
# 부모 클래스가 어떻게 대체 혹은 오버라이드 하는지 알아보자!
class Car():
    def exclaim(self):
        print("I'm a car")
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")

give_me_a_car = Car()
give_me_a_Yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
# Car클래스를 상속했지만 같은 이름의 메서드를 만들면서 덮어쓰기 했다.
# exclaim 메서드를 오버라이드했다.

class Person():
    def __init__(self, name):
        self.name = name
class MDPerson(Person):
    def __init__(self, name):
        self.name = 'Doctor' + name
class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)
# 부모클래스와 같은 인자를 취하지만 객체의 인스턴스 내부에서는 다른 name값을 저장한다.

# 메서드 추가하기
# 자식 클래스는 또한 부모클래스에 없는 메서드를 추가할 수 있다.
class Car():
    def exclaim(self):
        print("I'm a Car!")
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")
    def need_a_push(self):
        print("A little help here?")
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_yugo.need_a_push()
give_me_a_car.need_a_push()   # 에러발생
# Yugo는 Car가 하지 못하는 뭔가를 할 수 있으며, Yugo의 독특한 개성을 나타낼 수 있다.

# 부모에게 도움받기
# 자식클래스에서 부모클래스의 메서드를 호출하고 싶다면 이 방법을 사용할 수 있다.
class Person():    # 부모클래스
    def __init__(self, name):
        self.name = name
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
# 자식클래스의 __init__()메서드를 정의하면 부모클래스의 __init__()메서드를 대체하는 것이라서 호출하지 않는다.
# __init__() 메서드는 Person.__init__() 메서드를 호출한다. 이 메서드는 self 인자를 슈퍼클래스로 전달하는 역할을 한다.
# 그러므로 수퍼클래스에 어떤 선택적 인자를 제공하기만 하면 된다. 이 경우 Person()에서 받는 인자는 name이다.
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
bob.name    # 'Bob Frapples'      # 부모 메서드의 코드를 가져와서 사용하고 있다.
bob.email   # 'bob@frapples.com'  # 자기 자신의 코드 사용

class EmailPerson(Person):
    def __init__(self, name, email):
        self.name = name
        self.email = email
# 이 코드와 같지만 불편한 사항이 많다.

# 자신: self
car = Car()
car.exclaim()
# I'm a Car!
# car객체의 Car클래스를 찾는다.
# car객체를 Car클래스의 exclaim() 메서드의 self 매개변수에 전달한다.
Car.exclaim(car)   # 똑같이 작동, 객체를 메서드에 전달하는 것이다.

# get/set 속성값과 프로퍼티
# 프로그래머는 private속성의 값을 읽고 쓰기 위해 getter메서드와 setter메서드를 사용한다.
# 파이썬에서는 getter나 setter메서드가 필요없다. 왜냐하면 모든 속성과 메서드는 public이고 우리가 예상한대로 쉽게 동작한다.
# setter은 외부로부터 인자를 받아서 클래스에 setting해주는 메서드
# getter는 클래스 내부의 변수를 클래스 외부로 반환해주는 메서드

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

fowl = Duck('Howard')
fowl.name             # 매개변수가 없으면 자동으로 getter 실행
fowl.get_name()
fowl.name = 'Daffy'   # 매개변수가 있으면 자동으로 setter 실행
fowl.name
fowl.set_name('Daffy')
fowl.name

# 프로퍼티를 정의하는 또 다른 방법은 데커레이터를 사용하는 것이다. 다음 예제는 두 개의 다른 메서드르르 정의한다.
# 각 메서드는 name()이지만, 서로 다른 데커레이터를 사용한다.
class Dunk():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
fowl = Dunk('Howard')
fowl.name
fowl.name = 'Donald'
fowl.name
# 여전히 name을 속성처럼 접근할 수 있다. 하지만 get_name()과 set_name()은 보이지 않는다.

# 또한 프로퍼티는 계산된 값을 참조할 수 있다.
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2*self.radius
c = Circle(5)
c.radius
c.diameter
c.radius = 7
c.diameter

# 속성에 대한 setter 프로퍼티를 명시하지 않는다면 외부로부터 이 속성을 설정할 수 없다
# 이것은 읽기전용 속성이다.
c.diameter = 20   # 에러발생
# AibuteError: can't set attribute


# private 네임 맹글링
# 파이썬은 클래스 정의 외부에서 볼 수 없도록 하는 속성에 대한 네이밍 컨센션이 있다.
# 속성 앞에 두 언더스코어(__)를 붙이면 된다.
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

fowl = Duck('Howard')
fowl.name
fowl.name = 'Donald'
fowl.name
# 아무 문제가 없다. 그러나 __name 속성을 바로 접근할 수 없다.
fowl.__name
# AttributeError: 'Duck' object has no attribute '__name'
# 이 네이밍 컨벤션은 속성을 private로 만들지는 않지만 파이썬은 이 속성이 우연히
# 외부코드에서 발견할 수 없도록 이름을 맹글링mangling 해놓았다.
fowl._Duck__name
# 'inside the setter'를 출력하지 않았다. 비록 이것이 속성을 완벽하게 보호할 수는 없지만,
# 네임 맹글링은 속성의 의도적인 직접 접근을 어렵게 만든다.

# 메서드 타입
# 어떤 데이터(속성)와 함수(메서드)는 클래스 자신의 일부이고, 어떤 것은 클래스로부터 생성된 객체의 일부이다.
# 클래스 정의에서 메서드의 첫번째 인자가 self라면 이 메서드는 인스턴스 메서드이다.
# 이것은 일반적인 클래스를 생성할 때의 메서드 타입이다.
# 인스턴스 매서드의 첫번때 매개변수는 self이고, 파이썬은 이 메서드를 호출할 때 객체를 전달한다.
# 이와 반대로 클래스 메서드는 클래스 전체에 영향을 미친다. 클래스에 대한 어떤 변화는 모든 객체에 영향을 미친다.
# 클래스 정의에서 함수에 @classmethod 데커레이터가 있다면 이 것은 클래스 메서드이다.
# 또한 이 메서드의 첫번째 매개변수는 클래스 자신이다. 파이썬에서는 보통 이 클래스의 매개변수를 cls로 쓴다.
class A():
    cnt = 0
    def __init__(self):
        A.cnt += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.cnt, "little objects.")   # cls는 A()클래스를 말한다. A.cnt도 사용가능

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()
# 객체화를 하면서 클래스변수인 A.cnt가 변화하였고 변화된 사항은 클래스메서드를 통해 실행된다.
# 즉 클래스 메서드는 클래스 외부에서 공유가능하다는 뜻이다.

# 정적메서드
# 정적메서드는 @staticmethod 데커레이터가 붙어있고 첫번째 매개변수로 self나 cls가 없다.
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')
CoyoteWeapon.commercial()
# 이 메서드에 접근하기 위해 CoyoteWeapon클래스에서 객체를 생성할 필요가 없다.

# 덕타이핑
# 파이썬은 다형성을 느슨하게 구현했다. 이것은 클래스에 상관없이 같은 동작을 다른 객체에 적용할 수 있다는 것을 의미한다.
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclaimationQuote(Quote):
    def says(self):
        return self.words + '!'
# QuestionQuote(), ExclaimationQuote() 클래스에서 초기화 함수를 쓰지 않았다. 그러므로 __init__() 메서드를 오버라이드 하지 않았다.
# 파이썬은 자동으로 부모클래스 Quote 의  __init__() 메서드를 호출해서 인스턴스 변수 person과 words를 저장한다.

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
hunter1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunter1.who(), 'says:', hunter1.says())   # who()는 가져다 쓰고 says()는 자기거 쓴다.
hunter2 = ExclaimationQuote('Daffy Duck', "It's a rabbit season")
print(hunter2.who(), 'says:', hunter2.says())   # who()는 가져다 쓰고 says()는 자기거 쓴다.
# 세개의 서로다른 says() 메서드는 세 클래스에 대해 서로 다른 동작을 제공한다. 이것은 객체지향 언어에서 전통적인 다형성의 특징이다.
# 그러니까 이름이 모두 says()라도 서로 다른 클래스에 따라 서로 다른 동작을 제공한다는거다
class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'
brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(hunter)   # 같은 함수내에서 같은 이름의 메서드를 사용하지만
who_says(hunter1)  # 동작하는 받아오는 객체에 따라 다른 인스턴스를 사용하기 때문에
who_says(hunter2)  # 다르게 동작한다.
who_says(brook)    # 이상!

# 특수 메서드
a = 3 + 8

class Word():
    def __init__(self, text):
        self.text = text
    def equals(self, words2):
        return self.text.lower() == words2.text.lower()
first = Word('ha')
second = Word('HA')
third = Word('eh')
first.equals(second)  # True
first.equals(third)   # False

# equal() 메서드를 __eq__()메서드로 바꿔보자
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
first = Word('ha')
second = Word('HA')
third = Word('eh')
first == second
first == third
# 비교연산을 위한 마법 메서드
# 산술연산을 위한 마법 메서드
# 표는 p.190에서 찾아서 보세요~

# 컴포지션(배합)
# 자식클래스가 부모클래스처럼 행동하고 싶을 때 상속은 좋은 기술이지만 컴포지션이나 어그리게이션이 더 나을 수도 있다.
class Bill():
    def __init__(self, description):
        self.description = description
class Tail():
    def __init__(self, length):
        self.length = length
class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a',
              self.tail.length, 'tail')
tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()
# Duck()가 객체화된 duck에 변수로 tail과 bill이 들어갔다.
# 객체화를 시키면 우선 __init__()만 실행이 되는데 여기에서 선언해주는 많은 self변수들을
# duck객체에서 사용할 수 있게 된다.
# duck은 매개변수로 받은 bill의 변수들(!)을 self.bill에 담고 tail의 변수들(!)을 self.tail에 담아서
# 그 중에서 description과 length를 빼와서 함수를 실행시킨다고 보면된다.

# 네임드 튜플
# 네임드 튜플은 튜플의 서브클래스이다. 이름(.name)과 위치([offset]로 값에 접근할 수 있다.
# 네임드 튜플 함수
# 네임드 튜플은 모듈을 불러와야 한다.
# 이전 코드 사용
from collections import namedtuple
class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a',
              self.tail.length, 'tail')

duck = Duck('wide orange', tail='long')   # 여기는 기존과 같음
duck.bill   # wide orange                 # 여기는 기존과 같음
duck.tail   # long                        # 여기는 기존과 같음

Duck = namedtuple('Duck', 'bill tail')  # 클래스와 bill, tail을 네임드튜플과 간단한 문자열 속성으로 변환
# 즉 클래스를 네임드 튜플로 만들어서 매개변수를 통하는 self변수들을 네임드튜플에 담아 값을 할당할 수 있다.
# (bill='wide orange')
duck = Duck('wide orange', tail='long')   # 그후에 네임드 튜플을 기존과 같이 객체화 시켜준다.
duck   # 이렇게 딕셔너리처럼 사용가능
duck.bill   # duck['bill'] 딕셔너리처럼 이렇게 쓰지 않는다.
duck.tail   # 대신 이렇게 사용
duck.bill = 'abcde'   # 이렇게 바꿀 수 없다!!!!!!!!!!!

parts = {'bill':'wide orange', 'tail':'long'}
parts
duck2 = Duck(**parts)    # 이렇게 딕셔너리로 변환가능!@!#!@#!@#@!#!@#!@
duck2                    # Duck(bill='wide orange', tail='long')

duck2 = Duck(bill='wide orange', tail='long')   # 네임드 튜플 만드는 방법
duck2
# 네임드튜플은 불변한다. 하지만 필드를 바꿔서 또 다른 네임드 튜플을 반환할 수 있다.
duck3 = duck2._replace(tail='magnicent', bill='crushing')   # wow
duck3   # Duck(bill='crushing', tail='magnicent')

# 딕셔너리와 비교!!!!
duck_dict = {'bill':'wide orange', 'tail':'long'}
duck_dict   # 확인
duck_dict['color'] = 'green'   # 딕셔너리에 필드추가 가능
duck_dict   # {'bill': 'wide orange', 'color': 'green', 'tail': 'long'}
duck.color = 'green'  # 위에서 봤듯 당여히 안되고
duck.color   # 당연히 반환도 못한다. 네임드 튜플이 아니기 때문에

