# CHAPTER 4. 파이크러스트:코드 구조
# 라인 유지하기
alphabet = ''
alphabet += 'abcdefg'
alphabet += 'hijklmn'
alphabet += 'opqrstu'
alphabet += 'vwxyz'
alphabet

alphabet = 'abcdefg' + \
    'hijklmn' + \
    'opqrstu' + \
    'vwxyz'
alphabet

# 비교하기: if, elif, else
disaster = True
if disaster:
    print('woe!')
else:
    print('whee!')
# if와 else는 조건이 참인지 거짓인지 확인하는 파이썬의 선언문(statement)
# print()는 파이썬의 내장함수
# 파이썬 대화형 인터프리터를 사용할 경우 탭과 스페이스를 혼용하지 않는 것을 권한다.
furry = True
small = True
if furry:
    if small:
        print("It's a cat")
    else:
        print("It's a bear")
else:
    if small:
        print("It's a skink")
    else:
        print("It's a human. Or a hairless bear")

color = 'puce'
if color == 'red':
    print("It's a tomato")
elif color == 'green':
    print("It's a green pepper")
elif color == 'bee purple':
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color puce", color)

# 파이썬의 비교연산자
# == 같다.
# != 다르다.
# < 보다 작다.
# <= 보다 작거나 같다.
# > 보다 크다.
# >= 보다 크거나 같다.
# in ... 멤버쉽
# 비교연산자는 부울값 True 혹은 False를 반환한다.
x = 7
x == 5
x == 7
x < 10
x > 10
# 만약 동시에 여러개의 식을 비교해야 한다면 최종 부울값을 판단하기 위해 and, or, not와 같은 부울 연산자를 사용할 수 있다.
5 < x and x < 10
(5<x) and (x<10)
5 < x < 10
5 < x < 10 < 999
# 이렇게 비교도 가능하다.

# False는 명시적으로 False라고 표시할 필요가 없다.
# 다음은 모두 False로 간주한다.
# None
# 0
# 0.0
# ''
# []
# ()
# {}
# set()
some_list = []
if some_list:
    print("There's a something in here")
else:
    print("Hey it's empty")

# 반복하기: while
count = 1
while count <= 5:
    print(count)
    count += 1
# while문은 count의 값이 5보다 작거나 같은지 계속 비교한다.
# 변수가 5에서 6으로 증가될 때까지 계속 수행한다.

# 중단하기: break
# 언제 어떤 일이 일어날지 확실하지 않다면 루프 안에 break를문을 사용한다.
while True:
    stuff = input("String to capitalize [type q to quit]:")
    if stuff == 'q':
        break   # q를 입력하면 나와라
    print(stuff.capitalize())

# 건너뛰기: continue
# 반복문을 중단하고 싶지는 않지만 이번 루프의 작동을 완료하고 다음 루프로 건너뛰고 싶을때 사용한다.
while True:
    value = input("Integer, please [q to quit]")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number, "squared is", number**2)

# break 확인하기: else
# break는 어떤 것을 체크하고 반복문을 나가는 명령어이다.
# 하지만 while문이 모두 완료될 때까지 break조건을 찾지 못하면 else가 실행된다.
numbers = [1,3,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:
    print('No even number found')


# 순회하기: for
# 데이터가 메모리에 맞지 않더라도 데이터 스트림을 처리할 수 있도록 허용해준다.
rabbits = ['Flospy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

# 파이써닉한 우아한 방법
for rabbit in rabbits:
    print(rabbit)

word = 'cat'
for letter in word:
    print(letter)   # 이런 것도 되는구나

accusation = {'room':'balloom', 'weapon':'pipe', 'person':'Col. Mustard'}
for card in accusation:
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)

# 한번에 튜플 하나씩만 할당할 수 있다.
# 튜플의 첫번째 내용(키)은 card에 두번째 내용(밸류)는 contents에 할당된다.
for card, contents in accusation.items():
    print('card',card, 'has the contents', contents)

# 중단하기: break
# for문의 break는 while문의 break와 똑같이 동작한다.

# 건너뛰기: continue
# for문의 continue는 while문의 continue와 똑같이 동작한다.

# break 확인하기: else
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break     # break에 의해 반복문이 중단되었는지 확인하는 것
else:         # 즉 break가 작동되지 않고 정상적으로 반복문이 모두 완료되면 else가 작동한다.
    print('This is not much of a cheese shop, is it?')

# 좀 더 직관적으로 알아볼 수 있는 break, else 하드코드
cheese = []
found_one = False
for cheese in cheeses:
    found_one = True
    print('This shop has some lovely', cheese)
    break
if not found_one:
    print('This is not much of a cheese shop, is it?')

# 여러시퀀스 순회하기: zip()
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, '/', fruit, '/', drink, '/', dessert)
# 여러 시퀀스중 가장 짧은 시퀀스가 완료되면 zip()은 멈춘다.

english = ('Monday', 'Tuesday', 'Wednesday')
french = ('Lundi', 'Mardi', 'Mercredi')
# 두개의 튜플을 순회 가능한 튜플로 만들기 위해 zip()을 사용한다.
# zip()에 의해 반환되는 값은 튜플이나 리스트 자신이 아니라 하나로 반환될 수 있는 순회 가능한 값이다.
list(zip(english, french))    # [('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]
tuple(zip(english, french))   # (('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi'))
dict(zip(english, french))    # {'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi'}

# 숫자 시퀀스 생성하기: range()
for x in range(0,3):
    print(x)
list(range(0,3))

for x in range(2,-1,-1):
    print(x)
list(range(2,-1,-1))

list(range(0,11,2))

# 컴프리헨션
# 컴프리헨션이란 하나 이상의 이터레이터로부터 파이썬의 자료구조를 만드는 방법
number_list = []
for number in range(1,6):
    number_list.append(number)
number_list

number_list = list(range(1,101))
number_list = [a for a in range(1, 101)]
number_list = [a+1 for a in range(1,101)]

# [표현식 for 항목 in 순회가능한 객체 if 조건]
a_list = []
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)
a_list

a_list = [number for number in range(1,6) if number%2 == 1]
a_list   # 이렇게 더 콤팩트한 방법 사용가능

# 이중루프 컴프리헨션
rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row, col)

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for row, col in cells:
    print(row, col)

# 딕셔너리 컴프리헨션
# {키_표현식:값_표현식 for 표현식 in 순회 가능한 객체}
word = 'letters'
letter_counts = {letter:word.count(letter) for letter in word}
letter_counts

# 셋 컴프리헨션
a_set = {number for numbers in range(1,6) if number%3 == 1}
a_set

# 제너레이터 컴프리헨션
# 튜플은 컨프리헨션이 없다. 컴프리헨션의 []를 ()로 바꿔서 사용해도 튜플 컴프리헨션이 생성되지 않는다.
number_thing = (number for number in range(1,6))
type(number_thing)

for number in number_thing:
    print(number)   # 이렇게 제너레이터 객체를 순회할 수 있다.

number_list = list(number_thing)
number_list   # 리스트 컴프리헨션처럼 만들기 위해 제너레이터 컴프리헨션에 list() 호출을 통해 랩핑할 수 있다.

try_again = list(number_thing)
try_again
#####★★★★★★★만약 다시 순회하려고 한다면 아무것도 볼 수 없다.
# 제너레이터는 한번만 실행될 수 있다. 리스트, 셋, 문자열, 딕셔너리는 메모리에 존재하지만, 제너레이터는 즉석에서 그 값을 생성하고,
# 이터레이터를 통해서 한번에 값을 하나씩 처리한다. 제너레이터는 이 값을 기억하지 않기 때문에 다시 시작하거나 제너레이터를 백업할 수 없다.

# 함수
# 함수는 입렵 매개변수로 모든 타입을 여러개 취할 수 있다. 그리고 반환값으로 모든 타입을 여러 개 반환할 수 있다.

def do_nothing():
    pass   # 아무것도 하지 않는다는 것을 보여주기 위해 pass

def make_a_sound():
    print('quack')
make_a_sound()

def agree():
    return True
if agree():
    print('Splendid')
else:
    print('That was unexpected')

def echo(anything):
    return anything + ' ' + anything
echo('Rumplestiltskin')

def commentary(color):
    if color == 'red':
        return "It's a tomato"
    elif color == 'green':
        return "It's a green pepper"
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it"
    else:
        return "I've never heard of the color " + color + ","
comment = commentary('blue')   # 매개변수가 들어가서 반환된 값이 저장된다.
print(comment)

# 만약 함수가 명시적으로 return을 호출하지 않으면 호출자는 반환값으로 return을 얻는다.

# 유용한 None
thing = None
if thing:
    print("It's something")
else:
    print("It's nothing")
# True는 아니지만 False도 아니다.

if thing is None:
    print("It's nothing")
else:
    print("It's something")

def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")

is_none(None)
is_none(True)
is_none(False)
is_none(0)
is_none(0.0)
is_none(())
is_none([])
is_none({})
is_none(set())

# 위치인자
def menu(wine, entree, dessert):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}
menu('chardonnay', 'chicken', 'cake')

# 키워드인자
# 이와같이 매개변수에 상응하는 이름을 인자에 지정할 수 있다.
menu(entree='beef', dessert='bagel', wine='fish')   # 이렇게 순서가 달라도 지정가능하다.
menu('frontenac', dessert='flan', entree='fish')    # 이렇게 위치인자와 키워드인자를 섞어서 쓸 수 있다.

# 기본 매개변수값 지정하기
def menu(wine, entree, dessert='pudding'):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}
menu('chardonnay', 'chicken')
menu('dunkelfelder', 'dunk', 'doughnut')

def buggy(arg, result=[]):   # 여기서 먼저 빈 리스트를 지정해준다.
    result.append(arg)
    print(result)
buggy('a')
buggy('b')

def works(arg):              # 위의 함수와 같은 함수
    result = []
    result.append(arg)
    return result
works('a')
works('b')

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
nonbuggy('a')
nonbuggy('b')

# 위치인자 모으기: * (애스터리스크)
# 함수의 매개변수에 애스터리스크를 사용할 때 애스터리스크는 매개변수에서 위치인자 변수들을 튜플로 묶는다.
def print_args(*args):
    print('Positional argument tuple:', args)
print_args()                          # 함수를 인자없이 호출하면 &args에는 아무것도 없다.
print_args(3,2,1,'wait!','uh...')     # 매개변수를 묶어서 튜플로 반환한다.

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)
print_more('cap','gloves','scarf','monocle','mustache wax')

# 키워드 인자 모으기
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

# docstring
def print_echo(anything):
    'echo return sits input argment'
    return anything

def print_if_true(thing, check):
    '''
    :param thing: 이거는 이거 
    :param check: 저거는 저거
    :return: 그래서 이거
    '''
    pass
help(print_if_true)
print(print_if_true.__doc__)

# 일등시민: 함수
# 함수는 변수에 할당할 수 있고, 다른함수에서 이를 인자로 쓸 수 있으며 함수에서 이를 반환할 수도 있다.
def answer():
    print(42)
def run_something(func):
    func()
run_something(answer)    # 함수의 매개변수로 함수를 받아서 실행시킬 수 있다.
type(run_something)      # answer를 전달한다는 것은 함수를 다른 객체와 같이 간주한다는 뜻이다.

def add_args(arg1,arg2):
    print(arg1 + arg2)
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)
run_something_with_args(add_args, 4, 9)
# 매개변수로 함수와 숫자를 받아서 처리함 add_args(4,9)와 같음

def sum_args(*args):
    return sum(args)
def run_with_positional_args(func, *args):
    return func(*args)   # 인자를 튜플 하나로 받는 것이 아니라 여러개의 인자로 받아서 func에 넣어주기 위해 * 붙인다.
run_with_positional_args(sum_args, 1,2,3,4)

# 내부함수
def outer(a,b):        # 1
    def inner(c,d):    # 3
        return c+d     # 4
    return inner(a,b)  # 2
outer(4,11)

def knight(saying):
    def inner(quote):
        return "We are the knight who say: '%s'" % quote   # format과 같은 역할
    return inner(saying)
knight('Ni!')

# 클로저
# 내부함수는 클로저처럼 행동할 수 있다. 클로저는 다른 함수에 의해 동적으로 생성된다.
# 그리고 바깥 함수로부터 생성된 변수값을 변경하고, 저장할 수 있는 함수이다.
def knight2(saying):
    def inner2():
        return "We are the knight who say: '%s'" % saying   # format과 같은 역할
    return inner2
# 여기서 inner2가 '클로저'이다.
# return inner2는 inner2함수의 특별한 복사본을 반환한다.

a = knight2('Duck')          # 외부함수에 변수를 넣어서 inner2()를 객체화시킴
b = knight2('Hasenpfeffer')
type(a)
type(b)
a()
b()
a
b

# 익명함수: lambda()
# 파이썬의 람다함수는 단일문으로 표현되는 익명함수(anonymous function)이다.
def edit_story(words, func):   # words의 각 문자열을 func의 매개변수로 받아서 순회하면서 실행
    for word in words:         # 하는 함수
        print(func(word))
stairs = ['thud', 'meow', 'thud', 'hiss']   # 재료로 쓸 문자열 시퀀스
def enliven(word):
    return word.capitalize() + '!'
edit_story(stairs, enliven)

# 위의 함수실행절차를 lambda로 실행
edit_story(stairs, lambda word: word.capitalize()+'!')
# 람다의 :콜론 이후가 람다함수의 정의부분이다.

# 제너레이터
# 제너레이터는 파이썬의 시퀀스를 생성하는 객체이다.
# 전체 시퀀스를 한번에 메모리에 생성하고 정렬할 필요 없이 잠재적으로 아주 큰 시퀀스를 순회할 수 있다.
# 대표적으로 range()가 있다.
# 제너레이터를 순회할 때마다 마지막으로 호출된 항목을 기억하고 다음 값을 반환한다.
# 제너레이터는 일반함수와 다르다. 일반함수는 이전 호출에 대한 메모리가 없고, 항상 똑같은 상태로 첫번째 라인부터 수행한다.
# 제너레이터 함수는 return문으로 반환하지 않고 yeild문으로 값을 반환한다.
# 제너레이터 컴프리헨션
a = (i for i in range(10))
for i in a:   # 제너레이터는 한번만 순회가능하다.
    print(i)  # 즉 어떠한 형태로든 한번만 사용가능하다.
a = (i for i in range(10))
b = list(a)   # 리스트화도 한번만 가능하다.
b
c = list(a)   # 여기선 빈 리스트 생성
c

# 자주 쓰이는 제너레이터의 예는 range()
sum(range(1,101))
def my_range(first=0, last=10, step=1):   # 제너레이터 함수만들기
    number = first                        # 순회가능한 시퀀스를 만든다고 보면 된다.
    while number < last:
        yield number
        number += step
for i in my_range():
    print(i)   # 제너레이터는 순회함으로써 출력가능하다.


# 데커레이터
# 데커레이터는 하나의 함수를 취해서 또 다른 함수를 반환하는 함수이다.
# *args, **kwargs
# 내부함수
# 함수인자
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional argumants:', args)
        print('Keyword argument:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function
# 함수이름과 인자값을 출력한다.
# 인자로 함수를 실행한다.
# 결과를 출력한다
# 수정된 함수를 사용할 수 있도록 반환한다.

def add_ints(a, b):
    return a + b
add_ints(3,5)

cooler_add_ints = document_it(add_ints)   # 데커레이터를 수동으로 할당
cooler_add_ints(3,5)

@document_it
def add_ints(a,b):
    return a + b
add_ints(3,5)

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result*result
    return new_function

@document_it
@square_it    # 이렇게 데코레이터를 두개 사용할 수도 있다.
def add_ints(a, b):
    return a + b
add_ints(3, 5)

# 네임스페이스와 스코프
# 네임스페이스는 특정 이름이 유일하고 다른 네임스페이스에서의 같은 이름과 관계가 없는것을 말한다.
# 메인 프로그램에서 x라는 변수를 정의하고, 함수에서 x라는 변수를 정의했을 때 이들은 서로 다른 것을 참조한다.
# 하지만 다양한 방법으로 이 경계를 넘을 수 있다.
# 메인프로그램은 전역 변수의 값을 얻을 수 있다. (global variable)
animal = 'fruitbat'   # 전역변수
def print_global():
    print('at the top level:', animal)
print('at the top level:', animal)
print_global()    # 함수로부터 전역변수의 값을 얻을 수 있다. animal = 'fruitbat'을 받아서 사용한다.

def change_and_print_global():    # 함수에서 전역변수의 값을 바꾸려고 하면 에러가 발생한다.
    print('inside change_and_print_global:', animal)    # 여기서 우선 사용을 해주면서 전역변수를 끌어오고
    animal = 'wombat'                                   # 여기서 수정해준다.
    print('after the change:', animal)                  # 수정한 값을 다시 사용
change_and_print_global()     # 에러 발생, 즉 함수내에서는 전역변수의 값을 사용할 수는 있으되 갱신은 하지 못한다.

def change_and_print_global():
    animal = 'wombat'                                   # 아까와 다르게 전역변수를 끌어오지 않고 여기서 만들어준다.
    print('after the change:', animal)

# 이름에 _와 __사용
# 이름 맨 앞에
def amazing():
    '''This is the amaizing function.
    Want to see it again?'''
    print('This function is names:', amazing.__name__)   # 여기에 함수 이름 저장된다.
    print('And its docstring is:', amazing.__doc__)      # 여기에 함수 docstring 저장된다.
amazing()

# 에러 처리하기
# 어떤 상황에서 실패할 수 있는 코드를 실행했을 때는 모든 잠재적인 에러를 방지하기 위해 적절한 예외처리가 필요하다.
short_list = [1,2,3]
position = 5
short_list[position]   # 예외발생@@@@!!@!!!

short_list = [1,2,3]
position = 5
try:
    short_list[position]
except:   # 예외발생시 아래 명령문 실행
    print('Need a position between 0 and', len(short_list)-1, 'but got', position)

short_list = [1,2,3]
while True:
    value = input('Position [q to quit]?')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:     # 인덱스 에러나면 아래 명령문 실행
        print('Bad index:', position)
    except Exception as other:    # 나머지 모든 예외는 아래 명령문 실행
        print('Something else broke:', other)

# 예외만들기
# 예외를 정의할 수 있다.
# 새로운 예외 타입을 정의하려면 클래스 객체타입을 정의해야한다.
class UppercaseException(Exception):
    pass
words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():     # 대문자 발견하면
        raise UppercaseException(word)   # 아래 예외 실행

try:
    raise OopsException('panic')   # OopsException을 발생시켜라
except OopsException as exc:       # OopsException 예외가 발생했으므로 아래 명령어를 실행해라
    print(exc)                     # exc는 OopsException 발생했으므로 'panic'(예외클래스에 미리 할당 가능)을 출력한다.

