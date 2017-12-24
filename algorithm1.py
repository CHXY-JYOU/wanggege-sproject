# -*- coding:utf-8 -*-

import pandas as pd

MAX = 100000 #标识最大的可能整数
def dist(a, b): #返回字符a与b的ASCII码的差的绝对值
    return abs(ord(a) - ord(b))
val = pd.DataFrame(range(0), index=range(-1, 300), columns=range(-1, 300))
def comp():
    val.loc[0][0] = 0;
    len1 = len(str1)
    len2 = len(str2)
    for i in range(0, len1+1):
        for j in range(0, len2+1):
            if (i + j):  #i和j至少一个大于0
                val.loc[i][j] = MAX

                tmp = (val.loc[i - 1][j] + k)
                if (i)and(tmp < val.loc[i][j]): #i大于0
                    val.loc[i][j] = tmp

                tmp = (val.loc[i][j - 1] + k)
                if (j)and(tmp < val.loc[i][j]): #j大于0
                    val.loc[i][j] = tmp

                tmp = (val.loc[i - 1][j - 1] + dist(str1[i - 1], str2[j - 1]))
                if (i * j)and (tmp < val.loc[i][j]): #i和j至少有一个不为0
                        val.loc[i][j] = tmp

    print val.loc[len1][len2]

if __name__ == '__main__':
    str1 = raw_input('input A：') #字符串A
    str2 = raw_input('input B: ') #字符串B
    k = input('input k: ')       #与空格固定距离k
    comp()
