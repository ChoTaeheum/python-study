# CHAPTER 7 데이터 주무르기
# 문자열 - 텍스트 데이터에 사용되는 유니코드 문자의 시퀀스
# 바이트와 바이트배열 - 이진 데이터에 사용되는 8비트 정수의 시퀀스

# 7.1 택스트 문자열
# 아스키 코드 - 7비트 사용(128개의 값), 26개의 대소문자, 숫자, 공백, 구두, 비인쇄 제어코드
# 유니코드 - 전세계 문자를 정의하기 위한 국제표준코드 113,021개의 문자를 정의

# 유니코드
# 4자리 - 16진수와 그 앞에 \u는 유니코드의 기본평면 256개 중 하나의 문자를 지정한다. 첫번째 두 숫자는 평면 번호이다.(00에서 FF)
#        다음의 두 숫자는 평면에 있는 문자의 인덱스다. 평면 00은 아스키코드고, 평면안의 문자위치는 아스키코드의 번호와 같다.

# lookup() - 대소문자를 구분하지 않는 인자를 취하고 유니코드 문자를 반환한다. 즉, 이름을 받아서 유니코드를 반환
# name() - 인자로 유니코드 문자를 취하고 대문자 이름을 반환한다. 이름!!!!!(ex."LATIN CAPITAL LETTER A")

import unicodedata

# 파이썬 유니코드 문자를 취하는 테스트 함수 작성
def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))   # 오 이거 좀 신기

unicode_test('A')

# 다음은 아스키부호를 넣어보자
unicode_test('$')

# 유니코드 통화문자
unicode_test('\u00a2')

# 딩벳글꼴의 스노우맨
unicode_test('\u2603')

# cafe 단어의 저장, 사용
place = 'café'
unicode_test('\u00e9')
unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE')

place = 'caf\u00e9'
place   # 'café'


# 문자열 len함수는 유니코드의 바이트가 아닌 문자수를 센다.
len("$")
len('\U0001f47b')

# UTF-8 인코딩과 디코딩
# 파이썬에서 일반문자열을 처리할 때는 각 유니코드 문자를 저장하는 방법에 대해 걱정하지 않아도 된다. 그러나 외부 데이터를 교환할 때는 다음 과정이 필요하다.
   # 문자열을 바이트로 인코딩
   # 바이트를 문자열로 디코딩

# 유니코드에 6,4000 미만의 문자가 있다면 2바이트로 된 각 유니코드 문자의 식별자를 저장할 수 있지만 불행하게도 문자가 더 많다.
# 유니코드 한 문자당 1~4바이트를 사용하게 설계했다.
# 1바이트 : 아스키코드
# 2바이트 : 키릴문자를 제외한 대부분의 파생된 라틴어
# 3바이트 : 기본 다국어 평면의 나머지
# 4바이트 : 아시아 언어 및 기호를 포함한 나머지

# 인코딩
# 문자열을 바이트로 인코딩해보자 encode() 함수의 첫번째 인자는 인코딩 이름이다.
# 'ascii' : 7비트의 아스키코드
# 'utf-8' : 8비트의 가변길이 인코딩 형식, 거의 대부분의 문자 지원
# 'cp-1252' : 윈도우 인코딩 형식

snowman = '\u2603'
snowman
ds = snowman.encode('utf-8')
ds   # b'\xe2\x98\x83'
len(ds)   # 3, snowman 유니코드 문자를 인코딩하기 위해 3바이트를 사용한다.

# 'utf-8' 이외의 다른 인코딩도 사용할 수 있다. 하지만 유니코드 문자열을 인코딩할 수 없다면 에러를 얻게된다.
# 예를들어, 아스키를 인코딩할 때 유니코드 문자가 유효한 아스키문자가 아닌 경우 실패한다.
ds = snowman.encode('ascii')


# 디코딩
# 외부소스(파일, 데이터베이스, 웹사이트, 네트워크 API 등)에서 텍스트를 얻을 때마다 그것은 바이트 문자열로 인코딩되어 있다.
# 이 소스를 실제로 사용된 인코딩을 알기 위해, 인코딩 과정을 거꾸로 하여 유니코드 문자열을 얻을 수 있다.
# 유니코드 문자열 생성
place = 'caf\u00e9'
place
type(place)

# 이것을 utf-8 형식의 place_bytes라는 바이트 변수로 인코딩한다.
place_bytes = place.encode('utf-8')
place_bytes
type(place_bytes)

# place_bytes는 5바이트로 되어있다. 첫 3바이트는 utf-8과 똑같이 표현되는 아스키문자다.
# 그리고 마지막 2바이트에서 'é'를 인코딩했다. 이제 바이트문자열을 유니코드문자열로 디코딩해보자
place2 = place_bytes.decode('utf-8')
place2

# 만약 utf-8로 인코딩한 후, utf-8이 아닌 다른 방식으로 디코딩하면 무슨일이 일어날까?
place3 = place_bytes.decode('ascii')
# 그러니까 유니코드로 인코딩한 바이트문자열은 유니코드로 디코딩해야 원하는 문자열을 얻을 수 있다.

# 참고사이트
# 유나코드 HOWTO
# 유니코드와 문자셋에 대한 기고글


# 7.1.2 포맷
# 이번절에서는 데이터값을 문자열에 끼워넣는 방법을 배운다. 다시 말해 다양한 포맷을 사용하여 문자열 안에 값을 넣는다.
# 포맷은 보고서와 그 외의 정리된 출력물을 만들기 위해 사용한다.
# 파이썬에는 옛스타일과 새로운 스타일의 포매팅문자열이 있다. 두 스타일은 파이썬 2와 3에서 지원한다.

# 옛스타일: %
# 문자열 포매팅의 옛스타일은 string % data 형식이다. 문자열안에 끼워 넣을 데이터를 표시하는 형식은 보간시퀀스다.
# %s : 문자열
# %d : 10진 정수
# %x : 16진 정수
# %o : 8진 정수
# %f : 10진 부동소수점수
# %e : 지수로 나타낸 부동소수점수
# %g : 지수로 나타낸 부동소수점수 혹은 10진 부동소수점수
# %% : 리터럴 %

# 다음은 정수에 대한 간단한 예이다.
'%s' % 42
'%d' % 42
'%x' % 42
'%o' % 42

# 다음은 부동소수점수에 대한 간단한 예
'%s' % 7.03
'%d' % 7.03
'%e' % 7.03
'%g' % 7.03

# 정수와 리터럴의 간단한 예
'%d%%' % 100

# 정수와 문자열에 대한 간단한 예
actor = 'Richard Gere'
cat = 'Chester'
weight = 28
"My wife's favorite actor is %s" % actor      # 그냥 입력
"Our cat %s weight %s pound" % (cat, weight)  # 튜플로 묶어서 입력
# 문자열 내의 %s는 다른 문자열을 끼워넣는 것을 의미한다. 문자열 안의 %s의 수는 %뒤의 데이터항목의 수와 일치해야한다.
# 심지어 weight는 정수임에도 문자열 안의 %s는 그것을 문자열로 반환한다.

n = 42
f = 7.03
s = 'string cheese'
'%d %f %s' % (n,f,s)
'%10d %10f %10s' % (n,f,s)
'%-10d %-10f %-10s' % (n,f,s)
'%10.4d %10.4f %10.4s' % (n,f,s)    # 이 설정은 문자열을 4만 남겨놓고 잘라내고, 소수점 이후의 숫자길이를 4로 제한한다.


# 새로운 스타일의 포매팅: {}와 format
# 파이썬3을 사용한다면 이것을 추천

'{} {} {}'.format(n,f,s)

# 아래와 같이 순서를 지정할 수도 있다.
'{2} {0} {1}'.format(n,f,s)

# 인자는 딕셔너리 혹은 이름을 지정한 인자가 될 수 있다. 그리고 지정자는 그들의 이름을 포함할 수 있다.
'{n} {f} {s}'.format(n=42, f=7.03, s='string cheese')

# 다음과 같이 세 값을 딕셔너리에 넣어보자
d = {'n':42, 'f':7.03, 's':'string cheese'}
# 다음 예제에서 {0}은 딕셔너리 전체인 반면 {1}은 딕셔너리 다음에 오는 문자열 'other'이다.
d[n]
'{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other')
# 이 예제들은 모두 기본포맷을 사용하여 인자를 출력했다.

# 옛스타일은 문자열 내의 % 다음에 타입지정자를 입력했다.(s,d,x와 같은)
# 그러나 새로운 스타일에서는 : 다음에 타입지정자를 입력한다. 먼저 위치인자를 살펴보자
'{0:d} {1:f} {2:s}'.format(n,f,s)

# 이번에는 같은 값을 사용하지만 인자에 이름을 지정한다.
'{n:d} {f:f} {s:s}'.format(n=42 ,f=7.03, s='string cheese')

# 다른옵션(최소필드길이, 최대문자길이, 정렬 등) 또한 지원한다.
'{0:10d} {1:10f} {2:10s}'.format(n,f,s)

# 이전 예제와 같으나, >기호는 오른쪽 정렬에 대해 더 명확하게 해준다.
'{0:>10d} {1:>10f} {2:>10s}'.format(n,f,s)

# 왼쪽 정렬해보자!
'{0:<10d} {1:<10f} {2:<10s}'.format(n,f,s)

# 최소필드길이가 10이고 중앙정렬해보자
'{0:^10d} {1:^10f} {2:^10s}'.format(n,f,s)

# 옛스타일에 있었던 최대문자수 기능은 없다.

# 마지막으로 문자를 채워넣어보자
'{0:!^20s}'.format('BIG SALE')



# 7.1.3 정규표현식
import re
result = re.match('You', 'Young Frankenstein')
# 'You'는 패턴이고, 'Young Frankenstein'은 확인하고자 하는 문자열 소스다. match()는 소스와 패턴의 일치여부를 확인한다.
result

youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')
# match()가 패턴과 소스를 비교하는 유일한 방법은 아니다. 다른 메서드를 살펴보자
# search()는 첫번째 일치하는 객체를 반환한다.
# findall()은 중첩에 상관없이 모두 일치하는 문자열 리스트를 반환한다.
# split()는 패턴에 맞게 소스를 쪼갠 후 문자열 조각의 리스트를 반환한다.
# sub()는 대체인자를 하나 더 받아서, 패턴과 일치하는 모든 소스 부분을 대체인자로 변경한다.

# 시작부터 일치하는 패턴찾기 : match()
# 'Young Frankenstein' 문자열은 'You'단어로 시작하는가? 여기에 그에 대한 코드와 코멘트가 있다.
source = 'Young Frankenstein'
m = re.match('You', source)   # match는 소스의 시작부터 패턴이 일치하는지 확인한다.
if m:    # match는 객체를 반환한다. 무엇이 일치하는지 보기 위해 다음작업을 수행한다.
    print(m.group())
# You

m = re.match('^You', source)   # 문자열이 You로 시작하는지 확인한다.
if m:
    print(m.group())
# You

# 'Frank'는 어떤가?
m = re.match('Frank', source)
if m:
    print(m.group())
# 아무것도 출력되지 않는다. 이번에는 match()가 아무것도 반환하지 않아서 print문이 실행되지 않았다.

# 이전에도 언급했듯이 match()는 패턴이 소스의 처음에 있는 경우에만 작동한다. 반면에 search()는 패턴이 아무데나 있어도 작동한다.
m = re.search('Frank', source)
if m:
    print(m.group())
# Frank


# 패턴을 바꿔보자
m = re.match('.*Frank', source)
if m:   # match는 객체를 반환한다.
    print(m.group())

# 다음은 바뀐 패턴에 대한 간단한 설명이다.
# .은 한 문자를 의미한다.
# *은 이전 패턴이 여러개 올 수 있다는 것을 의미한다. 그러므로 .*는 0회 이상의 문자가 올 수 있다는 것을 의미한다.
# Frank는 포함되어야 할 문구를 의미한다.
# match()는 .*Frank와 일치하는 문자열 'Young Frank'를 반환한다.

# 첫번째 일치하는 패턴 찾기: search()
# .*와일드카드 없이 'Young Frankenstein' 소스 문자열에서 'Frank' 패턴을 찾기 위해 search()를 사용할 수 있다.
m = re.search('Frank', source)
if m:    # search는 객체를 반환한다.
    print(m.group())
# Frank


# 일치하는 모든 패턴 찾기: findall()
# 이전 예제들은 매칭되는 패턴 하나만을 찾았다. 그렇다면 문자열에 'n'이 몇개 있는지 알 수 있을까?
m = re.findall('n', source)
m   # ['n', 'n', 'n', 'n'], findall은 찾은 개수만큼 들어있는 리스트를 반환한다.
len(m)   # 4

# 'n' 다음에 어떤 문자가 오는지 알아보자.
m = re.findall('n.', source)   # n 다음에 뭔가 하나라도 있는 것만
m
# 마지막 n은 위 패턴에 포함시키지 않는다. 'n' 이후의 문자는 선택적이 되도록 '?'를 추가한다.
# '.'은 하나의 문자를 의하고 '?'는 0또는 1회를 의미한다.
# 그러므로 .?는 하나의 문자가 0또는 1회 올 수 있다는 뜻이다.
m = re.findall('n.?', source)
m


# 패턴으로 나누기: split()
# 다음 예제에서는 간단한 문자열 대신 패턴으로 문자열을 리스트로 나눈다.(일반문자열에서 split() 메서드의 사용)
m = re.split('n', source)   #'n'을 기준으로 나눠라
m   # split은 리스트를 반환한다.
# ['You', 'g Fra', 'ke', 'stei', '']


# 일치하는 패턴 대체하기: sub()
# sub() 메서드는 문자열 replace() 메서드와 비슷하지만, 리터럴 문자열이 아닌 패턴을 사용한다.
m = re.sub('n', '?', source)
m  # sub는 문자열을 반환한다.
#   'You?g Fra?ke?stei?'


# 패턴: 특수문자
# 정규표현식은 아주 많은 문장부호를 사용한다.
# match(), search(), findall(), sub() 메서드에서 사용할 수 있는 정규표현식의 세부사항을 살펴보자. 이 메서드에서는 아래의 패턴을 적용할 수 있다.
# 리터럴은 모든 비특수문자와 일치한다.
# \n을 제외한 하나의 문자:.
# 0회 이상:*
# 0 또는 1회:?

# 특수문자
# \d 숫자
# \D 비숫자
# \w 알파벳문자 + 숫자
# \W 비알파벳문자
# \s 공백문자
# \S 비공백문자
# \b 단어경계(\w와 \W 또는 \W와 \w 사이의 경계)
# \B 비단어경계

# string 모듈은 테스트에 사용할 수 있는 문자열 상수가 미리 정의되어 있다. 알파벳 대/소문자, 숫자, 공백문자, 구두점을 포함한 100가지 아스키문자가 포함된
# printable을 사용해보자
import pprint
import string
printable = string.printable
len(printable)
printable
# '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

# printable에서 숫자는?
re.findall('\d', printable)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 숫자와 문자 언더스코어는?
re.findall('\w', printable)
'''
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']
'''

# 공백문자는?
re.findall('\s', printable)
# [' ', '\t', '\n', '\r', '\x0b', '\x0c']


# 패턴: 지정자
# 정규표현식에 패턴지정자를 사용할 수 있다.
# 여기서 expr은 표현식 expression을, prev는 이전토큰, next는 다음토큰을 의미한다.
# 패턴지정자
# abc             리터럴 abc
# (expr)          expr
# expr1|expr2     expr1 또는 expr2
# .               \n을 제외한 문자
# ^               소스 문자열의 시작
# $               소스문자열의 끝
# prev ?          0 또는 1회의 prev
# prev*           0 이상의 최대 prev
# prev*           0 이상의 최소 prev
# prev {m}        m회의 prev
# prev {m, n}     m에서 n회의 최대 prev
# prev {m, n}?    m에서 n회의 최소 prev
# [abc]           a 또는 b 또는 c(a|b|c와 같음)
# [^abc]          (a 또는 b 또는 c)가 아님
# prev (?=next)   뒤에 next가 오면 prev
# prev (?!next)   뒤에 next가 오지 않으면 prev
# (?<=next) next  뒤에 next가 오면 next
# (?<!next) next  뒤에 next가 오지 않으면 prev

# 패턴지정자에 대한 예제를 살펴보자. 먼저 소스 문자열을 정의한다.
source = '''I wish I may, I wish I might
... Have a dish of fish tonight.'''
# 소스에서 wish를 모두 찾는다.
re.findall('wish', source)
['wish', 'wish']

# 소스에서 wish 또는 fish를 모두 찾는다.
re.findall('wish|fish', source)
# ['wish', 'wish', 'fish'], wish 두개 fish 한개

# 소스가 wish로 시작하는지 찾는다.
re.findall('^wish', source)
# []

# 소스가 I wish로 시작하는지 찾는다.
re.findall('^I wish', source)
# ['I wish']

# 소스가 fish로 끝나는지 찾는다.
re.findall('fish$', source)
# []

# 소스가 fish tonight로 끝나는지 확인
re.findall('fish tonight.$', source)

# 문자 ^와 $는 앵커라고 부른다. ^는 검색문자열의 시작위치에, $는 검색 문자열의 마지막 위치에 고정한다. 그리고 .$는 가장 마지막에 있는 한 문자와 .을 매칭한다.
# 더 정확하게 하려면 문자 그대로 매칭하기 위해 .에 이스케이프 문자를 붙여야한다.
re.findall('fish tonight\.$', source)   # 사실 이거 이해 안감

# w 또는 f 다음에 ish가 오는 단어를 찾는다.
re.findall('[wf]ish', source)
# ['wish', 'wish', 'fish']

# w, s, h가 하나 이상인 단어를 찾는다.
re.findall('[wsh]+', source)
# ['w', 'sh', 'w', 'sh', 'h', 'sh', 'sh', 'h']

# ght 다음에 비알파벳 문자가 나오는 단어를 찾는다.
re.findall('ght\W', source)
# ['ght\n', 'ght.']

# wish 이전에 나오는 I를 찾는다.
re.findall('I (?=wish)', source)
# ['I ', 'I ']

# I 다음에 나오는 wish를 찾는다.
re.findall('(?<=I) wish', source)
# [' wish', ' wish']

# 정규표현식 패턴이 파이썬 문자열 규칙과 충돌하는 몇 가지 경우가 있다. 다음 패턴은 fish로 시작하는 단어를 찾아야 한다.
re.findall('/bfish', source)
# 그런데 위 코드는 왜 실행되지 않을까?  예를 들면 파이썬 문자열에서 \b는 백스페이스를 의미하지만, 정규표현식에서는 단어의 시작부분을 의미한다.
# 정규표현식의 패턴을 입력하기 전에 항상 문자 r(raw string)을 입력하라. 그러면 파이썬의 이스케이프 문자를 사용할 수 없게 되므로 실수로 이스케이프 문자를
# 사용하여 충돌이 일어나는 것을 피할 수 있게 된다.
re.findall(r'\bfish', source)


# 패턴: 매칭결과 지정하기
# match() 또는 search()를 사용할 때 모든 매칭은 m.group()과 같이 객체 m으로부터 결과를 반환한다. 만약 패턴을 괄호로 둘러싸는 경우,
# 매칭은 그 괄호만의 그룹으로 저장된다.
# 그리고 다음과 같이 m.groups()를 사용하여 그룹의 튜플을 출력한다.
m = re.search(r'(.dish\b).*(\bfish)', source)
m.group()
m.groups()









































































































































































