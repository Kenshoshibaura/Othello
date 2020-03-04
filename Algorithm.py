#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
import numpy as np
import FunctionModules as fm
import os
import time
from tqdm import tqdm

columnList = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
rowList = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
Inv_columnList = {v:k for k, v in columnList.items()}
Inv_rowList = {v:k for k, v in rowList.items()}

Point = [50,-20,10,3,3,10,-20,50,-20,-40,-1,-1,-1,-1,-40,-20,
        10,-1,3,1,1,3,-1,10,3,-1,1,0,0,1,-1,3,
        3,-1,1,0,0,1,-1,3,10,-1,3,1,1,3,-1,10,
        -20,-40,-1,-1,-1,-1,-40,-20,50,-20,10,3,3,10,-20,50]

def Evaluation_board3(get_board_pattern,turn,enable_count):
    score = 0
    your_turn = change_turn(turn)
    board_list = [[1] for y in range(0,8) for x in range(0,8) if get_board_pattern[y][x]!=0]
    stone_listA = [[1] if get_board_pattern[y][x]==turn else 0 for y in range(0,8) for x in range(0,8)]
    stone_listB = [[-1] if get_board_pattern[y][x]==your_turn else stone_listA[y][x] for y in range(0,8) for x in range(0,8)]
    weight_list = [[Point[y*8+x]*board_list[y][x]] for y in range(0,8) for x in range(0,8)]
    stone = sum(board_list)
    stone_dif = sum(stone_listB)
    weight_dif = sum(weight_list)

    #print("Point:"+str(my_weight)+","+str(your_weight))
    if stone < 20: #序盤 A:最大20石差 * 3 = -60 ~ 60 B:最大20候補 * 6 = -6 ~ 108 C:重み 最大180 // 4 = -45 ~ 45 D:確定最大20石 * ? = -?? ~ ??
        score = (stone_dif * 3) + ((enable_count - 2) * 6) + (weight_dif // 4)
    elif stone < 50: #中盤 A:最大50石差 * 2 = -100 ~ 100 B:最大20候補 * 12 = -36 ~ 216 C:重み 最大320 / 2 = -160 ~ 160 D:確定最大50石 * ? = -?? ~ ??
        score = (stone_dif * 2) + ((enable_count - 2) * 12) + (weight_dif // 2)
    elif stone < 58: #終盤A A:最大55石差 * 4 = -220 ~ 220 B:最大20候補 * 3 = -3 ~ 54 C:重み 最大300? / 6 = -50 ~ 50 D:確定最大55石 * ? = -?? ~ ??
        score = (stone_dif * 4) + ((enable_count - 2) * 3) + (weight_dif // 6)
    elif stone < 62: #終盤B A:最大60石差 * 5 = -300 ~ 300 D:確定最大60石 * ? = -?? ~ ??
        score = (stone_dif * 5)
    else: #最終盤 A:最大64石差 * 10 = -640 ~ 640 完成済み
        score = (stone_dif * 10)

    #print("stone:"+str(stone)+" enable:"+str(enable_count)+" + score:"+str(score))
    return score
def Evaluation_board2(get_board_pattern,turn,enable_count):
    score = 0
    stone,blank = 0,0
    stone_dif = 0
    weight_dif = 0
    for y in range(0,8):
        for x in range(0,8):
            if str(get_board_pattern[y][x]) == str(turn):
                stone_dif += 1
                stone += 1
                weight_dif += Point[y*8+x]
            elif str(get_board_pattern[y][x]) == "0":
                blank += 1
            else:
                stone_dif -= 1
                stone += 1
                weight_dif -= Point[y*8+x]
    #print("Point:"+str(my_weight)+","+str(your_weight))
    if stone < 20: #序盤 A:最大20石差 * 3 = -60 ~ 60 B:最大20候補 * 6 = -6 ~ 108 C:重み 最大180 // 4 = -45 ~ 45 D:確定最大20石 * ? = -?? ~ ??
        score = (stone_dif * 3) + ((enable_count - 2) * 6) + (weight_dif // 4)
    elif stone < 50: #中盤 A:最大50石差 * 2 = -100 ~ 100 B:最大20候補 * 12 = -36 ~ 216 C:重み 最大320 / 2 = -160 ~ 160 D:確定最大50石 * ? = -?? ~ ??
        score = (stone_dif * 2) + ((enable_count - 2) * 12) + (weight_dif // 2)
    elif stone < 58: #終盤A A:最大55石差 * 4 = -220 ~ 220 B:最大20候補 * 3 = -3 ~ 54 C:重み 最大300? / 6 = -50 ~ 50 D:確定最大55石 * ? = -?? ~ ??
        score = (stone_dif * 4) + ((enable_count - 2) * 3) + (weight_dif // 6)
    elif stone < 62: #終盤B A:最大60石差 * 5 = -300 ~ 300 D:確定最大60石 * ? = -?? ~ ??
        score = (stone_dif * 5)
    else: #最終盤 A:最大64石差 * 10 = -640 ~ 640 完成済み
        score = (stone_dif * 10)

    #print("stone:"+str(stone)+" enable:"+str(enable_count)+" + score:"+str(score))
    return score
def Evaluation_board(get_board_pattern,turn):
    score = 0
    for y in range(0,8):
        for x in range(0,8):
            if str(get_board_pattern[y][x]) == str(turn):
                score += (Point[y*8+x] + 10)
            elif str(get_board_pattern[y][x]) == "0":
                score = score + 0
            else:
                score -= (Point[y*8+x] + 10)
    return score
def search_maxscore(file_search):
    max_score = -100000
    with open(file_search)as f:
        for line in f:
            brain_data = line[:-1].split(',')
            score = int(brain_data[1]) + int(brain_data[2])
            if score >= max_score:
                max_score = score
                select = str(brain_data[0])
        if max_score == -100000:
            select = random.choice(next_posi_enable)
            print("ERROR:max_score")
        #print("探索成功："+select+"を着手します "+str(max_score))
    return max_score,select
def board_conversion(next_dia_all):
    get_board_pattern = []
    for i in range(0,8):
        for j in range(0,8):
            if next_dia_all[i,j] == 3.0:
                get_board_pattern.append("2")
            elif next_dia_all[i,j] == 4.0:
                get_board_pattern.append("1")
            elif next_dia_all[i,j] == 5.0:
                get_board_pattern.append("0")
            elif next_dia_all[i,j] == 6.0:
                get_board_pattern.append("0")
            else:
                get_board_pattern.append(str(int(next_dia_all[i,j])))
    now_board_pattern = ''.join(get_board_pattern)
    #print("現在の盤面をリスト型で表すと次の通りとなります\n"+str(get_board_pattern))
    #print("現在の盤面を64bitで表すと次の通りとなります\n"+str(now_board_pattern))
    return get_board_pattern,now_board_pattern
def get_prediction_board(get_board_pattern,turn,candidate):

    board = [[0 for i in range(8)] for j in range(8)]
    after_board = [[0 for i in range(8)] for j in range(8)]

    if candidate == "pass":
        for i in range(0,8):
            for j in range(0,8):
                after_board[i][j] = int(get_board_pattern[i][j])
        return after_board

    #candidate から i,jを取得
    coordinate = list(candidate)
    x = columnList[str(coordinate[0])]
    y = rowList[str(coordinate[1])]

    if (type(get_board_pattern) is list) is True:
        for i in range(0,8):
            for j in range(0,8):
                board[i][j] = int(get_board_pattern[(i*8)+j])
    else:
        for i in range(0,8):
            for j in range(0,8):
                board[i][j] = int(get_board_pattern[i][j])

    if turn > 3:
        turn -= 3
    if turn == 1:
        my_turn = 1
        en_turn = 2
    elif turn == 2:
        my_turn = 2
        en_turn = 1
    else:
        print("ERROR:turn "+str(turn))

    board[y][x] = my_turn #着手を反映
    if (x < 6) and (board[y][x+1] == en_turn): #right
        for right in range(x+1,8):
            #print("R:"+str(right))
            if board[y][right] == en_turn:
                board[y][right] = 3
            elif board[y][right] == 0:
                break
            elif board[y][right] == my_turn:
                for m in range(0,8):
                    for n in range(0,8):
                        if board[m][n] == 3:
                            board[m][n] = my_turn
                break
        for m in range(0,8):
            for n in range(0,8):
                if board[m][n] == 3:
                    board[m][n] = en_turn
    if (x > 1) and (board[y][x-1] == en_turn): #left
        for left in range(x-1,-1,-1):
            #print("L:"+str(left))
            if board[y][left] == en_turn:
                board[y][left] = 3
            elif board[y][left] == 0:
                break
            elif board[y][left] == my_turn:
                for m in range(0,8):
                    for n in range(0,8):
                        if board[m][n] == 3:
                            board[m][n] = my_turn
                break
        for m in range(0,8):
            for n in range(0,8):
                if board[m][n] == 3:
                    board[m][n] = en_turn
    if (y < 6) and (board[y+1][x] == en_turn): #bottom
        for bottom in range(y+1,8):
            #print("B:"+str(bottom))
            if board[bottom][x] == en_turn:
                board[bottom][x] = 3
            elif board[bottom][x] == 0:
                break
            elif board[bottom][x] == my_turn:
                for m in range(0,8):
                    for n in range(0,8):
                        if board[m][n] == 3:
                            board[m][n] = my_turn
                break
        for m in range(0,8):
            for n in range(0,8):
                if board[m][n] == 3:
                    board[m][n] = en_turn
    if (y > 1) and (board[y-1][x] == en_turn): #top
        for top in range(y-1,-1,-1):
            #print("T:"+str(top))
            if board[top][x] == en_turn:
                board[top][x] = 3
            elif board[top][x] == 0:
                break
            elif board[top][x] == my_turn:
                for m in range(0,8):
                    for n in range(0,8):
                        if board[m][n] == 3:
                            board[m][n] = my_turn
                break
        for m in range(0,8):
            for n in range(0,8):
                if board[m][n] == 3:
                    board[m][n] = en_turn
    if (x > 1) and (y < 6) and (board[y+1][x-1] == en_turn): #left and bottom
        i=1
        for left in range(x-1,-1,-1):
            #print("LB:"+str(left)+","+str(y+i))
            if board[y+i][left] == en_turn:
                board[y+i][left] = 3
            elif board[y+i][left] == 0:
                break
            elif board[y+i][left] == my_turn:
                for m in range(0,8):
                    for n in range(0,8):
                        if board[m][n] == 3:
                            board[m][n] = my_turn
                break
            i+=1
            if((y+i)>7):
                break
        for m in range(0,8):
            for n in range(0,8):
                if board[m][n] == 3:
                    board[m][n] = en_turn
    if (x > 1) and (y > 1) and (board[y-1][x-1] == en_turn): #left and top
        i=1
        for left in range(x-1,-1,-1):
            #print("LT:"+str(left)+","+str(y-i))
            if board[y-i][left] == en_turn:
                board[y-i][left] = 3
            elif board[y-i][left] == 0:
                break
            elif board[y-i][left] == my_turn:
                for m in range(0,8):
                    for n in range(0,8):
                        if board[m][n] == 3:
                            board[m][n] = my_turn
                break
            i+=1
            if((y-i)<0):
                break
        for m in range(0,8):
            for n in range(0,8):
                if board[m][n] == 3:
                    board[m][n] = en_turn
    if (x < 6) and (y < 6) and (board[y+1][x+1] == en_turn): #right and bottom
        i=1
        for right in range(x+1,8):
            #print("RB:"+str(right)+","+str(y+i))
            if board[y+i][right] == en_turn:
                board[y+i][right] = 3
            elif board[y+i][right] == 0:
                break
            elif board[y+i][right] == my_turn:
                for m in range(0,8):
                    for n in range(0,8):
                        if board[m][n] == 3:
                            board[m][n] = my_turn
                break
            i+=1
            if((y+i)>7):
                break
        for m in range(0,8):
            for n in range(0,8):
                if board[m][n] == 3:
                    board[m][n] = en_turn
    if (x < 6) and (y > 1) and (board[y-1][x+1] == en_turn): #right and top
        i=1
        for right in range(x+1,8):
            #print("RT:"+str(right)+","+str(y-i))
            if board[y-i][right] == en_turn:
                board[y-i][right] = 3
            elif board[y-i][right] == 0:
                break
            elif board[y-i][right] == my_turn:
                for m in range(0,8):
                    for n in range(0,8):
                        if board[m][n] == 3:
                            board[m][n] = my_turn
                break
            i+=1
            if((y-i)<0):
                break
        for m in range(0,8):
            for n in range(0,8):
                if board[m][n] == 3:
                    board[m][n] = en_turn
    #print(board)

    for y in range(0,8):
        for x in range(0,8):
            after_board[y][x] = int(board[y][x])

    return after_board
def change_turn(turn):
    if turn == 1:
        return 2
    elif turn == 2:
        return 1
    else:
        print("ERROR:change_turn()")
        return 0
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
def search_enable(demo_board,turn):
    #turn=change_turn(turn)
    demo_dia_all, demo_diaList = fm.search_newstone_position_all(demo_board,turn)
    demo_posi_enable = []
    for i in range(0,8):
        for j in range(0,8):
            if demo_dia_all[i,j] == turn + 4:
                demo_posi_enable.append(str(Inv_columnList[j])+str(Inv_rowList[i]))
    if not demo_posi_enable:
        demo_posi_enable.append("pass")
    #print("指すことの可能な手は次の通りです:"+str(demo_posi_enable))

    return demo_posi_enable
def addwrite(file_search,select,score):
    exist = 0
    if (os.path.exists(file_search)) == True: #2重書き込み防止
        with open(file_search,mode='r')as f:
            for line in f:
                if (select in line) is True:
                    exist = 1
    if exist == 0:
        with open(file_search,mode='a')as f:
            input_data = str(select) + "," + str(score) + ",0\n"
            #print("input_data:"+input_data)
            f.write(input_data)
def MiniMax(now_board,my_turn,next_posi_enable,search_count,search,file_search):
    your_turn = change_turn(my_turn)
    my_turn_score = -100000
    my_turn_select = ""
    for m,my_candidate in enumerate(next_posi_enable):
        demo_after_me = get_prediction_board(now_board,my_turn,my_candidate)
        demo_after_me_2 = np.array(demo_after_me)
        your_enable = search_enable(demo_after_me_2,your_turn)
        if not your_enable:
            your_enable.append('pass')
        your_turn_score = 100000
        score_pre = -100000
        for y,your_candidate in enumerate(your_enable):
            demo_after_you = get_prediction_board(demo_after_me_2,your_turn,your_candidate)
            demo_after_you_2 = np.array(demo_after_you)
            my_enable = search_enable(demo_after_you_2,my_turn)
            if not my_enable:
                my_enable.append('pass')
            if search_count > 1:
                score_pre,select_new = MiniMax(demo_after_you_2,my_turn,my_enable,search_count-1,search,file_search)
            elif search_count <= 1:
                for l,last_candidate in enumerate(my_enable):
                    demo_last = get_prediction_board(demo_after_me_2,my_turn,last_candidate)
                    demo_last_2 = np.array(demo_last)
                    score_new = Evaluation_board(demo_last,my_turn)
                    if score_new > score_pre:
                        score_pre = score_new
            if score_pre < your_turn_score:
                your_turn_score = score_pre
        if search == search_count:
            addwrite(file_search,my_candidate,your_turn_score)
        if your_turn_score > my_turn_score:
            my_turn_score = your_turn_score
            my_turn_select = my_candidate
    return my_turn_score,my_turn_select
def AB(now_board,my_turn,next_posi_enable,search_count,search,file_search):
    your_turn = change_turn(my_turn)
    my_turn_score = -100000
    my_turn_select = ""
    for m,my_candidate in enumerate(next_posi_enable):
        demo_after_me = get_prediction_board(now_board,my_turn,my_candidate)
        demo_after_me_2 = np.array(demo_after_me)
        your_enable = search_enable(demo_after_me_2,your_turn)
        if not your_enable:
            your_enable.append('pass')
        your_turn_score = 100000
        score_pre = -100000
        for y,your_candidate in enumerate(your_enable):
            demo_after_you = get_prediction_board(demo_after_me_2,your_turn,your_candidate)
            demo_after_you_2 = np.array(demo_after_you)
            my_enable = search_enable(demo_after_you_2,my_turn)
            if not my_enable:
                my_enable.append('pass')
            if search_count > 1:
                score_pre,select_new = AB(demo_after_you_2,my_turn,my_enable,search_count-1,search,file_search)
            elif search_count <= 1:
                for l,last_candidate in enumerate(my_enable):
                    demo_last = get_prediction_board(demo_after_me_2,my_turn,last_candidate)
                    demo_last_2 = np.array(demo_last)
                    last_enable = search_enable(demo_last_2,your_turn)
                    #score_new = Evaluation_board(demo_last,my_turn)
                    score_new = Evaluation_board2(demo_last,my_turn,len(last_enable))
                    if score_new > score_pre:
                        score_pre = score_new
                    if score_pre > your_turn_score:
                        break
            if score_pre < your_turn_score:
                your_turn_score = score_pre
            if your_turn_score < my_turn_score:
                break
        if search == search_count:
            addwrite(file_search,my_candidate,your_turn_score)
        if your_turn_score > my_turn_score:
            my_turn_score = your_turn_score
            my_turn_select = my_candidate
    return my_turn_score,my_turn_select
def AB2(now_board,my_turn,next_posi_enable,search_count,search,file_search):
    your_turn = change_turn(my_turn)
    my_turn_score = -100000
    my_turn_select = ""
    if search == search_count:
        text = tqdm(next_posi_enable)
    else:
        text = next_posi_enable
    for m,my_candidate in enumerate(text):
        demo_after_me = get_prediction_board(now_board,my_turn,my_candidate)
        demo_after_me_2 = np.array(demo_after_me)
        your_enable = search_enable(demo_after_me_2,your_turn)
        if not your_enable:
            your_enable.append('pass')
        your_turn_score = 100000
        score_pre = -100000
        for y,your_candidate in enumerate(your_enable):
            demo_after_you = get_prediction_board(demo_after_me_2,your_turn,your_candidate)
            demo_after_you_2 = np.array(demo_after_you)
            my_enable = search_enable(demo_after_you_2,my_turn)
            if not my_enable:
                my_enable.append('pass')
            if search_count > 1:
                score_pre,select_new = AB2(demo_after_you_2,my_turn,my_enable,search_count-1,search,file_search)
            elif search_count <= 1:
                for l,last_candidate in enumerate(my_enable):
                    demo_last = get_prediction_board(demo_after_me_2,my_turn,last_candidate)
                    demo_last_2 = np.array(demo_last)
                    last_enable = search_enable(demo_last_2,your_turn)
                    #score_new = Evaluation_board(demo_last,my_turn)
                    score_new = Evaluation_board2(demo_last,my_turn,len(last_enable))
                    if score_new > score_pre:
                        score_pre = score_new
                    if score_pre > your_turn_score:
                        break
            if score_pre < your_turn_score:
                your_turn_score = score_pre
            if your_turn_score < my_turn_score:
                break
        if search == search_count:
            addwrite(file_search,my_candidate,your_turn_score)
        if your_turn_score > my_turn_score:
            my_turn_score = your_turn_score
            my_turn_select = my_candidate
    """
    if search == search_count:
        for m,my_candidate in enumerate(tqdm(next_posi_enable)):
            demo_after_me = get_prediction_board(now_board,my_turn,my_candidate)
            demo_after_me_2 = np.array(demo_after_me)
            your_enable = search_enable(demo_after_me_2,your_turn)
            if not your_enable:
                your_enable.append('pass')
            your_turn_score = 100000
            score_pre = -100000
            for y,your_candidate in enumerate(your_enable):
                demo_after_you = get_prediction_board(demo_after_me_2,your_turn,your_candidate)
                demo_after_you_2 = np.array(demo_after_you)
                my_enable = search_enable(demo_after_you_2,my_turn)
                if not my_enable:
                    my_enable.append('pass')
                if search_count > 1:
                    score_pre,select_new = AB2(demo_after_you_2,my_turn,my_enable,search_count-1,search,file_search)
                elif search_count <= 1:
                    for l,last_candidate in enumerate(my_enable):
                        demo_last = get_prediction_board(demo_after_me_2,my_turn,last_candidate)
                        demo_last_2 = np.array(demo_last)
                        last_enable = search_enable(demo_last_2,your_turn)
                        #score_new = Evaluation_board(demo_last,my_turn)
                        score_new = Evaluation_board2(demo_last,my_turn,len(last_enable))
                        if score_new > score_pre:
                            score_pre = score_new
                        if score_pre > your_turn_score:
                            break
                if score_pre < your_turn_score:
                    your_turn_score = score_pre
                if your_turn_score < my_turn_score:
                    break
            if search == search_count:
                addwrite(file_search,my_candidate,your_turn_score)
            if your_turn_score > my_turn_score:
                my_turn_score = your_turn_score
                my_turn_select = my_candidate
    else:
        for m,my_candidate in enumerate(next_posi_enable):
            demo_after_me = get_prediction_board(now_board,my_turn,my_candidate)
            demo_after_me_2 = np.array(demo_after_me)
            your_enable = search_enable(demo_after_me_2,your_turn)
            if not your_enable:
                your_enable.append('pass')
            your_turn_score = 100000
            score_pre = -100000
            for y,your_candidate in enumerate(your_enable):
                demo_after_you = get_prediction_board(demo_after_me_2,your_turn,your_candidate)
                demo_after_you_2 = np.array(demo_after_you)
                my_enable = search_enable(demo_after_you_2,my_turn)
                if not my_enable:
                    my_enable.append('pass')
                if search_count > 1:
                    score_pre,select_new = AB2(demo_after_you_2,my_turn,my_enable,search_count-1,search,file_search)
                elif search_count <= 1:
                    for l,last_candidate in enumerate(my_enable):
                        demo_last = get_prediction_board(demo_after_me_2,my_turn,last_candidate)
                        demo_last_2 = np.array(demo_last)
                        last_enable = search_enable(demo_last_2,your_turn)
                        #score_new = Evaluation_board(demo_last,my_turn)
                        score_new = Evaluation_board2(demo_last,my_turn,len(last_enable))
                        if score_new > score_pre:
                            score_pre = score_new
                        if score_pre > your_turn_score:
                            break
                if score_pre < your_turn_score:
                    your_turn_score = score_pre
                if your_turn_score < my_turn_score:
                    break
            if search == search_count:
                addwrite(file_search,my_candidate,your_turn_score)
            if your_turn_score > my_turn_score:
                my_turn_score = your_turn_score
                my_turn_select = my_candidate
    """
    return my_turn_score,my_turn_select

class AI_choice:

    def __init__(self):
        pass

    def get_next_posi(self, diagrams, next_dia_all, next_diaList, turn):
        #print("---"+str(turn)+"の次の手の探索を開始します---")
        #着手可能手抽出 next_posi_enable
        next_posi_enable = search_enable_first(next_dia_all,turn)
        #現在の盤面取得・変換 get_board_pattern,ow_board_pattern
        get_board_pattern,now_board_pattern = board_conversion(next_dia_all)

        #検索するファイル名作成 file_search
        file_search = "brain/" + str(turn) + "/" + now_board_pattern + ".csv"

        #ファイルが存在するか探索
        if (os.path.exists(file_search)) == True:
            start = time.time()
            score,select = search_maxscore(file_search)
            finish = time.time() - start
            print("探索成功："+select+"を着手します "+str(score)+" time:"+str(finish))

        else: #新規盤面(ファイルが存在しない)場合 MiniMax探索を実行
            #start = time.time()
            #score,select = AB(get_board_pattern,turn,next_posi_enable,2,2,file_search)
            #finish = time.time() - start
            #print("AB Result:"+select+" "+str(score))
            start = time.time()
            #for _ in tqdm(range(1)):
            score,select = AB2(get_board_pattern,turn,next_posi_enable,2,2,file_search)
            finish = time.time() - start
            #print("AB Result:"+select+" "+str(score))
            #print("AB: "+str(finish)+" AB2: "+str(finish2)+" ~ "+str(finish/finish2))
            print("新規盤面："+select+"を着手します score(AB):"+str(score)+" time:"+str(finish))

        return select

class random_choice:

    def __init__(self):
        pass

    def get_next_posi(self, diagrams, next_dia_all, next_diaList, turn):
        next_posi_enable = []
        for i in range(0,8):
            for j in range(0,8):
                if next_dia_all[i,j] == turn + 4:
                    next_posi_enable.append(str(Inv_columnList[j])+str(Inv_rowList[i]))
        select = random.choice(next_posi_enable)
        return select
class max_choice:

    def __init__(self):
        pass

    def get_next_posi(self, diagrams, next_dia_all, next_diaList, turn):
        next_count = []
        for next_dia in next_diaList:
            next_count.append((next_dia==turn).sum() + (next_dia==turn+2).sum() + (next_dia==turn+4).sum())

        next_count = np.array(next_count)
        targets = np.where(next_count == next_count.max())

        target = random.choice(targets[0])
        next_dia = next_diaList[target]
        tmp = np.where(next_dia == turn+4)

        next_posi = str(Inv_columnList[tmp[1][0]])+str(Inv_rowList[tmp[0][0]])

        return next_posi
