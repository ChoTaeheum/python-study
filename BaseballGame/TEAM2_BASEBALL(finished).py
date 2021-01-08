from tkinter import Frame, Canvas, Label, Button, LEFT, Tk, TOP
import random,re,time,csv
import ctypes

############# 기록을 저장할 경로 설정 ###################         #지은
##### 저장할 경로는 항상 새로운 경로일 것! ##########

### 메인 폴더 ###
filepath = "c:\\data\\"

### 실시간 선수 기록 저장 ####
save_player_path = "c:\\data\\baseball_save_player2.csv"

### 최종 경기 기록 저장 ###
save_result_path = "c:\\data\\baseball_save_result.csv"

############ 파일을  load할 경로 설정 ###################
##### load할 파일이 없으면 None 으로 설정! ###########

### 게임을 이어서 할 경우 실시간 경기 기록 불러오기 ###
load_player_path = "c:\\data\\baseball_save_player1.csv"

### 기록 분석을 위한 최종 경기 기록 데이터가 필요할 경우 ###
load_result_path = None

########################################################

#판정관련
#0 : 헛스윙
#0 : 파울
#1 : 단타
#2 : 2루타
#3 : 3루타
#4 : 홈런

###################################################################################################
## 기록 관련 클래스
###################################################################################################
class Record:
    def __init__(self):
        self.__hit = 0  # 안타 수
        self.__bob = 0  # 볼넷 수 융
        self.__homerun = 0  # 홈런 수
        self.__atbat = 0  # 타수
        self.__avg = 0.0  # 타율

    @property
    def hit(self):
        return self.__hit

    @hit.setter
    def hit(self, hit):
        self.__hit = hit

    @property
    def bob(self):
        return self.__bob

    @bob.setter
    def bob(self,bob):
        self.__bob = bob

    @property
    def homerun(self):
        return self.__homerun

    @homerun.setter
    def homerun(self, homerun):
        self.__homerun = homerun

    @property
    def atbat(self):
        return self.__atbat

    @atbat.setter
    def atbat(self, atbat):
        self.__atbat = atbat

    @property
    def avg(self):
        return self.__avg

    @avg.setter
    def avg(self, avg):
        self.__avg = avg

    # 타자 기록 관련 메서드
    def batter_record(self, hit, bob, homerun):
        self.hit += hit
        self.bob += bob
        self.homerun += homerun
        self.atbat += 1
        self.avg = self.hit / self.atbat

###################################################################################################
## 선수 관련 클래스
###################################################################################################
class Player:
    def __init__(self, team_name, number, name):
        self.__team_name = team_name  # 팀 이름
        self.__number = number  # 타순
        self.__name = name  # 이름
        self.__record = Record()  # 기록

    @property
    def team_name(self):
        return self.__team_name

    @property
    def number(self):
        return self.__number

    @property
    def name(self):
        return self.__name

    @property
    def record(self):
        return self.__record

    @property
    def player_info(self):
        return self.__team_name + ', ' + str(self.__number) + ', ' + self.__name

    # 선수 타율 관련 메서드
    def hit_and_run(self, hit, bob, homerun):
        self.__record.batter_record(hit, bob,homerun)


###################################################################################################
## 팀 관련 클래스
###################################################################################################
class Team:
    def __init__(self, team_name, players):
        self.__team_name = team_name  # 팀 이름
        self.__player_list = self.init_player(players)  # 해당 팀 소속 선수들 정보

    @property
    def team_name(self):
        return self.__team_name

    @property
    def player_list(self):
        return self.__player_list

    # 선수단 초기화
    def init_player(self, players):
        temp = []
        for player in players:
            number, name = list(player.items())[0]
            temp.append(Player(self.__team_name, number, name))
        return temp

    def show_players(self):
        for player in self.__player_list:
            print(player.player_info)

###################################################################################################
## 저장 및 불러오기 관련 클래스  -원주/지은
#####################################################################################################

class Saveandload:
    DATA_SET = 0
    CHECK = 0
    LOAD_YN = False
    @staticmethod
    def get_save_path():
        import os
        if not os.path.isdir(os.path.split(filepath)[0]):  # input받은 주소 중 현재 존재하지 않는 폴더를 input했다면, 즉 isdir이 not이라면.
            os.mkdir(os.path.split(filepath)[0])
        return filepath

    @staticmethod
    def make_data_set(cnt, game_info, adv, score, batter_number):
        '''
        :param player_info: 선수정보
        :param cnt: 스트라이크, 아웃, 볼 개수
        :param game_info: 등등..
        :param adv:
        :return:
        '''
        DATA_SET = []
        cnt = [str(data) for data in cnt] # S B O
        game_info = [str(data) for data in game_info] # 이닝, 체인지
        adv = [str(data) for data in adv] # 어드밴스
        score = [str(data) for data in score] # 점수
        batter_number = [str(data) for data in batter_number] # 배터 순서
        DATA_SET.append([game_info, adv, cnt, score, batter_number])
        # 따로 세이브 버튼 누르지 않고, 여기서 계속 데이터 저장
        Saveandload.save(DATA_SET)

    @staticmethod
    def save(DATA_SET):
        filepath = Saveandload.get_save_path()
        with open(filepath + "baseball_save_status.csv", "wt", encoding="utf-8") as f:
            for row in DATA_SET:
                for idx, value in enumerate(row, 1):
                    if idx == 1:
                        # print(value)
                        f.write(value[0] + '\n')
                        f.write(value[1] + '\n')
                    if idx == 2:
                        f.write(value[0] + "," + value[1] + "," + value[2] + '\n')
                    if idx == 3:
                        f.write(value[0] + "," + value[1] + "," + value[2] + '\n')
                    if idx == 4:
                        f.write(value[0] + "," + value[1] + '\n')
                    if idx == 5:
                        f.write(value[0] + "," + value[1] + '\n')

    @staticmethod
    def load():
        INNING = 0
        adv = 0
        CHANGE = 0
        STRIKE_CNT = 0  # 스트라이크 개수
        BALL_CNT = 0  # 볼 개수 융
        OUT_CNT = 0  # 아웃 개수
        SCORE = 0  # [home, away]
        BATTER_NUMBER = 0
        f = open(filepath + 'baseball_save_status.csv')
        reader = csv.reader(f, delimiter=',')
        for idx, line in enumerate(reader, 1):
            if idx == 1:
                INNING = int(line[0])
            elif idx == 2:
                CHANGE = int(line[0])

            elif idx == 3:
                adv = [int(i) for i in line]
            elif idx == 4:
                STRIKE_CNT = int(line[0])
                BALL_CNT = int(line[1])
                OUT_CNT = int(line[2])
            elif idx == 5:
                SCORE = [int(i) for i in line]
            else:
                BATTER_NUMBER = [int(i) for i in line]
        return [INNING, CHANGE, adv, STRIKE_CNT, BALL_CNT, OUT_CNT, SCORE, BATTER_NUMBER]

    @staticmethod
    def load_to_start_game():
        if Game.LOAD_CHK == True and Saveandload.LOAD_YN == True:
            temp = Saveandload.load()  # list
            # INNING = 0
            Game.INNING = temp[0]
            # CHANGE = 0  # 0 : hometeam, 1 : awayteam
            Game.CHANGE = temp[1]
            # ADVANCE = [0, 0, 0]  # 진루 상황
            Game.ADVANCE = temp[2]
            Game.STRIKE_CNT = temp[3]
            Game.BALL_CNT = temp[4]
            Game.OUT_CNT = temp[5]
            # SCORE = [0, 0]  # [home, away]
            Game.SCORE = temp[6]
            # BATTER_NUMBER = [1, 1]  # [home, away] 타자 순번
            Game.BATTER_NUMBER = temp[7]


    @staticmethod
    def load_chk():
        if Saveandload.LOAD_YN == False:
            Saveandload.LOAD_YN = True
            print('Load Finished')
        else:
            pass

    @staticmethod
    def save_record(save_path, *save_col):  # 지은
        csvFile = open(save_path, 'a')
        try:
            writer = csv.writer(csvFile)
            writer.writerow(save_col)
        finally:
            csvFile.close()

    @staticmethod
    def load_record(hometeam, home, away, load_path):  # 지은
        if Saveandload.LOAD_YN == True:
            try:
                if load_path == None:
                    print("불러올 파일이 없습니다. 새 게임을 시작합니다.")
                    return Main.start_game
                else:
                    # load한 csv파일을 records 리스트에 담기
                    records = [records for records in csv.reader(open(load_path, 'r')) if len(records) != 0]
                    # records 리스트를 선수별로 unpacking
                    for record in records:
                        curr_team = home if record[0] == hometeam else away
                        player_list = curr_team.player_list
                        player = player_list[int(record[1]) - 1]  # 선수를 순서대로 player에 할당
                        _, _, _, atbat, hit, bob, homerun, avg = record
                        player.record.atbat = int(atbat)
                        player.record.hit = int(hit)
                        player.record.bob = int(bob)
                        player.record.homerun = int(homerun)
                        player.record.avg = float(avg)
                    return Main.Loadgame

            except FileNotFoundError:
                print('파일 위치를 잘못 입력하셨습니다.')


###################################################################################################
## 게임 관련 클래스
###################################################################################################
class Game(object):
    TEAM_LIST = {
        '한화': ({1: '정근우'}, {2: '이용규'}, {3: '송광민'}, {4: '최진행'}, {5: '하주석'}, {6: '장민석'}, {7: '로사리오'}, {8: '이양기'}, {9: '최재훈'}),
        '롯데': ({1: '나경민'}, {2: '손아섭'}, {3: '최준석'}, {4: '이대호'}, {5: '강민호'}, {6: '김문호'}, {7: '정훈'}, {8: '번즈'}, {9: '신본기'}),
        '삼성': ({1: '박해민'}, {2: '강한울'}, {3: '구자욱'}, {4: '이승엽'}, {5: '이원석'}, {6: '조동찬'}, {7: '김헌곤'}, {8: '이지영'}, {9: '김정혁'}),
        'KIA': ({1: '버나디나'}, {2: '이명기'}, {3: '나지완'}, {4: '최형우'}, {5: '이범호'}, {6: '안치홍'}, {7: '서동욱'}, {8: '김민식'}, {9: '김선빈'}),
        'SK': ({1: '노수광'}, {2: '정진기'}, {3: '최정'}, {4: '김동엽'}, {5: '한동민'}, {6: '이재원'}, {7: '박정권'}, {8: '김성현'}, {9: '박승욱'}),
        'LG': ({1: '이형종'}, {2: '김용의'}, {3: '박용택'}, {4: '히메네스'}, {5: '오지환'}, {6: '양석환'}, {7: '임훈'}, {8: '정상호'}, {9: '손주인'}),
        '두산': ({1: '허경민'}, {2: '최주환'}, {3: '민병헌'}, {4: '김재환'}, {5: '에반스'}, {6: '양의지'}, {7: '김재호'}, {8: '신성현'}, {9: '정진호'}),
        '넥센': ({1: '이정후'}, {2: '김하성'}, {3: '서건창'}, {4: '윤석민'}, {5: '허정협'}, {6: '채태인'}, {7: '김민성'}, {8: '박정음'}, {9: '주효상'}),
        'KT': ({1: '심우준'}, {2: '정현'}, {3: '박경수'}, {4: '유한준'}, {5: '장성우'}, {6: '윤요섭'}, {7: '김사연'}, {8: '오태곤'}, {9: '김진곤'}),
        'NC': ({1: '김성욱'}, {2: '모창민'}, {3: '나성범'}, {4: '스크럭스'}, {5: '권희동'}, {6: '박석민'}, {7: '지석훈'}, {8: '김태군'}, {9: '이상호'})
    }

    INNING = 1  # 1 이닝부터 시작
    CHANGE = 0  # 0 : hometeam, 1 : awayteam
    STRIKE_CNT = 0  # 스트라이크 개수
    BALL_CNT = 0 #볼 개수 융
    OUT_CNT = 0  # 아웃 개수
    ADVANCE = [0, 0, 0]  # 진루 상황
    SCORE = [0, 0]  # [home, away]
    BATTER_NUMBER = [1, 1]  # [home, away] 타자 순번
    LOAD_CHK = True
    LOCATION = {0: [0, 0], 1: [0, 1], 2: [0, 2], 3: [0, 3], 4: [0, 4],
                5: [1, 0], 6: [1, 1], 7: [1, 2], 8: [1, 3], 9: [1, 4],
                10: [2, 0], 11: [2, 1], 12: [2, 2], 13: [2, 3], 14: [2, 4],
                15: [3, 0], 16: [3, 1], 17: [3, 2], 18: [3, 3], 19: [3, 4],
                20: [4, 0], 21: [4, 1], 22: [4, 2], 23: [4, 3], 24: [4, 4]
                } #던지는 위치의 좌표를 리스트로 저장.
    ANNOUNCE= ''

    def __init__(self, master, game_team_list):
        print('Home Team : ' + game_team_list[0]+' : ', Game.TEAM_LIST[game_team_list[0]])
        print('Away Team : ' + game_team_list[1]+' : ', Game.TEAM_LIST[game_team_list[1]])
        self.__hometeam = Team(game_team_list[0], Game.TEAM_LIST[game_team_list[0]])
        self.__awayteam = Team(game_team_list[1], Game.TEAM_LIST[game_team_list[1]])
        self.game_team_list = game_team_list
        self.root = master

    @property
    def hometeam(self):
        return self.__hometeam

    @property
    def awayteam(self):
        return self.__awayteam

    # 팀별 선수 기록 출력
    def show_record(self):
        print('===================================================================================================================')
        print('==  {} | {}  =='.format(self.hometeam.team_name.center(52, ' ') if re.search('[a-zA-Z]+', self.hometeam.team_name) is not None else self.hometeam.team_name.center(50, ' '),
                                        self.awayteam.team_name.center(52, ' ') if re.search('[a-zA-Z]+', self.awayteam.team_name) is not None else self.awayteam.team_name.center(50, ' ')))
        print('==  {} | {}  =='.format(('('+str(Game.SCORE[0])+')').center(52, ' '), ('('+str(Game.SCORE[1])+')').center(52, ' ')))
        print('===================================================================================================================')
        print('== {} | {} | {} | {} | {} | {} '.format('이름'.center(8, ' '), '타율'.center(5, ' '), '타석'.center(4, ' '), '안타'.center(3, ' '), '홈런'.center(3, ' '), '볼넷'.center(3, ' ')), end='')
        print('| {} | {} | {} | {} | {} | {} =='.format('이름'.center(8, ' '), '타율'.center(5, ' '), '타석'.center(4, ' '), '안타'.center(3, ' '), '홈런'.center(3, ' '), '볼넷'.center(3, ' ')))
        print('===================================================================================================================')

        hometeam_players = self.hometeam.player_list
        awayteam_players = self.awayteam.player_list

        for i in range(9):
            hp = hometeam_players[i]
            hp_rec = hp.record
            ap = awayteam_players[i]
            ap_rec = ap.record

            save_hp=[self.hometeam.team_name, hp.name, hp_rec.avg, hp_rec.atbat, hp_rec.hit, hp_rec.homerun, hp_rec.bob ] # 지은
            save_ap=[self.awayteam.team_name, ap.name, ap_rec.avg, ap_rec.atbat, ap_rec.hit, ap_rec.homerun, ap_rec.bob ] # 지은

            Saveandload.save_record(save_result_path, *save_hp)   # 지은
            Saveandload.save_record(save_result_path, *save_ap)   # 지은

            print('== {} | {} | {} | {} | {} | {} |'.format(hp.name.center(6+(4-len(hp.name)), ' '), str(hp_rec.avg).center(7, ' '),
                                                      str(hp_rec.atbat).center(6, ' '), str(hp_rec.hit).center(5, ' '), str(hp_rec.homerun).center(5, ' '), str(hp_rec.bob).center(5,' ')), end='')
            print(' {} | {} | {} | {} | {} | {} =='.format(ap.name.center(6+(4-len(ap.name)), ' '), str(ap_rec.avg).center(7, ' '),
                                                        str(ap_rec.atbat).center(6, ' '), str(ap_rec.hit).center(5, ' '), str(ap_rec.homerun).center(5, ' ') , str(ap_rec.bob).center(5, ' ')))
        print('===================================================================================================================')

    # 진루 및 득점 설정하는 메서드
    def advance_setting(self, hit_cnt, base_num, bob=False, double_play=False, sb=False):
        if hit_cnt == 4:  # 홈런인 경우
            Game.SCORE[Game.CHANGE] += (Game.ADVANCE.count(1)+1)
            Game.ADVANCE = [0, 0, 0]

        elif hit_cnt == -1:  # 태흠, 플라이볼일 경우
            pass

        elif double_play is True:   # 태흠
            for i in range(len(Game.ADVANCE), 0, -1):
                if Game.ADVANCE[i-1] == 1:
                    Game.ADVANCE[i-1] = 0
                    break
                    # 여기서 병살주자 비워주고 시작

            for i in range(len(Game.ADVANCE), 0, -1):   # 두명이 아웃 당했지만 다른 베이스에 있던 주자가 달릴 수 있기 때문에!!!!!!!!!!!!!!!!
                if Game.ADVANCE[i-1] == 1:
                    if (i + hit_cnt) > 3:  # 기존에 출루한 선수들 중 득점 가능한 선수들에 대한 진루 설정 예, 1루+3루타 / 2루+2루타 / 3루+1루타
                        Game.SCORE[Game.CHANGE] += 1  # 득점 해주고
                        Game.ADVANCE[i - 1] = 0  # 자리 다시 비워주고
                    else:  # 기존 출루한 선수들 중 득점권에 있지 않은 선수들에 대한 진루 설정
                        Game.ADVANCE[i - 1 + hit_cnt] = 1
                        Game.ADVANCE[i - 1] = 0

        else:
            if bob==False: #볼넷이 아닐때
                if sb == False:  # 볼넷도 아니고 도루도 아니고, hit_cnt만 필요함, 이 줄만 태흠
                    for i in range(len(Game.ADVANCE), 0, -1):
                        if Game.ADVANCE[i-1] == 1:
                            if (i + hit_cnt) > 3:  # 기존에 출루한 선수들 중 득점 가능한 선수들에 대한 진루 설정
                                Game.SCORE[Game.CHANGE] += 1
                                Game.ADVANCE[i-1] = 0
                            else:  # 기존 출루한 선수들 중 득점권에 있지 않은 선수들에 대한 진루 설정
                                Game.ADVANCE[i-1 + hit_cnt] = 1
                                Game.ADVANCE[i-1] = 0
                    Game.ADVANCE[hit_cnt-1] = 1  # 타석에 있던 선수에 대한 진루 설정

                elif sb == True:  # 도루인 경우
                    Game.ADVANCE[base_num - 1 + hit_cnt] = 1  # 진루상황 넣어주고
                    Game.ADVANCE[base_num - 1] = 0  # 서있던 곳 빼주고


            elif bob==True: #볼넷일때
                if Game.ADVANCE[0]==1: #1루에 주자가 있을때.
                    if Game.ADVANCE[1]==0 and Game.ADVANCE[2]==1:#1,3루 일때
                        Game.ADVANCE[1]=1
                    else: #그 외의 경우
                        for i in range(len(Game.ADVANCE), 0, -1):
                            if Game.ADVANCE[i-1] == 1:
                                if (i + hit_cnt) > 3:  # 기존에 출루한 선수들 중 득점 가능한 선수들에 대한 진루 설정
                                    Game.SCORE[Game.CHANGE] += 1
                                    Game.ADVANCE[i-1] = 0
                                else:  # 기존 출루한 선수들 중 득점권에 있지 않은 선수들에 대한 진루 설정
                                    Game.ADVANCE[i-1 + hit_cnt] = 1
                                    Game.ADVANCE[i-1] = 0
                        Game.ADVANCE[hit_cnt-1] = 1  # 타석에 있던 선수에 대한 진루 설정


                else: #1루에 주자가 없을때는 1루에만 주자를 채워 넣는다.
                    Game.ADVANCE[0] = 1

    # 컴퓨터가 생성한 랜덤 수와 플레이어가 입력한 숫자가 얼마나 맞는지 판단
    def hit_judgment(self, random_ball, hit_numbers): #(공던질위치, 구질) #융
        cnt = 0
        Foul = False
        Double_Play = False  # 태흠
        fly_ball = False  # 태흠
        UPDOWN = abs(Game.LOCATION[random_ball[1]][0] - Game.LOCATION[hit_numbers[1]][0]) #투수와 타자의 선택한 공 위치의 높낮이차이 #융
        L_OR_R = abs(Game.LOCATION[random_ball[1]][1] - Game.LOCATION[hit_numbers[1]][1]) #투수와 타자의 선택한 공 위치의 좌우차이 #융

        if random_ball[0] == hit_numbers[0]: #투수가 던진 공의 구질과 타자가 선택한 구질이 같을 때 #융
            if random_ball[1] == hit_numbers[1]:#위치가 같으니까 홈런 #융
                cnt += 4

            elif UPDOWN == 0:#높낮이가 같은 선상일 때 #융
                if L_OR_R == 1: #좌우로 1칸 차이 #융
                    Game.ANNOUNCE = '3루타~'
                    cnt += 3
                    if self.doble_play_OUT() is True:   # 태흠
                        Double_Play = True

                elif L_OR_R == 2: #좌우로 2칸 차이 #융
                    Game.ANNOUNCE = '2루타~'
                    cnt += 2
                    if self.doble_play_OUT() is True:   # 태흠
                        Double_Play = True

                elif L_OR_R >= 3: #좌우로 3칸 차이 #융
                    Game.ANNOUNCE = '1루타~'
                    cnt += 1
                    if self.doble_play_OUT() is True:   # 태흠
                        Double_Play = True

            elif UPDOWN == 1:#높낮이 차이가 하나일때 #융
                if L_OR_R ==1:
                    Game.ANNOUNCE = '2루타~'
                    cnt += 2
                    if self.doble_play_OUT() is True:   # 태흠
                        Double_Play = True

                elif L_OR_R ==2:
                    Game.ANNOUNCE = '1루타~'
                    cnt += 1
                    if self.doble_play_OUT() is True:   # 태흠
                        Double_Play = True

                elif L_OR_R >= 3:
                    Game.ANNOUNCE = '파울'
                    cnt += 0
                    Foul = True

            elif UPDOWN >= 2:#높낮이가 두개이상 차이날때 #융
                Game.ANNOUNCE = '헛스윙~!'
                cnt += 0

        else: #투수가 던진 공의 구질과 타자가 선택한 구질이 다를 때 융
            if random_ball[0] == hit_numbers[0]:#위치가 같지만 구질은 다르니 3루타 융
                cnt += 3
                if self.flyball_OUT() is True:   # 플라이볼 판정
                    cnt = -1   # 0이면 스트라이크 판정 나서 -1로 해줌

            elif UPDOWN == 0:#높낮이가 같은 선상일 때 #융
                if L_OR_R == 1:
                    Game.ANNOUNCE = '2루타~'
                    cnt += 2
                    if self.doble_play_OUT() is True:   # 태흠
                        Double_Play = True

                elif L_OR_R == 2:
                    Game.ANNOUNCE = '1루타~'
                    cnt += 1
                    if self.doble_play_OUT() is True:   # 태흠
                        Double_Play = True

                elif L_OR_R >= 3:
                    Game.ANNOUNCE = '파울 ㅜㅜ'
                    cnt += 0
                    Foul = True

            elif UPDOWN == 1:#높낮이 차이가 하나일때 융
                if L_OR_R ==1:
                    Game.ANNOUNCE = '1루타~'
                    cnt += 1
                    if self.doble_play_OUT() is True:   # 태흠
                        Double_Play = True

                elif L_OR_R ==2:
                    Game.ANNOUNCE = '파울ㅠㅠ'
                    cnt += 0
                    Foul = True

                elif L_OR_R >= 3:
                    Game.ANNOUNCE = '헛스윙'
                    cnt += 0

            elif UPDOWN >= 2:#높낮이가 두개이상 차이날때 융
                Game.ANNOUNCE = '헛스윙~!'
                cnt += 0

        return cnt, Foul, Double_Play, fly_ball

    def doble_play_OUT(self):   # 태흠
        self.r1 = random.random()
        if self.r1 < 0.33:
            return True
        return False

    def flyball_OUT(self):   # 태흠
        self.r2 = random.random()
        if self.r2 < 0.5:
            return True
        return False

    #선수가 입력한 숫자 확인  # 융
    def hit_number_check(self,hit_numbers): #구질(0~1),위치(0~24)가 들어옴 융
        if len(hit_numbers) == 2:
            if (hit_numbers[0] >= 0 and hit_numbers[0] <= 1) and (hit_numbers[1] >= 0 and hit_numbers[1] <= 24):
                return True
            else:
                return False

    # 선수 선택
    def select_player(self, number, player_list):
        for player in player_list:
            if number == player.number:
                return player

    # 랜덤으로 숫자 생성(1~20)
    def throws_numbers(self):
        while True:
            random_loc = random.randint(0, 24)  # 0 ~ 24 중에 랜덤 수를 출력
            random_ball= random.randint(0,  1)   # 구질
            return random_ball, random_loc

class Main(Game):
    HITORNOT = -1
    FORB = -1
    BALLLOC = -1

    def __init__(self, master, game_team_list):
        super().__init__(master,game_team_list)
        self.root = master
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)
        self.canvas = Canvas(self.frame, width=1000, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.frameb = Frame(self.frame)
        self.frameb.pack(fill="both", expand=True)

        self.hit = Button(self.frameb, text='타격하기(클릭 후 예상 구질 선택) ', width=5, height=2, command=self.Hitbutton, bg='orange', fg='black')
        self.hit.pack(fill="both", expand=False)

        self.nohit = Button(self.frameb, text='타격하지 않고 흘리기', width=5, height=2, command=self.Nohitbutton, bg='orange', fg='black')
        self.nohit.pack(fill="both", expand=False, side=TOP)

        self.stolen_base = Button(self.frameb, text='도루 명령하기(클릭 후 도루주자 선택!)', width=5, height=2, command=self.Stolenbasebutton, bg='orange', fg='black')
        self.stolen_base.pack(fill="both", expand=False, side=TOP)

        self.newgame = Button(self.frameb, text='New Game', height=4, command=self.start_game, bg='grey', fg='white')
        self.newgame.pack(fill="both", expand=True, side=LEFT)

        self.loadgame = Button(self.frameb, text='Load Game', height=4, command=self.Loadgame, bg='white', fg='black')
        self.loadgame.pack(fill="both", expand=True, side=LEFT)

        self.fastball = Button(self.frameb, text='직구', width=13, height=2, command=self.FastBall, bg='purple', fg='white')
        self.fastball.pack(fill="both", expand=False, side=TOP)

        self.breakingball = Button(self.frameb, text='변화구', width=13, height=2, command=self.BreakingBall, bg='purple', fg='white')
        self.breakingball.pack(fill="both", expand=False, side=TOP)

        self.base_choice1 = Button(self.frameb, text='1루주자 도루', width=13, height=2, command=self.Runner_choice1, bg='magenta', fg='white')
        self.base_choice1.pack(fill="both", expand=False, side=TOP)

        self.base_choice2 = Button(self.frameb, text='2루주자 도루', width=13, height=2, command=self.Runner_choice2, bg='magenta', fg='white')
        self.base_choice2.pack(fill="both", expand=False, side=TOP)

        self.canvas.bind("<ButtonPress-1>", self.Mouse_Action)   # 마우스를 누르는 행동
        self.color = ["white", "red"]
        self.ball_color=[]
        self.strike_color=[]
        self.out_color=[]
        self.board()
        self.base_num = 0  # 태흠

    def start_game(self):
        Saveandload.load_to_start_game()
        Saveandload.load_record(self.game_team_list[0], self.hometeam, self.awayteam, load_player_path) #지은
        Game.LOAD_CHK = False

        if Game.INNING <= 3: #게임을 진행할 이닝을 설정. 현재는 1이닝만 진행하게끔 되어 있음.
            Game.ANNOUNCE = '{} 이닝 {} 팀 공격 시작합니다.'.format(Game.INNING, self.hometeam.team_name if Game.CHANGE == 0 else self.awayteam.team_name)
            self.board()
            self.attack()

            if Game.CHANGE == 2:  # 이닝 교체
                Game.INNING += 1
                Game.CHANGE = 0
            self.start_game()
        else:
            Game.ANNOUNCE = '게임 종료!!!'
            self.show_record()

    def attack(self):
        curr_team = self.hometeam if Game.CHANGE == 0 else self.awayteam
        player_list = curr_team.player_list
        air_format = '\n' + '[{}] {}번 타자[{}] 타석에 들어섭니다.\n 현재 타석 : {}번 타자[{}], 타수 : {}, 타격 : {}, 볼넷 : {}, 홈런 : {},  타율 : {}'

        if Game.OUT_CNT < 3:
            player = self.select_player(Game.BATTER_NUMBER[Game.CHANGE], player_list)
            Game.ANNOUNCE += air_format.format(curr_team.team_name, player.number, player.name, player.number, player.name,  player.record.atbat, player.record.hit, player.record.bob, player.record.homerun,  player.record.avg,)
            self.board()

            while True:
                random_numbers = self.throws_numbers()  # 컴퓨터가 랜덤으로 숫자 2개 생성(구질[0](0~1), 던질위치[1](0~24))
                PLAYER_INFO = [curr_team.team_name, player.number, player.name, player.record.atbat, player.record.hit, player.record.bob,
                               player.record.homerun, player.record.avg]
                CNT = [Game.STRIKE_CNT, Game.BALL_CNT, Game.OUT_CNT]
                GAME_INFO = [Game.INNING, Game.CHANGE]
                ADV = Game.ADVANCE
                SCORE = Game.SCORE
                BATTER_NUMBER = Game.BATTER_NUMBER

                Saveandload.make_data_set(CNT, GAME_INFO, ADV, SCORE, BATTER_NUMBER)
                Saveandload.save_record(save_player_path, *PLAYER_INFO)  #지은

                Main.FORB = -1
                Main.BALLLOC = -1
                Main.HITORNOT = -1

                while True:
                    self.root.update()
                    if Main.HITORNOT != -1:
                        hit_yn = Main.HITORNOT
                        break

                    else:
                        time.sleep(0.05)
                        continue

                if hit_yn == 1 :#################타격 시############################ #융
                    while True :
                        self.root.update()
                        time.sleep(0.05)

                        if Main.FORB != -1 and Main.BALLLOC != -1 :
                            hit_numbers = [Main.FORB, Main.BALLLOC]
                            hit_cnt = self.hit_judgment(random_numbers, hit_numbers)  # 안타 판별  # cnt, Foul, Double_Play, fly_ball
                            break

                    if hit_cnt[0] == 0:  # strike !!!
                        if hit_cnt[1] == False:   # 파울이 아닐 때 융
                            Game.STRIKE_CNT += 1
                            Game.ANNOUNCE = '스트라이크!!!'
                            self.board()
                            if Game.STRIKE_CNT == 3:
                                Game.ANNOUNCE = '삼진 아웃!!!'
                                Game.STRIKE_CNT = 0
                                Game.OUT_CNT += 1
                                player.hit_and_run(0,0,0)
                                break


                        if hit_cnt[1] == True:#파울일 때
                            if Game.STRIKE_CNT <= 1: #스트라이크 카운트가 1 이하일때는 원래대로 진행 융
                                Game.STRIKE_CNT += 1
                                Game.ANNOUNCE = '파울!!!'
                                self.board()
                                if Game.STRIKE_CNT == 3:
                                    Game.ANNOUNCE = '삼진 아웃!!!'
                                    self.board()
                                    Game.STRIKE_CNT = 0
                                    Game.OUT_CNT += 1
                                    player.hit_and_run(0, 0, 0)
                                    break

                    else:
                        Game.STRIKE_CNT = 0
                        if hit_cnt[0] != 4:

                            if hit_cnt[0] == -1:   # 플라이볼일때, 태흠
                                Game.OUT_CNT += 1
                                Game.ANNOUNCE = '== ▣ 높게 뜬공! 그대로 외야수에 잡혀 아웃됩니다. \n'
                                player.hit_and_run(1 if hit_cnt[0] > 0 else 0, 0, 1 if hit_cnt[0] == 4 else 0)
                                self.advance_setting(hit_cnt[0], None, False, False, False)
                                self.board()
                                break

                            elif hit_cnt[2] == True and 1 in Game.ADVANCE:   # 출루인줄 알았지만 병살타ㅜ({}루타, 병살타 판단), 태흠
                                Game.STRIKE_CNT = 0
                                Game.BALL_CNT = 0
                                Game.OUT_CNT += 2
                                player.hit_and_run(1 if hit_cnt[0] > 0 else 0, 0, 1 if hit_cnt[0] == 4 else 0)  # 진루타, 볼넷, 홈런
                                Game.ANNOUNCE = ' 병살타!!! 아~ 이게 무슨일입니까!! \n'
                                self.advance_setting(hit_cnt[0], None, False, True, False)
                                self.board()
                                break

                            Game.ANNOUNCE = '{}루타!!!'.format(hit_cnt[0])
                            player.hit_and_run(1 if hit_cnt[0] > 0 else 0, 0, 1 if hit_cnt[0] == 4 else 0)
                            self.board()

                        else:   # 홈런일 때
                            Game.ANNOUNCE = '홈런!!!'
                            player.hit_and_run(1 if hit_cnt[0] > 0 else 0, 0, 1 if hit_cnt[0] == 4 else 0)
                            self.board()
                        self.advance_setting(hit_cnt[0], None, False, False, False)
                        break

                elif hit_yn == 0:######타격 안하고 지켜보기 시전########################### 융
                    #컴퓨터가 던진 공이 볼일때 융
                    if (random_numbers[1] >= 0 and random_numbers[1] <= 4) or (random_numbers[1] % 5 == 0) or (random_numbers[1] >= 20):
                        Game.BALL_CNT += 1
                        Game.ANNOUNCE = '볼 !!!!!!!!!!!!!!!!!!!!!!'
                        self.board()
                        if Game.BALL_CNT == 4:
                            Game.ANNOUNCE = '볼넷 1루출루 !!!!!!!!!!!!!!!!!!!!!! 투수가 정신을 못차리네요!'
                            self.advance_setting(1, None, True, False, False)
                            self.board()
                            Game.STRIKE_CNT = 0
                            Game.BALL_CNT = 0
                            player.hit_and_run(0,1,0)
                            break

                    #컴퓨터가 던진 공이 스트라이크 일 때 융
                    if random_numbers[1] in [6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]:
                        Game.STRIKE_CNT += 1
                        Game.ANNOUNCE = '스트라이크!!!!!!!!!!!!!'
                        self.board()
                        if Game.STRIKE_CNT == 3:
                            Game.ANNOUNCE = '방망이도 못 휘두르고 삼진!!!!!!!!!!!!!! 제구력이 훌륭하군요!'
                            Game.STRIKE_CNT = 0
                            Game.BALL_CNT = 0
                            Game.OUT_CNT += 1
                            player.hit_and_run(0, 0, 0)
                            self.board()
                            break

                elif hit_yn == 2:  # 도루선택, 태흠
                    self.root.update()
                    if Game.ADVANCE in [[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]]:
                        Game.ANNOUNCE = '====================================================================================================\n' \
                                        '★★★★★★★★도루 가능한 주자가 없습니다.★★★★★★★★'
                        self.board()
                        self.attack()

                    else:     # 태흠~
                        rn = random.random()
                        self.base_num = 0
                        while 1:
                            self.root.update()
                            if self.base_num == 0:
                                Game.ANNOUNCE = '도루시킬 주자를 선택하세요[1, 2] : {} || {}'.format(
                                    '1루주자' if Game.ADVANCE[0] == 1 and Game.ADVANCE[1] == 0 else '도루 불가',
                                    '2루주자' if Game.ADVANCE[1] == 1 and Game.ADVANCE[2] == 0 else '도루 불가')
                                self.board()

                            elif Game.ADVANCE[self.base_num - 1] == 1 and Game.ADVANCE[self.base_num] == 0:
                                self.board()
                                break  # 조건 충족하면 while 1에서 나가준다. 다음 if절 실행하기 위해서!!!

                            else:
                                Game.ANNOUNCE = '도루 불가라고 난독증이냐? 다시선택해!!!!' + '도루시킬 주자를 선택하세요[1, 2] : {} || {}'.format(
                                    '1루주자' if Game.ADVANCE[0] == 1 and Game.ADVANCE[1] == 0 else '도루 불가',
                                    '2루주자' if Game.ADVANCE[1] == 1 and Game.ADVANCE[2] == 0 else '도루 불가')
                                self.board()
                                continue

                        if rn < 0.3:  # 도루 성공확률, 태흠
                            self.advance_setting(1, self.base_num, False, False, True)
                            # print('도루성공, 게임창을 확인해주세용~')
                            Game.ANNOUNCE = '도루성공, Stolen Base'
                            self.board()
                            time.sleep(0.7)
                            break

                        else:  # 도루 실패할 경우, 태흠
                            Game.ANNOUNCE = '도루실패, Caught Stealing - 아웃!!!!!'
                            self.board()
                            Game.OUT_CNT += 1
                            Game.ADVANCE[self.base_num - 1] = 0
                            break      # ~태흠

                else :
                    continue

            PLAYER_INFO = [curr_team.team_name, player.number, player.name, player.record.atbat, player.record.hit, player.record.bob,
                           player.record.homerun, player.record.avg]
            Saveandload.save_record(save_player_path, *PLAYER_INFO)  # 지은


            if Game.BATTER_NUMBER[Game.CHANGE] == 9:
                Game.BATTER_NUMBER[Game.CHANGE] = 1
            else:
                Game.BATTER_NUMBER[Game.CHANGE] += 1
            self.attack()

        else:# OUT_CNT가 3이 되었을 때
            Game.CHANGE += 1
            Game.STRIKE_CNT = 0
            Game.BALL_CNT = 0
            Game.OUT_CNT = 0
            Game.ADVANCE = [0, 0, 0]
            self.board()

    def Loadgame(self):
        Saveandload.load_chk()
        self.start_game()

    def state_color(self, CNT1, CNT2, color1, color2="white"):        #지은
        col1 = [color1 for i in range(CNT2)]
        col2 = [color2 for i in range(CNT1-CNT2)]   # CNT1: 색깔 표시 개수 ["white","white","white"]
        column = col1 + col2                        # CNT2: 게임 진행 상태  self.game.BALL_CNT : 0
        return column

    def board(self):
        hometeam = self.hometeam.team_name
        awayteam = self.awayteam.team_name

        homescore = self.SCORE[0]
        awayscore = self.SCORE[1]
        announce = self.ANNOUNCE
        inning = self.INNING
        change = self.CHANGE
        attackordefence = [["공격", "수비"] if change == 0 else ["수비", "공격"]]
        scoreformat = '{} : {}  ({}) | {}이닝 | ({})  {} : {}'

        self.ball_color = self.state_color(3, self.BALL_CNT, "orange")    #지은
        self.strike_color = self.state_color(2, self.STRIKE_CNT, "blue")
        self.out_color = self.state_color(2, self.OUT_CNT, "red")

        self.canvas.create_rectangle(500, 0, 1000, 600, outline="black")
        self.canvas.create_rectangle(500, 0, 1000, 100, outline="black")
        self.canvas.create_rectangle(600, 600, 700, 0, outline="black")
        self.canvas.create_rectangle(500, 100, 1000, 200, outline="black")
        # ---------스트라이크존------#
        self.canvas.create_rectangle(600, 200, 1100, 500, fill="yellow")
        # ----------스트라이크존------#
        self.canvas.create_rectangle(700, 600, 800, 0, outline="black")
        self.canvas.create_rectangle(500, 200, 1000, 300, outline="black")
        self.canvas.create_rectangle(800, 600, 900, 0, outline="black")
        self.canvas.create_rectangle(500, 300, 1000, 400, outline="black")
        self.canvas.create_rectangle(900, 600, 1000, 0, outline="black")
        self.canvas.create_rectangle(500, 400, 1000, 500, outline="black")
        self.canvas.create_rectangle(500, 600, 1000, 600, outline="black")

        self.canvas.create_rectangle(0, 100, 480, 600, fill="green")  # 좌상우하

        self.canvas.create_rectangle(220, 300, 260, 340, fill="white")
        # 진루 선
        self.canvas.create_line(240, 135, 35, 330, width=4, fill="white")
        self.canvas.create_line(240, 135, 445, 330, width=4, fill="white")
        self.canvas.create_line(40, 330, 240, 515, width=4, fill="white")
        self.canvas.create_line(445, 330, 240, 515, width=4, fill="white")
        self.canvas.create_oval(430, 315, 460, 345, fill=self.color[self.ADVANCE[0]])  # 1루
        self.canvas.create_oval(225, 120, 255, 150, fill=self.color[self.ADVANCE[1]])  # 2루
        self.canvas.create_oval(20, 315, 50, 345, fill=self.color[self.ADVANCE[2]])  # 3루

        self.canvas.create_oval(225, 500, 255, 530, fill="white")  # 홈베이스

        self.canvas.create_text(350, 490, font=("Courier", 12), text="B")
        self.canvas.create_oval(370, 480, 390, 500, fill=self.ball_color[0])#볼
        self.canvas.create_oval(405, 480, 425, 500, fill=self.ball_color[1])#볼
        self.canvas.create_oval(440, 480, 460, 500, fill=self.ball_color[2])#볼
        self.canvas.create_text(350, 525, font=("Courier", 12), text="S")
        self.canvas.create_oval(370, 515, 390, 535, fill=self.strike_color[0])  #스트라이크
        self.canvas.create_oval(405, 515, 425, 535, fill=self.strike_color[1])  # 스트라이크
        self.canvas.create_text(350, 560, font=("Courier", 12), text="O")
        self.canvas.create_oval(370, 550, 390, 570, fill=self.out_color[0])  # 아웃
        self.canvas.create_oval(405, 550, 425, 570, fill=self.out_color[1])  # 아웃

        self.label = Label(self.frame, text=scoreformat.format(hometeam, homescore, attackordefence[0][0], inning, attackordefence[0][1], awayscore, awayteam), height=6, bg='white', fg='black')
        self.label.config(font=("Courier", 20))
        self.label.pack(fill="both", expand=True)
        self.label.place(x=0, y=0, width=1000, height=38, bordermode='outside')
        self.label = Label(self.frame, text=announce, height=6, bg='white', fg='black')
        self.label.config(font=("Courier", 10))
        self.label.pack(fill="both", expand=True)
        self.label.place(x=0, y=30, width=1000, height=70, bordermode='outside')

    def Mouse_Action(self,event):
        loclist = [[5 * i + j for j in range(5)] for i in range(5)]
        for k in range(500, 1000, 100):
            for j in range(100, 600, 100):
                if event.x in range(k, k + 100) and event.y in range(j, j + 100):
                    X1 = int((k - 500) / 100)
                    Y1 = int((j - 100) / 100)
                    Main.BALLLOC = loclist[Y1][X1]

        if event.x in range(425, 465) and event.y in range(310, 350):
            self.base_num = 1
        elif event.x in range(220, 260) and event.y in range(115, 155):
            self.base_num = 2

    def Hitbutton(self):
        Main.HITORNOT = 1

    def Nohitbutton(self):
        Main.HITORNOT = 0

    def Stolenbasebutton(self):
        Main.HITORNOT = 2

    def Runner_choice1(self):
        self.base_num = 1

    def Runner_choice2(self):
        self.base_num = 2

    def FastBall(self):
        Main.FORB = 1

    def BreakingBall(self):
        Main.FORB = 0

if __name__ == '__main__':
    while True:
        try:
            game_team_list = []
            print('====================================================================================================')
            print('한화 / ', '롯데 / ', '삼성 / ', 'KIA / ', 'SK / ', 'LG / ', '두산 / ', '넥센 / ', 'KT / ', 'NC / ')
            game_team_list = input('=> 게임을 진행할 두 팀을 입력하세요 : ').split(' ')
            print('====================================================================================================')
            if (game_team_list[0] in Game.TEAM_LIST) and (game_team_list[1] in Game.TEAM_LIST):
                print('게임이 시작되었습니다. 작업표시줄에 실행된 게임콘솔창을 확인해주세요~\n')
                break
            else:
                ctypes.windll.user32.MessageBoxW(None, '팀명을 잘못 입력하셨습니다.', "Error", 0)
        except:
            ctypes.windll.user32.MessageBoxW(None, '팀명을 잘못 입력하셨습니다.', "Error", 0)

    root = Tk()
    app = Main(root, game_team_list)
    root.mainloop()