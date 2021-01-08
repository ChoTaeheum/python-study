# CHAPTER 5 파이 포장하기: 모듈, 패키지, 프로그램
# 스탠드 얼론 프로그램
# 메모장에서 코딩을 하고 *.py로 저장한 후에 cmd창에서 python *.py라고 실행시킬 수 있게 만드는 것을 스탠드얼론 프로그램이라고 한다.

# 모듈과 임포트문
# 모듈 임포트 하기
# 모듈은 .py확장자가 없는 파이썬 파일의 이름이다.
# 여기는 메인 프로그램
import report   # report 전체를 임포트하기
description = report.get_dexcription()   # 임포트하기
print("Today's weather:", description)

# 여기는 모듈 부분만 골라서 임포트
def get_description():
    """Return random weather, just like the pros"""
    from random import choice   # 부분만 골라서 임포트하기
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)

# 이렇게도 사용가능
def get_description():
    """Return random weather, just like the pros"""
    import random   # 전체 다 임포트하기
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return random.choice(possibilities)

from abc.abc import abc
# from 디렉토리.패키지 import 모듈
# from 디렉토리.파일(.py) import 메서드(def)

# 다른 이름으로 모듈 임포트하기
# import report as wr
# description = wr.get_description()
# print("Today's weather:", description)
#
# 필요한 모듈만 임포트하기
# 모듈 전체 또는 필요한 부분만 임포트할 수 있다.
from report import get_description
description = get_description()
print("Today's weather:", description)

# 모듈검색경로
# 파이썬은 임포트할 파일을 어디서 찾을까?
import sys
for place in sys.path:
     print(place)
     # 아주 유용하구나!!!!!
# 중복된 이름의 모듈이 있다면 첫번째 조건을 사용한다.
# 즉 앞선 검색경로에 존재하는 모듈을 사용한다는 뜻

# 패키지
# 파이썬 어플리케이션을 좀 더 확장가능하게 만들기 위해 패키지라는 계층구조에
# 구성할 수 있다.
# from 에는 패키지(디렉토리), 모듈(파일)
# import 에는 모듈(파일), 메소드(함수)
# 이렇게 입력가능하다.
# 실행파일과 같은 경로에 있는 패키지나 모듈은 자동으로 패키지 사용경로로 설정된다.
from sources import daily, weekly
# from 패키지 import 모듈, 모듈
# sources 디렉토리에 __init__.py라는 파일이 있어야 그 디렉토리를 패키지로 인식한다.
# 이 파일의 내용은 비워도 상관없다.
#
# 파이썬 표준 라이브러리
# 빌트인모듈이라고 생각하면 된다.
#
# 누락된 키 처리하기: setdefault(), defaultdict()
# 존재하지 않는 키로 딕셔너리에 접근을 시도하면 예외가 발생한다.
# setdefault()함수는 get()함수와 비슷하지만 키가 누락된 경우 딕셔너리에 항목을 할당할 수 있다.
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
periodic_table
periodic_table['Carbon'] = 12   # 이거랑 다른게 뭔데??? 이건 그냥 할당
# 다른게 뭐냐면 setdefault()는 딕셔너리에 접근해서 원하는 값을 할당함과 동시에 접근한다.
# 대신 존재하는 키에 접근해서 setdefault()를 사용하면 키에 대한 원래값이 반환되고 새로운 값을 할당하지 않는다.
helium = periodic_table.setdefault('Helium', 947)
helium
periodic_table
# 즉 해당 키의 값을 반환해보고 키가 없어서 반환할게 없으면 새로운 키를 만들고 값을 할당한다.

# defaultdict()함수도 비슷하다.
# 다른점은 딕셔너리를 생성할 때 모든 새키에 대한 기본값을 먼저 지정한다는 것이다.
#
from collections import defaultdict
periodic_table = defaultdict(int)   # 새로 만들어지는 키에 대한 밸류를 기본으로 0을 지정하는 딕셔너리 생성
# a = dict(), 그냥 이거 진화한 형태라고 보면 됩니다.
print(periodic_table)   # 처음엔 빈 리스트

periodic_table['Hydrogen'] = 1  # 1할당
periodic_table['Lead']          # 0할당
periodic_table

# defaultdict()의 인자는 값을 누락된 키에 할당하여 반환하는 함수이다.
from collections import defaultdict
def no_idea():
     return 'huh?'
bestiary = defaultdict(no_idea)   # 이 함수의 매개변수로 함수를 실행한 값을 지정할 수 없다.
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])
# 빈 기본값을 반환하기 위해 int()는 정수 0, list() 함수는 빈 리스트[], dict()함수는 빈 딕셔너리를 반환한다.
# 인자를 입력하지 않으면 새로운 키의 초기값이 None로 설정된다.

bestiary = defaultdict(lambda: 'Huh?')   # 기본값을 huh?로 할당
bestiary['E'] # huh? 출력

# 카운터를 만들기 위해 아래와같이 int()함수를 사용할 수 있다.
from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
     food_counter[food] += 1   # 위 리스트에 해당하는 키가 들어올때마다 1씩 더해서 새로 갱신한다.
for food, count in food_counter.items():
     print(food, count)   # eggs 1, spam 3

# 위와같은 방법을 defaultdict()를 사용하지 않고 구현하려면 아래와 같이한다.
dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
     if not food in dict_counter:
          dict_counter[food] = 0    # 딕셔너리에 존재하지 않으면 0을 할당하고 있으면 통과
     dict_counter[food] += 1        # if 절에서 나와서 1을 더해주고
for food, count in dict_counter.items():
     print(food, count)

# 항목세기: counter()
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
# breakfast_counter   # Counter({'spam':3, 'eggs':1})

# most_common() 함수는 모든 요소를 내림차순으로 반환한다.
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(2))   # 숫자를 입력하는 경우 그 숫자만큼 상위요소를 반환한다.

# 카운터를 결합할 수도 있다.
breakfast_counter = {'eggs': 3, 'eggs': 1}
# Counter({'spam':3, 'eggs':1})
lunch = ['spam', 'eggs' , 'bacon']
lunch_counter = Counter(lunch)
lunch_counter   # Counter({'eggs':2, 'bacon':1})

breakfast_counter + lunch_counter   # 합집합
breakfast_counter - lunch_counter   # 차집합
breakfast_counter & lunch_counter   # 교집합
breakfast_counter | lunch_counter   # 유니온 연산자, 공통항목을 출력하되 숫자가 큰 것을 출력

# 키 정렬하기
# 이 책의 앞부분에서 딕셔너리의 키 순서는 예측할 수 없다고 했다.
quotes = {'Moe':'A wise huy, huh?',
         'Larry':'Ow!',
         'Curly':'Nyuk nyuk!'}
for stooge in quotes:
    print(stooge)   # 키의 순서를 예측할 수 없다.

# OrderedDict() 함수는 키의 추가 순서를 기억하고 이터레이터로부터 순서대로 키값을 반환한다.
# (키, 값) 튜플의 시퀀스로부터 OrderedDict를 생성해보자
from collections import OrderedDict
quotes = ([('Moe','A wise huy, huh?'),
           ('Larry','Ow!'),
           ('Curly','Nyuk nyuk!')])
# 입력한 순서대로 키를 반환

# 스택 + 큐 == 데크
# 리스트는 기본적으로 stack의 형태를 가지고 있다.(append()와 pop() 함수)
# 여기서 deque()함수를 통해 큐와 스택의 기능 모두 가지고 있는 리스트를 만들어 준다!!!!
# 즉 popleft()나 appendleft()를 사용할 수 있다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 데크는 스택과 큐의 기능을 모두 가진 출입구가 양쪽에 있는 큐다.
# 데크는 시퀀스의 양 끝으로부터 항목을 추가하거나 삭제하는데 유용하게 쓰인다.
# 여기에서 회문(앞에서 읽으나 뒤에서 읽으나 똑같은 단어)


def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        return True
print(palindrome('racecar')) # True
print(palindrome('abc'))     # False

# 리스트는 기본적으로 stack의 형태를 가지고 있다.(append()와 pop() 함수)
from collections import deque
a = deque([1,2,3,4,5])
a.appendleft(3)
a.popleft()
a.pop()
a.append(7)
print(a)

# palindrome()함수의 간단하게 작성하기!!!!@!@@@!@!2
def another_palindrome(word):
    return word == word[::-1]   # 문자 뒤집기 슬라이싱
another_palindrome('radar')
another_palindrome('abc')

# 코드구조 순회하기
# itertools는 특수목적의 이터레이터 함수를 포함
# for ... in 루프에서 이터레이터 함수를 호출할 때 함수는 한번에 한 항목을 반환하고 호출상태를 기억한다.
# chain()함수는 순회가능한 인자들을 하나씩 반환한다.
import itertools
for item in itertools.chain([1,2], ['abc','def']):
    print(item)

# cycle()함수는 인자를 순환하는 무한이터레이터이다.
import itertools
for item in itertools.cycle([1,2,3,4]):
    print(item)

# accumulate()함수는 축적된 값을 계산한다. 디폴트는 합을 계산한다.
import itertools
for item in itertools.accumulate([1,2,3,4,5]):
    print(item)

for item in itertools.accumulate([1,2,3,4,5], multiply):   # 이거 안되는데?
    print(item)

# 깔끔하게 출력하기
from pprint import pprint
quotes = OrderedDict([('Moe', 'A wise guy, huh?', 'Larry', 'Ow'), ('Curly', 'Nyuk nyuk!'),])
print(quotes)
pprint(quotes)

# 배터리 장착
# PyPI
# github
# readthedocs
