import pandas as pd
import random
import os
from threading import Lock
from itertools import chain


def readfile(in_file, out_file):
    """
    load the origin data
    """
    fileHandle = open(out_file, 'w')
    for line in open(in_file):
        l = line.split('\t')
        try:
            fileHandle.write(l[1])
        except:
            pass

def readfile_train(out_file):
    """
    load the origin data
    """

    path = os.getcwd()
    file_names = os.listdir(path+'/origin_test')
    fileHandle = open(out_file, 'w')
    for file in file_names:
        for line in open('origin_test/' + file):
            l = line.split('\t')
            try:
                fileHandle.write(l[1])
            except:
                pass

# 去除原始数据中连续重复的单项行为
def process1(_str):
    """
        process the constant repeat elements in behavior sequence
    """
    _list = list(_str)
    n = len(_list)
    if n <= 1:
        print(_str)
        return
    list1 = []
    for i in range(n - 1):
        if _list[i] != _list[i + 1]:
            list1.append(_list[i])
    list1.append(_list[-1])
    str1 = ''.join(list1)
    return str1


def process2(_str):
    """
        process the too long behavior sequence
    """

    _list = list(_str)
    n = len(_list)
    if n <= 1:
        print(_str)
        return
    list1 = []
    for i in range(n - 1):
        if i < 20 and _list[i] != _list[i + 1]:
            list1.append(_list[i])
        elif _list[i].strip() != "d" and _list[i] != 'a' and _list[i] != 'e':
            list1.append(_list[i])
    list1.append(_list[-1])
    str1 = ''.join(list1)
    return str1


def process3(_str):
    _list = list(_str)
    n = len(_list)
    if n <= 1:
        print(_str)
        return
    list1 = []
    for i in range(n - 1):
        if i < random.randint(60, 70) and _list[i] != _list[i + 1]:
            list1.append(_list[i])

        elif _list[i].strip() != "m" and _list[i] != 'b' and _list[i] != 'o' and _list[i] != 'n' and _list[i] != 'p' \
                and _list[i] != 'g' and _list[i] != 'c' and _list[i] != 'h' and _list[i] != 'f' and _list[i] != 'i' \
                and _list[i] != 's' and _list[i] != 'q' and _list[i] != 'x' and _list[i] != 'r' and _list[i] != 'B' \
                and _list[i] != 'C' and _list[i] != 'l' and _list[i] != 'u' and _list[i] != 'k' and _list[i] != 'A' \
                and _list[i] != 'v' and _list[i] != 'w' and _list[i] != 'z' and _list[i] != 'j' and _list[i] != 't' \
                and _list[i] != 'F' and _list[i] != 'R' and _list[i] != '=' and _list[i] != '&' and _list[i] != '(' \
                and _list[i] != '_' and _list[i] != '$' and _list[i] != 'H' and _list[i] != 'K' and _list[i] != 'M' \
                and _list[i] != 'D':
            list1.append(_list[i])
    list1.append(_list[-1])
    str1 = ''.join(list1)
    return str1


def process4(_str):
    _list = list(_str)
    n = len(_list)
    if n <= 1:
        print(_str)
        return
    list1 = []
    for i in range(n - 1):
        if _list[i] != _list[i + 1]:
            list1.append(_list[i])
    list1.append(_list[-1])
    str1 = ''.join(list1)
    return str1


def process5(_str):
    _list = list(_str)
    n = len(_list)
    if n <= 1:
        print(_str)
        return
    list1 = []
    for i in range(n - 1):
        if i < 70 and _list[i] != _list[i + 1]:
            list1.append(_list[i])

        elif _list[i].strip() != "A" and _list[i] != 'x' and _list[i] != 'C' and _list[i] != 'o' and _list[i] != 'E' \
                and _list[i] != 'w' and _list[i] != 'B' and _list[i] != 'x' and _list[i] != 'I' and _list[i] != 'z' \
                and _list[i] != 'L':
            list1.append(_list[i])
    list1.append(_list[-1])
    str1 = ''.join(list1)
    return str1


def get_input_from_file(path):
    """
    Reads raw user behavior data from given file.
    """
    df = pd.read_csv(path, error_bad_lines=False)
    df = df.drop_duplicates()
    data = df.values.tolist()
    data = list(chain.from_iterable(data))
    return data


def Count(file):
    c = open('count.txt', 'w')
    list1 = []
    # print(max(len(x) for x in open(file)))
    for x in open(file):
        list1.append(len(x))
    list1.sort()
    for i in range(len(list1)):
        c.write(str(list1[i]) + '\n')


def ge_anoma():
    df = pd.read_csv("train_.csv")
    df = df.drop_duplicates()
    list1 = df.values.tolist()
    print(type(list1))
    print(list1)
    b = open('vulnbank_anomaly.txt', 'w')
    for line in list1:
        print(line)
        line = str(line)
        line = line.strip('[').strip(']').strip("'")
        line = list(line)
        random.shuffle(line)
        a = "".join(line)
        a = process1(a)
        b.write(str(a) + '\n')


def main():
    readfile_train('test.txt')
    #readfile('ip_behavior_20180919', 'train2.txt')
    lock = Lock()
    if lock.acquire():
        with open('train_process1.txt', 'w') as f:

            for x in open('test.txt', 'r'):
                st = process1(x)
                f.write(str(st))
    lock.release()

    if lock.acquire():
        with open('train_process2.txt', 'w') as f:
            for x in open('train_process1.txt', 'r'):
                st = process2(x)
                f.write(str(st))
    lock.release()

    if lock.acquire():
        with open('test_.txt', 'w') as f:
            for x in open('train_process2.txt', 'r'):
                st1 = process1(x)
                st2 = process3(st1)
                st3 = process1(st2)
                f.write(str(st3))
    lock.release()
'''
    if lock.acquire():
        with open('train_process4.txt', 'w') as f:
            for x in open('train_process3.txt', 'r'):
                st = process4(x)
                f.write(str(st))
    lock.release()

    e = open('train_.csv', 'w')
    for x in open('train_process4.txt', 'r'):
        st = process5(x)
        if len(st) <= 72:
            e.write(str(st))
'''

if __name__ == '__main__':

    main()
    # Count('train_.txt')
    # test("train_.txt")

    a = get_input_from_file('test_.txt')
    b = open('test.csv', 'w')
    for i in a:
        b.write(i + '\n')
