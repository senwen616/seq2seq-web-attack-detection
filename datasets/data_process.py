import pandas as pd
import random
from threading import Lock
from itertools import chain


def readfile(in_file, out_file):
    """
    load the origin data
    """
    fileHandle = open(out_file, 'w')
    for line in open(in_file):
        l = line.split('\t')
        fileHandle.write(l[1])


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
        if i < 50 and _list[i] != _list[i + 1]:
            list1.append(_list[i])

        elif _list[i].strip() != "q" and _list[i] != 'b' and _list[i] != 'p' and _list[i] != 'f' and _list[i] != 'h' \
                and _list[i] != 'g' and _list[i] != 'c' and _list[i] != 'r' and _list[i] != 's' and _list[i] != 'i' \
                and _list[i] != 't' and _list[i] != 'j' and _list[i] != 'm' and _list[i] != 'l' and _list[i] != 'u' \
                and _list[i] != 'k' and _list[i] != 'v' and _list[i] != 'n':
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
    df = pd.read_csv(path)
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
    readfile('ip_behavior_20190111', 'train2.txt')
    lock = Lock()
    if lock.acquire():
        with open('train_process1.txt', 'w') as f:

            for x in open('train2.txt', 'r'):
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
        with open('train_process3.txt', 'w') as f:
            for x in open('train_process2.txt', 'r'):
                st = process3(x)
                f.write(str(st))
    lock.release()

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


if __name__ == '__main__':
    main()
    # Count('train_.txt')
    # test("train_.txt")
    a = get_input_from_file('train_process4.txt')
    b = open('test_.csv', 'w')
    for i in a:
        b.write(i + '\n')
