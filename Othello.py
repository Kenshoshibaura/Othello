# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd
import FunctionModules as fm
import datetime
import os
import Algorithm
from joblib import Parallel, delayed

columnList = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
rowList = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
Inv_columnList = {v:k for k, v in columnList.items()}
Inv_rowList = {v:k for k, v in rowList.items()}

def search_enable_first(next_dia_all,turn):
    next_posi_enable = []
    for i in range(0,8):
        for j in range(0,8):
            if next_dia_all[i,j] == turn + 4:
                next_posi_enable.append(str(Inv_columnList[j])+str(Inv_rowList[i]))
    #print("指すことの可能な手は次の通りです:"+str(next_posi_enable))
    if not next_posi_enable:
        print("ERROR:pass")
        next_posi_enable.append('pass')
    return next_posi_enable

def show_enable(diagrams, next_dia_all, next_diaList, turn):
    next_posi_enable = search_enable_first(next_dia_all,turn)
    print(next_posi_enable)

def reevaluation():
    #print("---対局後の評価値更新処理を開始します---")
    path = 'log/'
    files = []
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path,filename)):
            if (".csv" in filename) is True:
                files.append(filename)
    #print("使用するlogファイルは次の通りです"+str(files))
    for i,file in enumerate(files):
        with open(path+file, mode='r')as f:
            #print(str(file)+"の対局を評価します")
            count_a = 0
            for line in f:
                data = line[:-1].split(',')
                if data[0] == "対局ID":
                    continue
                winner = data[9]
                count_a=count_a+1
            #print("この対局は"+str(count_a)+"手で"+str(winner)+"が勝利しました")
        with open(path+file, mode='r')as f:
            for line in f:
                data = line[:-1].split(',')
                if data[0] == "対局ID":
                    continue
                turn=str(data[2])
                if data[int(turn)+6] == "2":
                    atoh = []
                    for j in range(1,9):
                        for k in range(1,9):
                            atoh.append(str(int(float(data[k*8+j+1]))))
                    board = ''.join(atoh)
                    #print(str(board)+"から")
                    if int(turn) == 1:
                        en_turn = 2
                    elif int(turn) == 2:
                        en_turn = 1
                    else:
                        print("ERROR:AFTER TURN")
                        pass
                    hand=str(data[3])
                    #print("stone("+str(int(data[turn+4]))+","+str(int(data[en_turn+4]))+")")
                    #stone = int(float(str(data[turn+4]))) - int(float(str(data[en_turn+4])))
                    file_search = "brain/" + str(turn) + "/" + str(board) + ".csv"
                    if (os.path.exists(file_search)) == False:
                        print("No such file")
                        break
                    with open(file_search)as y:
                        for line_brain in y:
                            brain_data = line_brain[:-1].split(',')
                            if str(hand) == str(brain_data[0]):
                                score_board = str(brain_data[1])
                                score_match = str(brain_data[2])
                        if str(turn) == str(winner):
                            score_match_after = int(score_match) + 3
                        else:
                            score_match_after = int(score_match) - 3
                        score_match_after += 0 #stone?
                        before_line = str(hand) + "," + str(score_board) + "," + str(score_match) + "\n"
                        after_line = str(hand) + "," + str(score_board) + "," + str(score_match_after) + "\n"
                    with open(file_search)as y:
                        before_data = y.read()
                    #print("更新前のデータは次の通りです:\n"+str(before_data))
                    after_data = before_data.replace(before_line,after_line)
                    with open(file_search,mode="w")as y:
                        y.write(after_data)
                    #print("更新後のデータは次の通りです:\n"+str(after_data))
        #print(str(file)+"を削除します")
        os.remove(path+file)

class Othello:

    columnArray = np.array(['a','b','c','d','e','f','g','h'])
    rowArray = np.array(['1','2','3','4','5','6','7','8']).transpose()
    condition = {'1':'人間',
                 '2':'CPU(実戦)',
                 '3':'CPU(乱数)',
                 '4':'CPU(最大)'}
    columnList = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    rowList = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
    Inv_columnList = {v:k for k, v in columnList.items()}
    Inv_rowList = {v:k for k, v in rowList.items()}
    win = [0,0]

    def __init__(self,
                 interactive=True,
                 con_fir=None,
                 con_sec=None,
                 alg_fir=None,
                 alg_sec=None,
                 vs_count=None,
                 n_jobs=1,
                 folder='log',
                 ):

        self.interactive = interactive
        self.con_fir = con_fir
        self.con_sec = con_sec
        self.alg_fir = alg_fir
        self.alg_sec = alg_sec
        self.vs_count = vs_count
        self.n_jobs = n_jobs
        self.folder = folder

        if not os.path.isdir(self.folder):
            os.mkdir(self.folder)

    def condition_init(self):

        if self.interactive == True:
            #対局条件設定
            print("対局条件を入力してください。")
            print("先攻 1：人間　2：CPU(実戦)　3：CPU(乱数)　3：CPU(最大)")
            print('  ---------------------------------')
            self.con_fir = int(input())
            if self.con_fir == 2:
                self.alg_fir = Algorithm.AI_choice()
            elif self.con_fir == 3:
                self.alg_fir = Algorithm.random_choice()
            elif self.con_fir == 4:
                self.alg_fir = Algorithm.max_choice()
            print("後攻 1：人間　2：CPU(実戦)　3：CPU(乱数)　3：CPU(最大)")
            print('  ---------------------------------')
            self.con_sec = int(input())
            if self.con_sec == 2:
                self.alg_sec = Algorithm.AI_choice()
            elif self.con_sec == 3:
                self.alg_sec = Algorithm.random_choice()
            elif self.con_sec == 4:
                self.alg_sec = Algorithm.max_choice()
            if self.con_fir > 1 and self.con_sec > 1:
                print("対局回数を入力してください。")
                print('  ---------------------------------')
                self.vs_count = int(input())
            else:
                self.vs_count = 1
            print(self.condition[str(self.con_fir)] + " VS " + self.condition[str(self.con_sec)] + " でゲームを始めます")

    def diagrams_init(self):

        self.diagrams = np.zeros((8,8,100))
        self.diagrams[3,3,0] = 1
        self.diagrams[3,4,0] = 2
        self.diagrams[4,3,0] = 2
        self.diagrams[4,4,0] = 1
        self.gameset = False
        self.turnPlayer = 1
        self.tempo = 0
        self.passtempo = False
        self.ID = datetime.datetime.today().strftime("%Y_%m_%d_%H_%M_%S_%f")
        self.log = pd.read_csv('logformat.csv')

    def one_game(self):

        self.diagrams_init()

        #対局部分
        while(self.gameset == False):
            #状況表示
            if self.vs_count == 1:
                fm.show_position(self.columnArray, self.rowArray, self.diagrams[:,:,self.tempo])
            #print("NA-1\n"+str(self.diagrams[:,:,self.tempo])+"NA-2\n"+str(self.turnPlayer))
            #print(type(self.diagrams[:,:,self.tempo]))
            #print(type(self.turnPlayer))
            next_dia_all, next_diaList = fm.search_newstone_position_all(self.diagrams[:,:,self.tempo], self.turnPlayer)
            #print("NB-1\n"+str(next_dia_all)+"\nNB-2:\n"+str(next_diaList))
#            print(next_diaList[0])
            if len(next_diaList) == 0:
                if self.passtempo == True:
                    if self.vs_count == 1:
                        print("お互い打つ場所がないのでゲームセットです。")
                    next_posi = 'pass'
                    break
                else:
                    self.passtempo = True
                    next_posi = 'pass'
                    if self.vs_count == 1:
                        print("打つ場所がないのでパスとなります。")
            else:
                #fm.show_position(columnArray, rowArray, next_dia_all)
                self.passtempo = False
                if self.turnPlayer == 1:
                    if self.vs_count == 1:
                        print("先手の手番です。")
                    if self.con_fir == 1:
                        print("石を置く位置を入力してください")
                        #self.alg_fir.show_enable(self.diagrams, next_dia_all, next_diaList, self.turnPlayer)
                        show_enable(self.diagrams, next_dia_all, next_diaList, self.turnPlayer)
                        next_posi = input()
                        if next_posi == 'quit':
                            break
                        flag, EMsg = fm.next_posi_check(next_posi, next_dia_all, self.turnPlayer)
                        while flag == False:
                            print(EMsg)
                            next_posi = input()
                            flag, EMsg = fm.next_posi_check(next_posi, next_dia_all, self.turnPlayer)
                    else:
                        next_posi = self.alg_fir.get_next_posi(self.diagrams, next_dia_all, next_diaList, self.turnPlayer)
                        if self.vs_count == 1:
                            print(next_posi+"を着手します。")
                else:
                    if self.vs_count == 1:
                        print("後手の手番です。")
                    if self.con_sec == 1:
                        print("石を置く位置を入力してください")
                        #self.alg_sec.show_enable(self.diagrams, next_dia_all, next_diaList, self.turnPlayer)
                        show_enable(self.diagrams, next_dia_all, next_diaList, self.turnPlayer)
                        next_posi = input()
                        if next_posi == 'quit':
                            break
                        flag, EMsg = fm.next_posi_check(next_posi, next_dia_all, self.turnPlayer)
                        while flag == False:
                            print(EMsg)
                            next_posi = input()
                            flag, EMsg = fm.next_posi_check(next_posi, next_dia_all, self.turnPlayer)
                    else:
                        next_posi = self.alg_sec.get_next_posi(self.diagrams, next_dia_all, next_diaList, self.turnPlayer)
                        if self.vs_count == 1:
                            print(next_posi+"を着手します。")

            #ログを記録
            Blackcount, Whitecount = fm.stone_count_check(self.diagrams[:,:,self.tempo])
            if Blackcount > Whitecount:
                superiorityPlayer = 1
            elif Blackcount < Whitecount:
                superiorityPlayer = 2
            else:
                superiorityPlayer = 0

            data = [self.ID, self.tempo, self.turnPlayer, next_posi, len(next_diaList), Blackcount, Whitecount, self.con_fir, self.con_sec, superiorityPlayer]
            data.extend(self.diagrams[:,:,self.tempo].T.reshape(64))
            add_log = pd.Series(data=data, index=self.log.columns, name=self.tempo)
            self.log = self.log.append(add_log)

            #手数をインクリメント
            self.tempo += 1

            #盤面を更新
            if self.passtempo == False:
                for next_dia in next_diaList:
                    if next_dia[int(self.rowList[next_posi[1:]]),int(self.columnList[next_posi[:1]])] == 4 + self.turnPlayer:
                        self.diagrams[:,:,self.tempo] = next_dia.copy()
                    for i in range(0,8):
                        for j in range(0,8):
                            if self.diagrams[i,j,self.tempo] == 4 + self.turnPlayer:
                                self.diagrams[i,j,self.tempo] = self.turnPlayer
                            elif self.diagrams[i,j,self.tempo] == 3 or self.diagrams[i,j,self.tempo] == 4:
                                self.diagrams[i,j,self.tempo] = self.turnPlayer
            else:
                self.diagrams[:,:,self.tempo] = self.diagrams[:,:,self.tempo-1].copy()


            #手番の交代
            if self.turnPlayer == 1:
                self.turnPlayer = 2
            else:
                self.turnPlayer = 1

        #終局処理
        Blackcount, Whitecount = fm.stone_count_check(self.diagrams[:,:,self.tempo])
        if Blackcount > Whitecount:
            print(str(Blackcount) + " VS " + str(Whitecount) + " で先手●の勝ちです")
            self.win[0] += 1
        elif Whitecount > Blackcount:
            print(str(Whitecount) + " VS " + str(Blackcount) + " で後手○の勝ちです")
            self.win[1] += 1
        else:
            print("引き分けです")

        print("先手" + str(self.win[0]) + "勝 VS 後手" + str(self.win[1]) + "勝")
        self.log.to_csv(os.path.join(self.folder, self.ID + '.csv'), index=False)
        reevaluation()

    def start(self):

        self.condition_init()
        Parallel(n_jobs=self.n_jobs, verbose=10)(delayed(self.one_game)() for i in range(self.vs_count))

if __name__ == "__main__":

    othello = Othello(False, 2, 2, Algorithm.max_choice(), Algorithm.max_choice(), 1, 1, folder='test')
    othello.start()
