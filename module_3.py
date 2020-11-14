#!/usr/bin/env python 3
# -*- config: utf-8 -*-

if __name__ == '__main__':
    dic = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", }
    new_dic = {j: i for i, j in dic.items()}
    print(dic, new_dic)
