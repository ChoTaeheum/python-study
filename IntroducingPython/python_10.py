# CHAPTER 10 시스템
# 10.1 파일
# 파이썬은 많은 다른 언어처럼 유닉스의 파일 연산 패턴을 지니고 있다. chown(), chmod() 함수 등은 똑같은 이름을 사용한다. 그리고 몇가지 새로운 함수가 존재한다.


# 10.1.1 생성하기: open()
# oops.txt파일을 생성해보자
fout = open('oops.txt', 'wt')   # 지정경로에 파일 생성
print('Oops, I created a file.', file=fout)
fout.close()

# 이제 몇가지 테스트를 수행해보자
# 10.1.2 존재여부 확인하기: exists()
# 파일 혹은 디렉토리가 실제로 존재하는지 확인하기 위해 exists()함수를 사용한다. 상대경로와 절대경로를 지정할 수 있다.
import os
os.path.exists('oops.txt')     # True
os.path.exists('./oops.txt')   # True
os.path.exists('waffle')       # False
os.path.exists('.')            # True
os.path.exists('..')           # True


# 10.1.3 타입확인하기: isfile()
# 이 절에 등장하는 세 함수(isfile, isdir, isabs)는 이름이 파일인지, 디렉토라인지, 또는 절대경로인지 확인한다.
# 먼저 isfile()함수를 사용하여 평범한 파일인지 간단한 질문을 던져본다.

name = 'oops.txt'
os.path.isfile(name)  # 이게 파일이냐?
os.path.isdir(name)  # 이게 디렉토리냐?
os.path.isdir('.')  # 하나의 점(.)은 현재 디렉토리를 나타내고, 두개의 점(..)은 부모(상위) 디렉토리를 나타낸다. 이들은 항상존재하기 때문에 True를 반환한다.

# os 모듈은 절대경로와 상대경로를 처리하는 많은 함수를 제공한다. isabs()함수는 인자가 절대경로인지 확인한다.
# 실제로 존재하는 파일이름을 인자에 넣지 않아도 된다.
os.path.isabs('name')   # False
os.path.isabs(name)     # False
os.path.isabs('/big/fake/name')   # True
os.path.isabs('big/fake/name')   # False


# 10.1.4 복사하기: copy()
# copy()함수는 shutil이라는 다른 모듈에 들어있다. 다음 예제는 oops.txt를 ohno.txt로 복사한다.
import shutil
shutil.copy('oops.txt', 'ohno.txt')
# shutil.move()함수는 파일을 복사한 후 원본파일을 삭제한다.(이동)


# 10.1.5 이름 바꾸기: rename()
# rename()은 말 그대로 파일 이름을 변경한다. 다음예제는 ohno.txt를 ohwell.txt로 이름을 바꾼다.
import os
os.rename('ohno.txt', 'ohwell.txt')


# 10.1.6 연결하기: link(), symlink()
# 유닉스에서 파일은 한 곳에 있지만, 링크(link)라 불리는 여러 이름을 가질 수 있다. 저수준의 하드링크에서 주어진 파일을 모두 찾는것은 쉬운 일이 아니다
# 심벌릭링크(symbolic link)는 원본파일을 새 이름으로 연결하여 원본파일과 새 이름의 파일을 한 번에 찾을 수 있도록 해준다.
# link()함수는 하드링크를 생성하고, symlink()함수는 심벌릭 링크를 생성한다. islink()함수는 파일이 심벌릭 링크인지 확인한다.
# oops.txt파일의 하드링크인 새 yikes.txt파일을 만들어보자
os.link('oops.txt', 'yikes.txt')
os.path.isfile('yikes.txt')   # True

# oops.txt파일의 심벌릭 링크인 새 jeepers.txt파일을 만들어보자
os.path.islink('yikes.txt')   # False, 심벌릭링크가 아니다.(그냥 링크)
os.symlink('oops.txt', 'jeepers.txt')
os.path.islink('jeepers.txt')


# 10.1.7 퍼미션 바꾸기: chmod()
# 유닉스 시스템에서 chmod()는 파일의 퍼미션(permission, 권한)을 변경한다. 사용자에 대한 읽기, 쓰기, 실행 퍼미션이 있다.
# 그리고, 사용자가 속한 그룹과 나머지에 대한 퍼미션이 각각 존재한다.
# 이 명령은 사용자, 그룹, 나머지 퍼미션을 묶어서 압축된 8진수의 값을 취한다. oops.txt를 이 파일의 소유자(파일을 생성한 사용자)만 읽을 수 있도록 만들어보자.
os.chmod('oops.txt', 0o400)

# 이러한 수수께끼같은 8진수 값을 사용하기보다는 (약간) 잘 알려지지 않은 아리송한 심벌을 사용하고 싶다면 stat모듈을 임포트하여 다음과 같이 쓸 수 있다.
import stat
os.chmod('oops.txt', stat.S_IRUSR)
### 설명이 약간 부족하니 더 찾아서 공부하시오!


# 10.1.8 오너십 바꾸기: chown()
# 이 함수는 유닉스/리눅스/맥에서 사용된다. 숫자로 된 사용자 아이디(uid)와 그룹 아이디(gid)를 지정하여 파일의 소유자와 그룹에 대한 오너십을 바꿀 수 있다.
uid = 5
gid = 22
os.chown('oops', uid, gid)   # AttributeError 뜨는데 파이썬 버전때문인듯함


# 10.1.9 절대 경로 얻기: abspath()
# 이 함수는 상대 경로를 절대 경로로 만들어준다. 만약 현재 디렉토리가 /usr/gaberlunzie고, oops.txt파일이 거기에 있다면, 다음과 같이 입력할 수 있다.
# 그러니까 쉽게 말하면 상대경로를 입력하면 절대경로를 출력해준다~ 이말임
os.path.abspath('oops.txt')


# 10.1.10 심벌릭링크 경로 얻기: realpath()
# 이전 절에서 oops.txt 파일의 심벌릭 링크인 jeepers.txt 파일을 만들었다. 다음과 같이 realpath()함수를 사용하여 jeepers.txt파일로부터
# 원본파일인 oops.txt 파일의 이름을 얻을 수 있다.
os.path.realpath('jeepers.txt')   # 'C:\\python\\source_code\\oops.txt'


# 삭제하기: remove()
# remove()함수를 사용하여 oops.txt파일과 작별인사를 나누자
os.remove('oops.txt')
os.path.exists('oops.txt')


# 10.2 디렉토리
# 대부분의 운영체제에서 파일은 디렉토리의 계층구조 안에 존재한다.(최근에는 폴더라고 부른다.)
# 이러한 모든 파일과 디렉터리의 컨테이너는 파일 시스템이다.(volume이라고도 한다.)
# 표준 os 모듈은 이러한 운영체제의 특성을 처리하고, 조작할 수 있는 함수를 제공한다.

# 10.2.1 생성하기: mkdir()
# 시를 저장할 poems 디렉토리를 생성한다.
os.mkdir('poems')
os.path.exists('poems')


# 10.2.2 삭제하기: rmdir()
os.rmdir('poems')
os.path.exists('poems')


# 10.2.3 콘텐츠 나열하기
# 다시 poems 디렉토리를 생성한다.
os.mkdir('poems')

# 그리고 이 디렉토리의 콘텐츠를 나열한다.(아직 아무것도 없음)
os.listdir('poems')

# 이제 하위 디렉토리를 생성한다.
os.mkdir('poems/mcintype')
os.listdir('poems')

# 하위 디렉토리에 파일을 생성한다.
fout = open('poems/mcintype/the_good_man', 'wt')
fout.write('''Cheerful and happy was his mood, 
He to the poor was kind and good,
And he oft' times did find them food.''')
fout.close()

# 드디어 파일이 생겼다. 디렉토리의 콘텐츠를 나열해보자
os.listdir('poems/mcintype')


# 10.2.4 현재 디렉토리 바꾸기: chdir()
# 이 함수를 이용하면 현재 디렉토리에서 다른 디렉토리로 이동할 수 있다. 즉, 현재 디렉토리를 바꿀 수 있다. 현재 디렉토리를 떠나서 poems디렉토리로 이동해보자
import os
os.chdir('poems')
os.listdir('.')


# 10.2.5 일치하는 파일 나열하기: glob()
# glob()함수는 복잡한 정규표현식이 아닌, 유닉스 쉘 규칙을 사용하여 일치하는 파일이나 디렉토리의 이름을 검색한다. 규칙은 다음과 같다.
# 1. 모든 것에 일치 : *(re모듈에서의 .*와 같다.)
# 2. 한 문자에 일치 : ?
# a,b, 혹은 c 문자에 일치 : [abc]
# a,b, 혹은 c를 제외한 문자에 일치 : [!abc]
# m으로 시작하는 모든 파일이나 디렉토리를 찾는다.
import glob
glob.glob('m*')

# 두 글자로 된 파일이나 디렉토리를 찾는다.
glob.glob('??')

# m으로 시작하고 e로 끝나는 여덟글자의 단어를 찾는다.
glob.glob('m??????e')

# k,l, 혹은 m으로 시작하고 e로 끝나는 단어를 찾는다.
glob.glob('[klm]*e')


# 10.4 달력과 시간
# 날짜는 다양한 형식으로 표현할 수 있다.
# 1. July 29 1984
# 2. 29 Jul 1984
# 3. 29/7/1984
# 4. 7/29/1984
# 윤년은 부딪히는 또 다른 문제이다. 매 100년마다 오는 해는 윤년이 아니고 매 400년마다 오는 해는 윤년이다.
# 윤년은 4년마다 오는데 100년째(25번째)는 윤년이 아니다가 400년째 되는 해는 윤년이 된다.
import calendar
calendar.isleap(1900)
calendar.isleap(1996)
calendar.isleap(1999)   # 윤년검사기

# 파이썬 표준 라이브러리는 datetime, time, calendar, dateutil 등 시간과 날짜에 관한 여러가지 모듈이 있다. 일부 중복되는 기능이 있어서 혼란스럽다.


# 10.4.1 datetime 모듈
# 이는 여러 메서드를 가진 4개의 주요 객체르르 정의한다.
# date: 년, 월, 일
# time: 시, 분, 초, 마이크로초
# datetime: 날짜와 시간
# timedelta: 날짜 와/또는 시간 간격
# 년, 월, 일을 지정하여 date 객체를 만들 수 있다. 이 값은 속성으로 접근할 수 있다.
from datetime import date
halloween = date(2015, 10, 31)
halloween      # datetime.date(2015, 10, 31)
halloween.day  # 31
halloween.month  # 10
halloween.year  # 2015
halloween.isoformat()   # 날짜 출력하는 메서드, ISO포맷(년, 월, 일)

# today() 메서드를 사용하여 오늘날짜 출력
from datetime import date
now = date.today()
now   # datetime.date(2017, 10, 26)

# timedelta 객체를 사용하여 날짜에 시간간격을 더해보자
from datetime import timedelta
one_day = timedelta(days=1)    # 날짜기간 정의하는 객체 (일, 초, 마이크로초, 밀리초, ... days 말고 별 쓸모 없음)
two_day = timedelta(2, 0, 10)  # delta, 변화량을 의미한다.
one_day
two_day
now + two_day
tomorrow = now + one_day
tomorrow
now + 17*one_day
yesterday = now - one_day
yesterday

# 날짜의 범위는 date.min(year=1, month=1, day=1)부터 date.max(year=9999, month=12, day=31)까지다. 결과적으로 역사적 혹은 천문학적인 날짜는 계산할 수 없다.
date.min   # datetime.date(1, 1, 1)
date.max   # datetime.date(9999, 12, 31)

# datetime 모듈의 time 객체는 하루의 시간을 나타내는데 사용된다.
from datetime import time   # timedelta의 시간버전
noon = time(12, 0, 0)
noon
noon.hour
noon.minute
noon.second
noon.microsecond
# 인자는 시hour부터 마이크로초microsecond 순으로 입력한다. 컴퓨터는 마이크로초를 정확하게 계산될 수 없다.

# datetime 객체는 날짜와 시간을 모두 포함한다. January 2, 2015, at 3:04 A.M 5초, 6마이크로초와 같이 한번에 생성된다.
from datetime import datetime
some_day = datetime(2015, 1, 2, 3, 4, 5, 6)

# datetime 객체에도 isoformat() 메서드가 있다.
some_day.isoformat()
# '2015-01-02T03:04:05.000006', 중간의 T는 날짜와 시간을 구분한다.

# datetime 객체에서 now() 메서드로 현재의 날짜와 시간을 얻을 수 있다.
from datetime import datetime
now = datetime.now()
now   # datetime.datetime(2017, 10, 26, 14, 24, 2, 724044)
now.year
now.month
now.day
now.hour
now.minute
now.second
now.microsecond

# combine()으로 date 객체와 time 객체를 datetime 객체로 병합할 수 있다.
from datetime import datetime, date, time
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
noon_today   # datetime.datetime(2017, 10, 26, 12, 0)

# datetime 객체에서 date()와 time() 메서드를 사용하여 날짜와 시간을 얻을 수 있다.
noon_today.date()
noon_today.time()


# 10.4.2 time 모듈
# 파이썬에서 datetime 모듈의 time 객체와 별도의 time 모듈이 혼란스럽다. 더군다나 time 모듈에는 time()이라는 함수가 있다.
# 절대시간을 나타내는 한가지 방법은 어떤 시작점 이후 시간의 초를 세는 것이다. 유닉스 시간은 1970년 1월 1일 자정 이후 시간의 초를 사용한다.
# 이 값을 epoch(에포치)라고 부르며, 에포치는 시스템 간에 날짜와 시간을 교환하는 아주 간단한 방식이다.
# time 모듈의 time() 함수는 현재시간을 에포치값으로 반환한다.
import time
now = time.time()
now

# ctime() 함수를 사용하여 에포치값을 문자열로 반환할 수 있다.
time.ctime(now)

# 또한 strftime()을 사용하여 날짜와 시간을 문자열로 변환할 수 있다. 이는 datetime, date, time 객체에서 메서드로 제공되고, time 모둘에서 함수로 제공된다.
# strftime()은 다음처럼 문자열의 출력포맷을 지정할 수 있다.
# 문자열포맷     날짜/시간 단위          범위
# %Y            년                  1900 ~ ...
# %m            월                  01 ~ 12
# %B            월 이름             January, ...
# %b            월 축약이름          Jan, ...
# %d            월의 일자           01 ~ 31
# %A            요일 이름            Sunday,
# %a            요일 축약이름         Sun, ...
# %H            24시간            00 ~ 23
# %I            12시간              01 ~ 12
# %p            오전/오후           AM, PM
# %M            분                 00 ~ 59
# %S            초                00 ~ 59
# 숫자는 자릿수에 맞춰 왼쪽에 0이 채워진다.
# 다음은 time 모듈에서 제공하는 strftime() 함수다. 이것은 struct_time 객체를 문자열로 변환한다. 먼저 포맷문자열 fmt를 정의하고, 이것을 다시 사용하자
import time
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
t
# time.struct_time(tm_year=2017, tm_mon=10, tm_mday=26, tm_hour=15, tm_min=26, tm_sec=51, tm_wday=3, tm_yday=299, tm_isdst=0)
time.strftime(fmt, t)
# "It's Thursday, October 26, 2017, local time 03:26:51PM" 와 이건 존트 놀랍다.

# 이것을 다음과 같이 date 객체에 사용하면 날짜부분만 작동한다. 그리고 시간은 기본값으로 지정된다.
from datetime import date
some_day = date(2015, 12, 12)
fmt = "It's %B %d, %Y, local time %I:%M:%S%p"
some_day.strftime(fmt)
# "It's December 12, 2015, local time 12:00:00AM", date를 제외한 나머지 요소는 디폴트 값으로

# time 객체는 시간부분만 변환된다.
from datetime import time
some_time = time(10, 35)
some_time.strftime(fmt)
# "It's January 01, 1900, local time 10:35:00AM", time을 제외한 나머지 요소는 디폴트값으로
# time 객체에서 날짜를 사용하는 것은 의미가 없다.

# 문자열을 날짜나 시간으로 변환하기 위해 같은 포맷 문자열로 strptime()을 사용한다.
# 정규표현식 패턴매칭은 없다. 문자열의 비형식부분(% 제외)이 정확히 일치해야한다. 2015-06-02와 같이 년-월-일이 일치하는 포캣을 지정해보자.
# 날짜 문자열에서 대시(-) 대신 공백을 사용하면 무슨일이 일어날까?
import time
fmt = "%Y-%m-%d"
time.strptime("2015 06 02", fmt)  # 예외출력, ValueError: time data '2015 06 02' does not match format '%Y-%m-%d'

# 대시(-)를 붙이면 어떻게 될까?
time.strptime("2015-06-02", fmt)
# time.struct_time(tm_year=2015, tm_mon=6, tm_mday=2, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=153, tm_isdst=-1)

# 값이 범위를 벗어나면 예외가 발생한다.
time.strptime("2015-13-02", fmt)  # 예외, ValueError: time data '2015-13-02' does not match format '%Y-%m-%d'

# 날짜를 여러 나라의 언어로 출력해보자
import locale
from datetime import date
halloween = date(2015, 10, 31)
for lang_country in ['ko_kr', 'en_us', 'fr_fr', 'de_de', 'es_es', 'is_is', ]:
    locale.setlocale(locale.LC_TIME, lang_country)
    halloween.strftime('%A, %B %d')
# locale.Error: unsupported locale setting, 예외발생, 해결요망

# lang_country에 대한 값은 어디서 찾을 수 있을까? 다음 예제를 실행하여 (몇 백 개의) 값을 모두 찾을 수 있다.
import locale
names = locale.locale_alias.keys()

# 이전 예제 setlocale()에서 사용한 두 글자의 언어코드, 언더크소어, 두글자의 국가 코드처럼 names로부터 로케일 이름을 얻어온다.
good_names = [name for name in names if len(name) == 5 and name[2] == '_']
good_names
good_names[:5]

# 모든 독일어로 로케일을 원한다면 다음과 같이 실행한다.
de = [name for name in good_names if name.startswith('de')]
de


# 10.4.4 대체모듈
# 표준 라이브러리 모듈이 헷갈리거나 특정 포맷변환이 부족하다고 생각되는 경우, 외부 모듈을 사용할 수 있다.
# arrow - 많은 날짜와 시간 함수를 결합하여 간단한 API를 제공한다.
# dateutil - 이 모듈은 날짜 포맷을 파싱하고, 상대적인 날짜와 시간에 대해서도 처리한다.
# iso8601 - ISO8601 포맷에 대한 표준 라이브러리의 부족한 부분을 보충한다.
# fleming - 이 모듈은 표준시간대 함수를 제공한다.\




































































