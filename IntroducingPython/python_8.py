# RAM(random access memory)는 아주 빠르지만 비싸고, 일정한 전력공급을 필요로 한다. 전원이 꺼질 경우 메모리에 있는 모든 데이터가 사라진다.
# 디스크드라이브는 램보다 느리지만 용량이 넉넉하고, 비용이 싸며, 전원이 꺼지더라도 데이터를 유지한다.
# 지금까지 컴퓨터 시스템 개발자들은 디스크와 램 사이의 격차를 줄이기 위해 상당한 노력을 기울였다. 프로그래머는 디스크와 같은 비휘발성 장치를 사용하여, 데이터를 저장하고 복구할 수 있는 지속성이 필요하다.


# 파일 입출력
# 데이터를 가장 간단하게 지속하려면 보통파일(flat file)을 사용한다. 파일은 단지 파일이름으로 저장된 바이트 시퀀스이다. 파일로부터 데이터를 읽어서 메모리에 적재하고,
# 메모리에서 파일로 데이터를 쓴다. 파이썬은 이러한 작업을 쉽게 할 수 있게 만든다. (유닉스를 모델로 만듦)
# 파일을 읽고 쓰기 전에 파일을 열어야한다!!!!!
# fileobj = open(filename, mode)
# 다음은 위 호출에 대한 간단한 설명이다.
    # fileobj는 open()에 의해 반환되는 파일 객체다.
    # filename는 파일의 문자열 이름이다.
    # mode는 파일타입과 파일로 무엇을 할지 명시하는 문자열이다.

# mode의 첫번째 글자는 작업을 명시한다.
# r : 파일읽기
# w : 파일쓰기(파일이 존재하지 않으면 파일을 생성하고 파일이 존재하면 덮어쓴다.)
# x : 파일쓰기(파일이 존재하지 않을 경우에만 해당한다.)
# a : 파일추가(파일이 존재하면 파일의 끝에서부터 쓴다.)

# mode의 두번째 글자는 파일타입을 명시한다.
# t(또는 아무것도 명시하지 않음) : 텍스트타입
# b : 이진타입

# 파일을 열고 다 사용했다면, 반드시 파일을 닫아야 한다.


# 8.1.1 텍스트파일 쓰기: write()
poem = '''There was a young lady named Bright,
... Whose speed was far faster than light;
... She started one day
... In a relative way,
... And returned on the previous night.'''
len(poem)

# poem을 relativity 파일에 쓴다.
fout = open('relativity', 'wt')
fout.write(poem)
fout.close()
# write() 함수는 파일에 쓴 바이트수를 반환한다. write() 함수는 print() 함수처럼 스페이스나 줄바꿈을 추가하지 않는다.
# 다음은 print() 함수로 텍스트파일을 만든예다.
fout = open('relativity', 'wt')
print(poem, file=fout)
fout.close()
# print()는 각 인자뒤에 스페이스를, 끝에 줄바꿈을 추가한다. 이전예제에서는 relativity 파일에 줄바꿈이 추가되었다.
# print()를 write()처럼 작동하려면 print()에 다음 두 인자를 전달한다.
# sep(구분자, 기본값은 스페이스다.)
# end(문자열끝, 기본값은 줄바꿈이다.)
# 빈 문자열을 두 인자에 전달
fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

# 파일에 쓸 문자열이 크면 특정단위(chunk)로 나누어서 파일에 쓴다.
fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk
fout.close()
# 처음에는 100문자를 썼고, 다음에는 50문자를 썼다.

# 만일 relativity 파일이 중요하다면, 모드 x를 사용하여 파일을 덮어쓰지 않도록 한다.
fout = open('relativity', 'xt')


# 8.1.2 텍스트파일 읽기: read(), readline(), readlines()
fin = open('relativity', 'rt')   # relativity 파일에 있는 내용을 (아까 위에서 poem 쓰기한거)
poem = fin.read()                # 여기서 읽어들여서 poem에 저장한다.
fin.close()
len(poem)

# 한번에 얼마만큼 읽을 것인지 크기를 제한할 수 있다. read()함수가 한번에 읽을 수 있는 문자수를 제한하려면 최대문자수를 인자로 입력한다.
poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)   # 파일을 다 읽어서 빈문자열을 반환하면 False가 된다.
    if not fragment:
        break
        poem += fragment
fin.close()
len(poem)

# 파일을 다 읽어서 끝에 도달하면, read() 함수는 빈 문자열('')을 반환한다. 이것은 if not fragment에서 fragment가 False가 되고,
# 결국 not False가 되어 while True 루프를 탈출한다.

# 또한 readline() 함수를 사용하여 파일을 라인 단위로 읽을 수 있다. 다음 예제는 파일의 각 라인을 poem문자열에 추가하여 원본파일의 문자열을 모두 저장한다.
poem = ''
fin = open('relativity', 'rt')   # 파일 여는 컴파일러?, 먼저 쓰는 과정을 거쳐야 읽을 수 있다.
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
len(poem)
# 텍스트 파일의 빈 라인의 길이는 1이고('\n'), 이것을 True로 인식한다. 파일의 읽기의 끝에 도달했을 때 (read()함수처럼) readline() 함수 또한 False로 간주하는 빈 문자열을 반환한다.

# 텍스트 파일을 가장 읽기 쉬운 방법은 이터레이터를 사용하는 것이다. 이터레이터는 한번에 한 라인씩 반환한다. 다음 예제는 이전과 비슷하지만, 코드양은 더 적다.
poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line
fin.close()
len(poem)
poem

# 앞의 모든 예제는 결국 하나의 poem문자열을 만들었다. readlines() 호출은 한번에 모든 라인을 읽고, 한 라인으로 된 문자열들의 리스트를 반환한다.
fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')


# 8.1.5 자동으로 파일 닫기
# 열려있는 파일을 닫지 않았을 때, 파이썬은 이 파일이 더 이상 참조되지 않다는 것을 확인한 뒤에 파일을 닫는다.
# 이것은 함수안에 파일을 열어놓고 이를 명시적으로 닫지 않더라도 함수가 끝날 때 자동으로 파일이 닫힌다는 것을 의미한다.
# 파이썬에는 파일을 여는 것과 같은 일을 수행하는 콘텍스트 매니저가 있다. 파일을 열 때 with 표현식 as 변수형식을 사용한다.
with open('relativity', 'wt') as fout:
    fout.write(poem)
# 콘텍스트 매니저 코드블록의 코드 한줄이 실행되고 나서 (잘 수행되거나, 또는 문제가 있는경우 예외발생) 자동으로 파일을 닫아준다.


# 파일 위치 찾기: seek()
# 파일을 읽고 쓸 때, 파이썬은 파일에서 위치를 추적한다. tell()함수는 파일의 시작으로부터의 현재 오프셋을 바이트 단위로 반환한다.
# seek()함수는 다른 바이트 오프셋으로 위치를 이동할 수 있다. 이 함수를 사용하면 마지막 바이트를 읽기 위해 처음부터 마지막까지 파일 전체를 읽지 않아도 된다.
# seek()함수로 파일의 마지막 바이트를 추적하여 마지막 바이트만 읽을 수 있다.
fin = open('relativity', 'rt')
fin.tell()

# seek()함수를 사용하여 파일의 마지막에서 1바이트 전 위치로 이동한다.
fin.seek(3)   # (이터레이터를 진행시켜주는 역할을 한다?)

tdata = fin.read()
len(tdata)
tdata[0]
tdata
poem

# seek()함수는 현재 오프셋을 반환한다.
# seek()함수의 형식은 seek(offset, origin)이며, 다음은 두번째 인자 origin에 대한 설명이다.
# origin이 0일 때(기본값), 시작위치에서 offset바이트 이동한다.
# origin이 1일 때, 현재의 위치에서 offset바이트 이동한다.
# origin이 2일 때, 마지막 위치에서 offset 바이트 전 위치로 이동한다.
# 또한 이 값은 표준 os에 정의 되어 있다.
import os
os.SEEK_SET
os.SEEK_CUR
os.SEEK_END

# 다른 방법으로 마지막 바이트를 읽어보자
fin = open('relativity', 'rt')

# 파일의 마지막에서 1바이트 전 위치로 이동한다.
fin.seek(3, 2)
fin.tell()

# 이제 파일의 마지막 바이트를 읽어보자
tdata = fin.read()
len(tdata)
tdata[0]


# 8.2 구조화된 텍스트 파일
# 간단한 텍스트 파일은 라인으로 구성되어 있다. 이 파일보다 더 구조화된 텍스트 파일을 써야할 때가 있다. 어떤 프로그램에서 데이터를 저장하거나 이를 다른 프로그램으로 보낼 때, 구조화된 데이터가 필요하다.
# 구조화된 텍스트 파일형식은 아주 많지만, 대표적으로 몇가지 형식을 살펴보자
# 1. 탭('\t'), 콤마(','), 수직 바('|')와 같은 문자를 구분자로 사용한다. 여기에서는 csv를 다룬다.
# 2. 프로그램 설정 파일과 같은 여러가지 형식을 사용한다.
# 이러한 구조화된 파일 형식은 적어도 하나의 파이썬 모듈로 읽고 쓸 수 있다.


# 8.2.1 csv
# 구분된 파일은 스프레드시트와 데이터베이스의 데이터교환 형식으로 자주 사용된다.
# 우리는 수동으로 csv파일을 한번에 한 라인씩 읽어서, 콤마로 구분된 필드를 분리할 수 있다. 그리고 그 결과를 리스트와 딕셔너리같은 자료구조에 넣을 수 있다.
# 하지만 파일 구문분석을 할때 생각보다 더 복잡할 수 있기 때문에 표준 csv모듈을 사용하는 것이 더 좋다.
# 1. 어떤 것은 콤마 대신 수직바('|')나 탭('\t')문자를 사용한다.
# 2. 어떤것은 이스케이프 시퀀스를 사용한다. 만일 필드 내에 구분자를 포함하고 있다면, 전체필드는 인용부호로 둘러싸여 있거나 일부 이스케이프 문자가 앞에 올 수 있다.
# 3. 파일은 운영체제에 따라 줄바꿈 문자가 다르다. 유닉스는 '\n', MS는 \r\n', 애플은 '\r'을 썼지만 현재는 '\n'을 사용한다.
# 4. 열 이름이 첫번째 라인에 올 수 있다.
# 먼저 리스트를 읽어서 csv형식의 파일을 작성해보자
import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld']
]

# 파일 생성
with open('villains', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

# 다시 파일 읽어본다.
import csv
with open('villains', 'rt') as fin:   # 콘텍스트 매니저
    cin = csv.reader(fin)
    villains = [row for row in cin]   # 리스트 컴프리헨션
print(villains)
# reader()함수를 사용하여 csv형식의 파일을 쉽게 읽을 수 있다. 이 함수는 for문에서 cin객체의 행을 추출할 수 있게 해준다.
# 기본값으로 reader()와 writer()함수를 사용하면, 열은 콤마로 나누어지고, 행은 줄바꿈 문자로 나누어진다.

# 리스트의 리스트가 아닌 딕셔너리의 리스트로 데이터를 만들 수 있다. 이번에는 DictReader()함수를 사용하여 열 이름을 지정한다.
import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]
print(villains)

# DictWriter()함수를 사용하여 csv 파일을 다시 써보자. 또한 csv파일의 첫라인에 열이름을 쓰기 위해 writeheader()함수를 호출한다.
import csv
villains = [
    {'first': 'Doctor', 'last':'No'},
    {'first': 'Rosa', 'last':'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blofeld'}
    ]
with open('villains', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

# 다시 파일을 읽어보자 DictReader() 호출에서 필드이름의 인자를 빼면, 첫번째 라인(first, last)의 값은 딕셔너리의 키로 사용된다.
import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]
print(villains)

# 솔직히 이해 잘 안가니까 나중에 다시 보세요~























































