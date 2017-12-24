# -*- coding: utf-8 -*-

MAX = 50  # 最大活动数


class Active(object):  # 活动类
    def __init__(self, s, f, no):
        self.s = s  # 开始时间
        self.f = f  # 结束时间
        self.no = no  # 预安排会场号


# 交换两个类实例
def swap(si, sj):
    a[si].s, a[sj].s = a[sj].s, a[si].s
    a[si].f, a[sj].f = a[sj].f, a[si].f
    a[si].no, a[sj].no = a[sj].no, a[si].no


if __name__ == '__main__':
    k = input("输入待安排活动数: ")
    a = [Active for x in range(MAX)]
    print '输入待安排活动的开始时间和结束时间(用空格隔开):\n'
    # 输入活动开始和结束时间
    for i in range(1, k + 1):
        m, n = map(int, raw_input().split(" "))
        a[i] = Active(m, n, 0)
    # 活动时间排序
    for i in range(1, k + 1):
        for j in range(i, k + 1):
            if (a[i].s > a[j].s):
                swap(i, j)
            if (a[i].s == a[j].s):
                if (a[i].f > a[j].f):
                    swap(i, j)

    sum = 1  # 初始化会场数
    a[1].no = sum
    for x in range(2, k + 1):
        for y in range(1, x + 1):
            if ((a[y].no != 0) and (a[y].f <= a[x].s)):
                a[x].no = a[y].no
                a[y].no = 0  # 已安排过的活动置零
                break
        if (y == x):
            sum = sum + 1
            a[x].no = sum
    print sum
