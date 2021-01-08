# CHAPTER 2
# 2.1 변수, 이름, 객체
# 파이썬 데이터 타입
# 부울, 정수, 실수, 문자열
# 파이썬은 객체의 타입을 바꿀 수 없다! (강타입)
a = 7
print(a)
# 변수는 객체의 참조일 뿐 객체를 포함하는 개념이 아니다.
a = 7
print(a)
b = a
print(b)
#
# 변수 혹은 리터럴값의 타입 확인
type(a)
type(b)
type(58)
type(99.9)
type('abc')

# 클래스는 객체의 정의를 의미한다. 파이썬에서 'class'와 'type'은 그 의미가 거의 같다.

# 변수이름에 사용가능한 문자
# 소문자(a~z)
# 대문자(A~Z)
# 숫자(0~9)
# 언더스코어(_)

# 변수이름은 숫자로 시작할 수 없다.
# 파이썬은 언더스코어로 시작하는 이름을 특별한 방법으로 처리
# 유효한 이름의 예
# a
# a1
# a_b_c___95
# _abc
# _1a

# 사용불가능한 이름의 예
# 1
# 1a
# 1_

# 파이썬의 예약어들은 변수로 선언하면 안된다.
# False, class, finally, is, return, None, continue, for, lambda, try, ...... 등


# 2.2 숫자
# 파이썬은 정수(5, 1,000,000,000 등)와 부동소수점수(3.1416, 14.99, 1.87e4 등)를 지원하는 기능이 내장되어 있다.
# 연산자
# + 더하기
# - 빼기
# * 곱하기
# / 부동소수점나누기
# // 정수나누기 (소수점 이하 버림)
# % 나머지
# ** 지수

# 숫자 앞에 기호가 없으면 양수
# 숫자 앞에 -가 붙으면 음수
4 + 4 + 2 + 9 - 2 - 5
6 * 7
9 / 5
9 // 5   # 소수점 이하는 버리고 정수만 출력
5 / 0    # 0으로 나누면 예외 발생

a = 95
a = a-3
a
a -= 3
a
a += 8
a
a *= 2
a
a /= 3
a
a //= 4
a
9 % 5
9 // 5
divmod(9,5)

2 + 3 * 4
(2 + 3) * 4

10
0b10
0o10
0x10

# int()는 부동소수점수, 혹은 숫자로 이루어진 문자열을 정수로 반환한다.
int(True)
int(False)
int(98.6)
int(1.0e4)
int('99')
int('-23')
int('+12')
int(12345)

# 소수점이나 지수를 포함하는 문자열은 처리하지 않는다.
int('99 bottles of beer on the wall')   # error
int('98.6')   # error
int('1.0e4')   # error

# 만약 숫자의 타입을 섞어서 사용하면 파이썬은 자동으로 형변환을 한다.
4 + 7.0
True + 2
False + 5.0

# 파이썬의 int()는 아주 큰 공간을 가질 수 있다.
googol = 10**100
googol

# 부동소수점수
float(True)
float(False)
float(98)
float('99')
float('98.6')
float('-1.5')
float('1.0e4')


# 2.3 문자열
'Snap'
"Crackle"
# 인용부호가 포함된 문자열을 만들기 위해서 두개의 인용부호('', "")를 사용한다.
"'Nay,' said the naysayer."
'A "two by four" is actually 1 1/2 "* 3 1/2".'

# 세개의 단일 인용부호 혹은 세개의 이중 인용부호 사용가능!
'''BOOM!'''
"""Eek!"""
"""세개의 단일 인용부호는 위처럼 짧은 문자열보다는 대화식 인터프리터에서 
긴 문자열을 끝내지 않고 다음 줄로 넘기면서 입력할 때 용이하다. (이렇게)"""
poem = 'There was a young lady of Norway,
'
poem = '''There was a young lady of Norway,
'''
poem
print(poem)   # 둘의 차이 확인해볼 것 print()는 인용부호를 제거하고 호출한다.

bottles = 99
base = ''
base += 'current inventory : '
base += str(bottles)
base

# 데이터타입 변환:str()
str(98.6)
str(1.0e4)
str(True)
# 문자열이 아닌 객체를 print()로 호출할 때, 파이썬은 내부적으로 str()함수를 사용한다.

# 이스케이프 문자
# 문자앞에 백슬래시 기호(\)를 붙임으로써 특별한 의미를 줄 수 있다.
palindrome = 'A man, \nA plan, \nA canal:\nPanama. '
palindrome
print(palindrome)   # enter추가

print('\tabc')
print('a\tbc')   # tab추가

# 인용부호 표현 (\', \")
testimony = "\"I did nothing!\" he said. \"Not that either! Or the either thing.\""
print(testimony)
fact = "The world's largest rubber duck was 54'2\" by 65'7\" by 105'"
# 이중 인용부호 안에 이중 인용부호를 쓰기 때문에 표시를 해줘야합니다!
print(fact)

speech ='Today we honor our friend, the backslash: \\.'
print(speech)   # 백슬래시두번(\\)은 '백슬래시를 쓰겠다'

'Relese the kraken! ' + 'At once!'
"My word! " "A gentleman caller!"   # 리터럴 문자열은 다음과 같이 결합이 가능하다.

# 파이썬 문자열 결합과 달리 print()는 각 인자 사이에 공백을 붙인다. 그리고 마지막에는 줄바꿈 문자를 붙인다.
a = 'Duck.'
b = a
c = 'Grey Duck!'
a + b + c
print(a, b, c)

start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)

# 문자추출[]
letters = 'abcdefghijklmnopqrstucwxyz'
letters[0]
letters[1]
letters[-1]
letters[-2]

letters[100]
# 오프셋을 문자열의 길이 이상으로 지정하는 경우에는 다음과 같은 예외를 얻게 된다.
# IndexError: string index out of range

name = 'Henny'
name[0] = 'P'
# 문자열은 불변! 특정인덱스에 문자를 삽입하거나 변경할 수 없다.
# TypeError: 'str' object does not support item assignment
# 대신 아래와 같은 방법 사용가능
name = 'Henny'
name.replace('H', 'P')
'P' + name[1:]   # 이런 방법도 있다.

# 슬라이스: [start:end:step]
# 슬라이스를 활용하여 문자열의 일부를 추출할 수 있다.
# [:] 처음부터 끝까지 전체 시퀀스를 추출한다.
# [start:] start 오프셋부터 끝까지 시퀀스를 추출한다.
# [:end] 처음부터 (end - 1) 오프셋까지 시퀀스를 추출한다.
# [start:end] start 오프셋부터 (end - 1) 오프셋까지 시퀀스를 추출한다.
# [start:end:step] step만큼 문자를 건너뛰면서, start 오프셋부터 (end -1) 오프셋까지 시퀀스를 추출한다.

letters = 'abcdefghijklmnopqrstucwxyz'
letters[:]
letters[20:]
letters[10:]
letters[12:15]
letters[-3:]
letters[18:-3]
letters[-6:-2]
letters[::3]      # 처음부터 3스텝씩 건너뛰면서 문자를 추출한다.
letters[4:20:3]   # 4번째부터 19번째까지 3스텝씩 건너뛰면서 문자를 추출한다.
letters[19::4]    # 19번째부터 끝까지 4스텝씩 건너뛰면서 문자를 추출한다.
letters[:21:5]    # 처음부터 20번째까지 4스텝씩 건너뛰면서 문자를 추출한다.

# 편리한 파이썬의 슬라이스는 백스텝을 할 수 있다.
letters[::-1]
letters[-50:]   # 광범위하게 조사하는 방식, 실제 -50번째 오프셋은 없지만 그냥 가장 처음인 것부터 시작한다.
letters[-50]    # error
letters[-51:-50]
letters[:70]    # 광범위하게 조사, 위와 원리 같음
letters[70:71]

len(letters)
empty = ""
len(empty)
todos = 'get gloves,get mask,give cat vitamin,callambulance'
todos.split(',')   # 어떤 구분자를 기준으로 하나의 문자열을 작은 문자열들의 리스트로 나눈다.
todos.split()      # 구분자들을 지정하지 않으면 공백을 사용해 구분을 한다.

# join()함수는 문자열 list를 하나의 문자열로 결합한다. split()함수와 역행
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
', '.join(crypto_list)
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt'''
poem[:13]
len(poem)
poem.startswith('All')
poem.endswith('That\'s all, folks!')
word = 'the'
poem.find(word)   # 이 시에서 처음으로 the가 나오는 오프셋은?
poem.rfind(word)  # 이 시에서 마지막으로 the가 나오는 오프셋은?
poem.count(word)
poem.isalnum()    # 이 시는 글자와 숫자로만 이루어져 있는가?

setup = 'a duck goes into a bar...'
setup.strip('.')   # '.' 잘라내기
setup.capitalize()   # 첫번째 단어 대문자로 만들기
setup.title()        # 모든 단어의 첫글자를 대문자로 만들기
setup.upper()        # 모든 글자 대문자로 만들기
setup.lower()        # 모든 글자 소문자로 만들기
setup.swapcase()     # 대문자는 소문자로, 소문자는 대문자로 만들기
setup.center(30)     # 문자열을 지정한 공간에서 중앙에 배치하기
setup.ljust(30)      # 문자열을 지정한 공간에서 왼쪽에 배치하기
setup.rjust(30)      # 문자열을 지정한 공간에서 오른쪽에 배치하기

# 대체하기: replace()
setup.replace('duck', 'marmoset')
setup.replace('a ','a famous ', 100)   # 뒤의 100은 처음부터 100개까지 바꾸겠다는 뜻
setup.replace('a','a famous', 100)     # 이렇게 인용부호 안에 공간을 넣어주지 않으면 문자 중간에 들어가는 a도 바뀔 수 있으므로 조심

# 연습문제
seconds_per_hour = 60 * 60
seconds_per_day = seconds_per_hour * 24
seconds_per_day / seconds_per_hour    # 부동소수점 나눗셈
seconds_per_day // seconds_per_hour   # 정수 나눗셈
