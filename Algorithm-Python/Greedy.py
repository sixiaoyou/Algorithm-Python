#-*- coding: utf-8 -*-
"""
贪心算法一：
定义一个函数，名字为sameSums(aList)，alist是一个整形list
(限定重复元素不超过2个,排
2f0e
除这样的list，元素前后差为1，[4,5,6,7,8])，函数作用是判断能分成两组，
使得两组数字的和相等。若可以择返回值是true，
若不可以返回值是false。如下例：
sameSums([4, 7, 6, 3]) --> True //4+6 = 10 and 7 + 3 = 10
sameSums([3, 3]) --> True
sameSums([4, 12, 16]) --> True //4+12= 16 and 16
sameSums([5, 1]) --> False

特别提示：这个题目，贪心算法只能计算上面这样的情况。
这个题目，对初学者来说，有点难度，但稍微有点算法基础，编程思路，就不难。
先讲一个故事：二个小孩儿时从树上采板栗，最后合并一堆，分板栗，采集一人选一个的分。
假定人性是贪婪的，第一个先选的人，选最大的，第二个选的人，选次大的，一直循环下去。
贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来是最好的选择。
也就是说，不从整体最优上加以考虑，他所做出的是在某种意义上的局部最优解。
这个题目：先将list从大到小排序，中间设置2个空的list，从大的开始选，下一次选的时候，需要
比较一下和，如果谁的和小，再添加一个，直到最后一个元素。

"""


def sameSums(int_list):
    # """ www.iplaypy.com python教程 """
    # >>> sameSums([4, 7, 6, 3])
    # True
    # >>> sameSums([3, 3])
    # True
    # >>> sameSums([4, 12, 16])
    # True
    # >>> sameSums([5, 1])
    # False
    # """
    new_lst = sorted(int_list, reverse=True)
    list1 = list()
    list2 = list()
    for n in new_lst:
        if sum(list1) < sum(list2):
            list1.append(n)
        else:
            list2.append(n)
    return sum(list1) == sum(list2)


'''
问题描述：
当前有面值分别为2角5分，1角，5分，1分的硬币，请给出找n分钱的最佳方案（要求找出的硬币数目最少）
问题分析：
根据常识，我们到店里买东西找钱时，老板总是先给我们最大面值的，要是不够再找面值小一点的，直到找满为止。
如果老板都给你找分数的或者几角的，那你肯定不干，另外，他也可能没有那么多零碎的钱给你找。其实这就是一个典型的贪心选择问题。
先举个例子，假如老板要找给我99分钱，他有上面的面值分别为25，10，5，1的硬币数，为了找给我最少的硬币数，
那么他是不是该这样找呢，先看看该找多少个25分的，诶99／25＝3，
好像是3个，要是4个的话，我们还得再给老板一个1分的，我不干，那么老板只能给我3个25分的拉，由于还少给我24，
所以还得给我2个10分的和4个1分。
'''


def zhaoLinQian(list,total):
    nums=[]
    list=sorted(list,reverse=True)
    for i in list:
        nums.append(total/i)
        total=total%i
    for j in range(len(nums)):
        print '面值为: %d,应找零钱个数为：%d' %(list[j],nums[j])


if __name__ == "__main__":
    list=[25,10,5,1]
    total=99
    zhaoLinQian(list,total)


