#!/
# _*_coding: utf-8 _*_
# @Time :  18:24
# @Author : Mark Melendez
# @File : 21点.py
# @desc :此程序非赌博行为
# -----------------------------begin-------------------------------
# 导入依赖包
import PySimpleGUI as gui
import random

# 定义必要变量
start = [
    [gui.T('21点游戏即将开始')],
    [gui.T('游戏规则', enable_events=True)],
    [gui.B('点击发牌')]
]

rule = [[gui.T('''玩家共两个角色：电脑和人类，电脑是庄家

游戏开始时，先给人类和电脑每个玩家分别发两张牌作为底牌，庄家底牌只漏一张

判断双方底牌是否直接为21点，如果其中一方为21点则直接判胜利。如果双方都是21点，那就是平局，不得分。

当初始牌面上，没有直接出现21点，人类玩家根据自己的牌面大小决定是否继续要牌。如果要牌，那就在牌堆中抽一张，然后再次判断胜负。如果人类牌面的总点数超过了21点，那就直接判输

如果人类玩家停止要牌了，并且没有因为超过21点而被判输的情况下，则电脑要牌。
1 比如电脑一直要牌，直到比人类玩家大才停止要牌。
2 根据牌堆中剩余牌的数量，计算赢的概率，然后设置一个阈值，超过阈值就要，低于就不要。

完成一轮游戏的时候，可由人类玩家决定，是否继续玩下一轮

牌堆中剩余的牌数不够玩一轮游戏的时候，游戏自动结束。

计算规则: 2. 3. 4. 5. 6. 7. 8. 9. 10分别是正常的点数，J. Q. K均为10点

首先把A当做1来计算，牌面点数如果小于21，那么再把A当做11再计算一次，如果这个时候仍然小于21，那么A就当11算，如果这个时候牌面点数大于了21，那么A就当1算。''')]]

J = 10
Q = 10
K = 10
card = [2, 3, 4, 5, 6, 7, 8, 9, J, Q, K, 'A']


# 定义必要方法
def tie():
    tie = [
        [gui.T('本次游戏以平局结束!!!')], [gui.B('再来一次')]
    ]
    tie_win = gui.Window('平局', tie)
    tie_event = tie_win.read()
    if tie_event == '再来一次':
        main()
        tie_win.close()
    elif tie_event is None:
        tie_win.close()


def transport():
    transport = [
        [gui.T('很遗憾你输掉了游戏!!!')], [gui.B('再来一次')]
    ]
    transport_win = gui.Window('赢得了胜利', transport)
    transport_event = transport_win.read()
    if transport_event == '再来一次':
        main()
        transport_win.close()
    elif transport_event is None:
        transport_win.close()


def win():
    win = [
        [gui.T('恭喜你赢得了胜利!!!')], [gui.B('再来一次')]
    ]
    win_win = gui.Window('赢得了胜利', win)
    win_event = win_win.read()
    if win_event == '再来一次':
        main()
        win_win.close()
    elif win_event is None:
        win_win.close()


def get_user_card(user_card):
    getwin = [
        [gui.T('您当前的点数：', user_card)],
        [gui.B('继续要牌')], [gui.B('停止要牌')]
    ]
    getwindow = gui.Window('要牌与否？', getwin)
    getevent = getwindow.read()
    while True:
        if getevent is None:
            break
        elif getevent == '继续要牌':
            licensing()
            if user_card > 21:
                win()
                break
            else:
                transport()
                break
        elif getevent == '停止要牌':
            licensing()
            pc_card = user_card
            if pc_card > 21:
                win()
                break
            elif pc_card == user_card:
                tie()
                break
            elif pc_card <= user_card:
                transport()
                break
            elif pc_card >= user_card:
                win()
    getwindow.close()
    user_card_new = user_card
    return user_card_new


def licensing():
    user_card = random.sample(card, k=2)  # 在card列表内随机选取2个值作为底牌
    # 将A的两种情况代入
    if 'A' in user_card[0]:
        user_card = user_card
        user_card = user_card[1] + 1  # 将随机选取的列表中的两个值相加成int(A=1)
        if user_card < 21:
            user_card = user_card + 10
    elif 'A' in user_card[1]:
        user_card = user_card
        user_card = user_card[0] + 11  # 将随机选取的列表中的两个值相加成int(A=11)
        if user_card < 21:
            user_card = user_card + 10
    else:
        user_card = user_card[0] + user_card[1]  # 将随机选取的列表中的两个值相加成int
    return user_card  # 传回user_card


# 定义mian函数
def main():
    # 主窗口
    stwin = gui.Window('21点游戏', start)
    event, values = stwin.read()
    while True:

        if event is None:
            break
        # 规则窗口
        if event == '游戏规则':
            rule_win = gui.Window('游戏规则', rule)
            rulevent = rule_win.read()
            if rulevent is None:
                rule_win.close()
        # 发牌
        elif event == '点击发牌':
            user_card = 0  # 初始化点数
            licensing()
            # 点数=21
            if user_card == 21:
                win()
            else:
                get_user_card(user_card)
            break
    stwin.close()


# 调用main函数
if __name__ == '__main__':
    main()
