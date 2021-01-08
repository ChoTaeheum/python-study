# CHAPTER 3
# 리스트는 변경가능, 튜플은 불변

# list(리스트)
# 리스트는 데이터를 순차적으로 파악하는데 유용
# 내용의 순서가 바뀔 수도 있어 유용
# 삭제, 덮어쓰기 가능
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']

another_empty_list = list()   # 빈 리스트 할당 []
print(another_empty_list)

list('cat')   # 다른 데이터 타입을 리스트로 변환한다.
a_tuple = ('ready', 'fire', 'aim')
list(a_tuple)   # 튜플을 리스트로 변환

birthday = '1/6/1952'
birthday.split('/')   # split()는 문자열을 구분자로 나누어서 리스트로 변환한다.

splitme = 'a/b//c/d///e'
splitme.split('/')   # 구분자가 연속으로 여러개가 있을때 '' 리스트에 빈 문자열이 들어간다.

# [offset]으로 항목 얻기
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0]
marxes[1]
marxes[2]
# 입력된 오프셋의 값이 리스트의 범위를 넘어갈 경우 에러(예외) 발생

small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
all_birds   # 리스트 안에 리스트와 아이템이 함께 들어있다.
all_birds[0]
all_birds[2]

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
marxes

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0:2] = ['apple', 'blue']   # 이렇게 바꿀 수도 있음
marxes

marxes[::2]
marxes[::-2]
marxes[::-1]

# 리스트의 끝에 항목 추가하기
marxes.append('Zeppo')
marxes

# 리스트 병합하기
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
marxes   # 오른쪽에 갖다 붙이기

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others  # 이렇게도 붙인다.
marxes

# append()를 사용하면 항목을 병합하지 않고 others가 하나의 리스트로 병합된다.
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)   # 리스트로 들어간다.
marxes

# 오프셋과 insert()로 항목 추가하기
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.insert(3, 'Gummo')  # 3번째 오프셋에 'Gummo' 삽입
marxes

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.insert(10, 'Karl')  # 10번째 오프셋이 없으니까 가장 끝에 'Karl' 삽입
marxes

# 오프셋으로 항목삭제하기:del()
del marxes[-1]   # 끝에 있는 아이템 삭제
marxes

# 오프셋으로 리스트의 특정 항목을 삭제하면 제거된 항목 이후의 항목들이 한 칸씩 앞으로 당겨지고 리스트의 길이가 1 감소
del marxes[2:4]   # 이렇게 두개도 삭제가능
marxes

# 값으로 항목 삭제하기:remove()
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.remove('Gummo')
marxes

# 오프셋으로 항목을 얻은 후 삭제하기: pop()
# 항목들을 가져오면서 삭제, 즉 '빼낸다'고 생각하면 편함
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.pop()
marxes
marxes.pop(2)   # 두번째 오프셋 가져오기
marxes
marxes.pop('Groucho')   # 이렇게 값을 가져올 수는 없다!

# 값으로 항목 오프셋 찾기: index()
# 항목값의 리스트 오프셋을 알기
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.index('Chico')

# 존재여부 확인하기
marxes = ['Groucho', 'Chico','Harpo', 'Zeppo']
'Groucho' in marxes
'Bob' in marxes

words = ['a', 'deer', 'a', 'female', 'deer']
'deer' in words   # 적어도 하나의 값만 존재하면 True를 반환한다.

# 값 세기: count()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.count('Harpo')   # 'Harpo' 몇개이니
snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
snl_skit.count('cheeseburger')

# 문자열로 변환하기: join() ★★★★★★★★★★★★★★★★
# join()은 문자열 메서드, 리스트 메서드가 아니다!!
# marxes.join(',')가 더 직관적이지만 이렇게 쓸 수 없다.
# split()와 쓰는 방법도 반대, a.split(',') | (',').join(a)
# split()는 중간의 구분자를 기준으로 나누겠다는 뜻
# join()은 중간의 구분자를 기준으로 합치겠다는 뜻
friends = ['Herry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
joined
separated = joined.split(separator)
separated
separated == friends

# 정렬하기: sort()
# sort()는 리스트 자체를 내부적으로 정렬한다.
# sorted()는 리스트의 정렬된 복사본을 반환한다.

marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
sorted_marxes   # 문자열의 경우 알파벳 순으로 정렬
marxes   # 원본리스트는 변하지 않았다.

marxes.sort()
marxes   # 원본이 바뀌었다.

# 정수와 부동소수점을 혼합해서 쓸 수도 있다. 파이썬이 자동으로 타입을 형변환해주기 때문에..
numbers = [2,1,4.0,3]
numbers.sort()
numbers

numbers = [2,1,4.0,3]
numbers.sort(reverse=True)
numbers

# 항목의 개수 얻기
marxes = ['Groucho', 'Chico', 'Harpo']
len(marxes)

# 할당: =, 복사: copy()
a = [1,2,3]
a
b = a
a
a[0] = 'surprise'   # 항목 바꾸기
a
b   # a가 변하면서 같은 객체를 공유하고 있던 b 역시 변하게 된다.
    # 변수이름은 '스티커'다.

# 스티커가 아닌 따로 객체를 만들고 싶다면 copy()를 사용한다.
a = [1,2,3]
b = a.copy()   # 다 같은 복사본을 만드는 방법!
c = list(a)    # 다 같은 복사본을 만드는 방법!
d = a[:]       # 다 같은 복사본을 만드는 방법!

a[0] = 'integer lists are boring'
a
b   # a와 같은 객체를 공유하지 않는다.
c   # a와 같은 객체를 공유하지 않는다.
d   # a와 같은 객체를 공유하지 않는다.

# 튜플(tuple)
# 임의적인 항목 시퀀스, 리스트와 다르게 튜플을 불변한다. (추가, 삭제, 수정 불가)
# 튜플은 상수의 리스트라고 할 수 있다.
# 튜플생성하기
empty_tuple = ()
empty_tuple

one_marx = 'Groucho',   # 이렇게 하나의 항목을 튜플변수에 담을 수 있다.
one_marx
one_marx = tuple('Groucho')   # 이것은 충격적인 결과!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
one_marx
# 튜플의 아이템이 하나일 경우 문자열 뒤에 ','를 붙여줌으로써 일반 문자열과 구분해준다.
# 문자열 뒤에 ','(comma)를 붙여주지 않으면 구별하지 못한다. 즉 a = ('a')이렇게는 불가능하다. (리스트형태는 가능)
# 두개 이상의 아이템을 할당할 경우에는 마지막 요소에 콤마가 불필요하다. (붙여도 되고)
marx_tuple = 'Groucho', 'Choco', 'Harpo'   # 문자열변수는 두개 이상의 아이템을 갖는 것이 불가능하기 때문에 ()(괄호)가 불필요하다.
marx_tuple
marx_tuple = ('Groucho', 'Choco', 'Harpo') # 이렇게 붙여도 되고
marx_tuple

# 튜플은 한번에 여러 변수에 할당할 수 있다.
marx_tuple = ('Groucho', 'Choco', 'Harpo')
a, b, c = marx_tuple
a
b
c
# 이것을 튜플 언패킹이라고 한다.

password = 'swordfish'
icecream = 'tuttifrutti'
abc = password, icecream   # 두개이상의 문자열의 집합은 리스트형태가 아니면 무조건 튜플이다.

# 한문장에서 값을 교환하기 위해 임시변수를 사용하지 않고 튜플을 사용할 수 있다.
password = 'swordfish'
icecream = 'tuttifrutti'
icecream, password = password, icecream
icecream
password

# tuple()은 다른 객체를 튜플로 만들어준다.
marx_list = ['Groucho', 'Chico', 'Harpo']
tuple(marx_list)

# 튜플의 장점
# 튜플은 더 작은 공간을 활용한다.
# 튜플은 딕셔너리 키로 사용할 수 있다.
# 네임드 튜플은 객체의 단순한 대안이 될 수 있다.
# 함수의 인자들은 튜플로 전달된다.

# 딕셔너리
# 딕셔너리는 항목의 순서를 따지지 않는다.
# 오프셋으로 항목을 선택할 수 없다.
# 키와 밸류 설정, 키는 불변

# 딕셔너리 생성하기
# {}중괄호 안에 콤마로 구분된 키와 값을 가진다.
empty_dict = {}
empty_dict

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "MIstaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misess"
}
bierce   # 딕셔너리는 순서를 갖지 않는다.

# 딕셔너리로 변환하기: dict()
lol = [['a','b'], ['c','d'], ['e','f']]
dict(lol)   # 오호라~
lot = [('a','b'), ('c','d'), ('e','f')]
dict(lot)
tol = (['a','b'], ['c','d'], ['e','f'])
dict(tol)
los = ['ab', 'cd', 'ef']
dict(los)
tos = ('ab', 'cd', 'ef')
dict(tos)

# 항목 추가/변경하기: [key]
# 키에 의해 참조되는 항목에 값을 할당하면 된다.
# 키가 딕셔너리에 이미 존재하는 경우 그 값은 새 값으로 대체된다.
# 키가 존재하지 않는 경우 키와 사전에 추가된다.

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael'
}
pythons['Gilliam'] = 'Gerry'
pythons
pythons['Gilliam'] = 'Terry'
pythons
# 딕셔너리의 키는 반드시 유니크
# 만약 키값이 두개가 같다면 마지막 키만 살아남는다.

# 딕셔너리 결합하기: update()
# update()함수는 한 딕셔너리의 키와 값들을 복사해서 다른 딕셔너리에 붙여준다.
others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
pythons
# 만약 같은 키값이 결합하려는 딕셔너리에 동시에 있다면 두번째 딕셔너리의 값이 승리한다.

# 키와 del로 항목 삭제하기
del pythons['Marx']
pythons

# 모든 항목 삭제하기: clear()
pythons.clear()
pythons


# in으로 키 멤버쉽 테스트하기
'Chapman' in pythons   # True
'Gillium' in pythons   # False

# 항목얻기: [key]
pythons['Cleese']
pythons['Marx']   # 존재하지 않으면 예외
# 예외뜨는 문제를 해결하는 방법 (try, except 귀찮으니까)

pythons.get('Marx')     # 존재하지 않으면 아무것도 출력되지 않는다.
pythons.get('Cleese')   # 값이 존재하면 출력
pythons.get('Marx', 'Not a python')   # 옵션값을 지정해서 원하는 값을 출력가능, 실제로 추가되지는 않는다.

# 모든 키와 밸류 얻기: keys(), values()
# 딕셔너리의 모든 키를 얻기 위해서는 keys()를 사용한다.
signals = {'green':'go', 'yellow':'go faster', 'red':'smile for the camera'}
signals.keys()   # dict_keys라는 데이터 타입에 담긴다는 것을 기억해!
signals_keys_list = list(signals.keys())      # list로 사용하기
signals_keys_list
signals.values()
signals_values_list = list(signals.values())  # 이것도 역시 list로 사용가능
signals_values_list
signals.items()   # 튜플형태로 반환한다.
signals_items_list = list(signals.items())  # 이것도 역시 list로 사용가능
signals_items_list

# 셋
# 셋은 값은 버리고 키만 남은 딕셔너리와 같다. 각 키는 유니크하다. 딕셔너리와 마찬가지로 셋은 순서가 없다.
# 셋 생성하기: set()
empty_set = set()
empty_set
even_numbers = {0,2,4,6,8}
even_numbers
odd_numbers = {1,3,5,7,9}
odd_numbers

# 리스트, 문자열, 튜플, 딕셔너리로부터 중복된 값을 버린 셋을 생성할 수 있다.
set('letters')
tuple('letters')
list('letters')
dict('letters')   # 요건 에러

set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])   # set 만들기
set({'Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'})   # set 만들기
set(('Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'))   # set 만들기
set({'Dasher':'a', 'Dancer':'b', 'Prancer':'c', 'Mason-Dixon':'d'})   # set을 만드는데 key만 가져와서 만든다.

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}
# 셋은 값들의 시퀀스일 뿐이고 딕셔너리는 키와 값의 쌍으로 이루어져 있다.

# in으로 값 멤버쉽 테스트하기
drinks.items()
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

# 콤비네이션 연산자
# 셋 인터섹션 연산자(셋 교집합 연산자)
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:   # 여기서 &는 교집합을 뜻한다.
        print(name)                               # contents와 {'vermouth', 'orange juice'}이 교집합을 가지고 있는 경우 name를 출력한다.

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:   # vodka가 contents에 들어있고
        print(name)                                                    # {'vermouth', 'cream'}와 교집합이 없는 것

bruss = drinks['black russian']
wruss = drinks['white russian']
type(bruss)   # 타입은 set

a = {1,2}
b = {2,3}
a & b   # 교집합
a.intersection(b)   # 교집합

bruss & wruss   # 밸류에 교집합이 있는가?

a|b   # 합집합
a.union(b)   # 합집합
bruss | wruss   # 합집합
bruss.union(wruss)   # 합집합

a - b   # 차집합
a.difference(b)   # 차집합
bruss - wruss   # 차집합
wruss - bruss   # 차집합

a ^ b                       # 대칭차집합 : 한쪽에는 있지만 양쪽 모두에 들어있지 않은 멤버들
a.symmetric_difference(b)   # 즉, 서로 차집합을 수행한 후에 합집합을 한 것과 같다.
bruss ^ wruss

a <= b         # 첫번째 셋이 두번째 셋의 서브셋(부분집합)인지 살펴보기
a.issubset(b)  # 즉, 첫번째 셋이 두번째 셋에 완전히 포함되는가?
bruss <= wruss   # bruss는 wruss를 포함한다.

a < b          # 첫번째 셋이 두번째 셋의 진부분집합(즉 두번째 셋이 다 포함하고도 다른 멤버를 더 가지고 있는 셋)인가
a < a          # 프로퍼 서브셋
bruss < wruss

a >= b          # 슈퍼셋은 서브셋의 반대, 두번째 셋을 포함하는가
a.issuperset(b) # a가 b를 포함하는가
a >= a          # 모든 셋은 자신의 슈퍼셋이자 서브셋이다.
a <= a          # 모든 셋은 자신의 슈퍼셋이자 서브셋이다.

a > b              # 프로퍼 수퍼셋
wruss > wruss      # 프로퍼 수퍼셋
a > a

# 자료구조 비교하기
marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_dict = {'Groucho': 'banjo', 'Chico':'piano', 'Harpo':'harp'}
marx_list[2]
marx_tuple[2]
marx_dict['Harpo']

  