#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
try:
	from src import Elements
except ImportError:
	import Elements

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

def readFrom(filename):
    f = os.path.dirname(os.path.abspath(__file__)) + "/"
    """
    Format file:
    Tên map
    num1 num2 : Số hàng và số cột
    Ma trận num1 x num2
    ### Thông tin khác
    SH w x y
    <danh sách tọa độ>
    HI w x y
    <danh sách tọa độ>
    TG w x y
    <Danh sách tọa độ>
    SP w x y
    <Danh sách tọa độ, control được xét cho tọa độ đầu tiên>
    IN
    <Danh sách tọa độ>
    EN
    <Danh sách tọa độ>
    LSGOAL A/B          neu A la goal cho A tuong tu cho B, trong la danh cho ca 2
    <Danh sach toa do>
    IG 1/0                 #1 is autoIg and 0 is not
    <danh sach toa do>
    S&H w x y
    <danh sach toa do show>
    <danh sach toa do hide>
    S&T w x y
    <danh sach show>
    <danh sach toggle>
    """
    try:
        file = open(f + filename, mode='r')
    except IOError:
        file = open(f + filename[3:], mode='r')

    name = next(file)
    r, c = [int(x) for x in next(file).split()]
    matrix = list()
    blockarr = []
    goararr = []
    goala = []
    goalb = []
    isMatrix = True
    row = 0
    for line in file:
        if line.startswith("###"): isMatrix = False
        if isMatrix:
            matrix.append([Elements.Point(int(x), row, i) for i, x in enumerate(line.split())])
            row += 1
        elif line.startswith("SH"):#Show
            tmp = line.split()
            tmp.pop(0)
            w, x, y = [int(i) for i in tmp]
            nextline = [int(k) for k in next(file).split()]
            sh = Elements.Button(Elements.SHOWBTN, w, [], x, y)
            for i, j in pairwise(nextline):
                sh.lsPoint.append(matrix[i][j])
            matrix[x][y] = sh
        elif line.startswith("HI"):#Hide
            tmp = line.split()
            tmp.pop(0)
            w, x, y = [int(i) for i in tmp]
            nextline = [int(k) for k in next(file).split()]
            sh = Elements.Button(Elements.HIDEBTN, w, [], x, y)
            for i, j in pairwise(nextline):
                sh.lsPoint.append(matrix[i][j])
            matrix[x][y] = sh
        elif line.startswith("TG"):#Toggle
            tmp = line.split()
            tmp.pop(0)
            w, x, y = [int(i) for i in tmp]
            nextline = [int(k) for k in next(file).split()]
            sh = Elements.Button(Elements.TOGGLEBTN, w, [], x, y)
            for i, j in pairwise(nextline):
                sh.lsPoint.append(matrix[i][j])
            matrix[x][y] = sh
        elif line.startswith("SP"):#split
            tmp = line.split()
            tmp.pop(0)
            w, x, y = [int(i) for i in tmp]
            nextline = [int(k) for k in next(file).split()]
            sh = Elements.Button(Elements.SPLITBTN, w, [], x, y)
            for i, j in pairwise(nextline):
                sh.lsPoint.append([i, j])
            matrix[x][y] = sh
        elif line.startswith("EN"):#GOAL
            nextline = [int(k) for k in next(file).split()]
            for i, j in pairwise(nextline):
                matrix[i][j] = Elements.Button(Elements.GOAL, 3, [], i, j)
        elif line.startswith("IN"):#Init Block
            blockarr = [int(x) for x in next(file).split()]
        elif line.startswith("LSGOAL"):
            tmp = line.split()
            if len(tmp) == 1:
                goararr = [int(x) for x in next(file).split()]
            else:
                if tmp[1] == 'A':
                    goala = [int(x) for x in next(file).split()]
                elif tmp[1] == 'B':
                    goalb = [int(x) for x in next(file).split()]
        elif line.startswith("IG"):
            tmp = line.split()
            nextline = [int(k) for k in next(file).split()]
            for i, j in pairwise(nextline):
                if len(tmp) == 2 and tmp[1] == "1":
                    matrix[i][j].autoIg = False
                else: matrix[i][j].ig = True
        elif line.startswith("S&H"):
            tmp = line.split()
            tmp.pop(0)
            w, x, y = [int(i) for i in tmp]
            nextline = [int(k) for k in next(file).split()]
            nextline1 = [int(k) for k in next(file).split()]
            sh = Elements.Button(Elements.SHOWANDHIDE, w, [], x, y)
            for i, j in pairwise(nextline):
                sh.lsPoint.append(matrix[i][j])
            for i , j in pairwise(nextline1):
                sh.lsHide.append(matrix[i][j])
            matrix[x][y] = sh
        elif line.startswith("S&T"):
            tmp = line.split()
            tmp.pop(0)
            w, x, y = [int(i) for i in tmp]
            nextline = [int(k) for k in next(file).split()]
            nextline1 = [int(k) for k in next(file).split()]
            sh = Elements.Button(Elements.SHOWANDTOG, w, [], x, y)
            for i, j in pairwise(nextline):
                sh.lsShow.append(matrix[i][j])
            for i , j in pairwise(nextline1):
                sh.lsPoint.append(matrix[i][j])
            matrix[x][y] = sh

    map = Elements.Map(name, r, c, matrix)

    a = Elements.Node("A", blockarr[0], blockarr[1])
    b = Elements.Node("B", blockarr[2], blockarr[3])
    block = Elements.Block(a, b, a)
    goala = pairwise(goala)
    goalb = pairwise(goalb)
    goararr = pairwise(goararr)
    file.close()
    return (map, block, goararr, goala, goalb)