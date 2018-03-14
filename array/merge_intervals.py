# -*- coding:utf-8 -*-

"""
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        start, end = self.get_interval(intervals[0])[0], self.get_interval(intervals[0])[1]
        reslist = [self.get_interval(intervals[0])]
        for alis in intervals[1:]:
            l, r = self.get_interval(alis)[0], self.get_interval(alis)[1]
            if l > end:
                reslist.append(self.get_interval(alis))
            elif l == end:
                reslist[-1] = [start, r]
            elif r < start:
                reslist = [self.get_interval(alis)] + reslist
            elif r == start:
                reslist[-1] = [l, end]
            else:
                alis = [min(start, l), max(end, r)]
                reslist = self.get_reslist(reslist, l, r)
                reslist.append(alis)

            start, end = min(start, l), max(end, r)
            # print(reslist, start, end)
        return reslist

    def get_reslist(self, reslist, l, r):
        lindx, rindx = -1, -1
        print(reslist, l, r)
        for i in range(len(reslist)):
            if l > reslist[i][0]:
                lindx = i
            if r < reslist[i][1]:
                rindx = i
                break
        if lindx == -1:
            lindx = 0
        if rindx == -1:
            return []
        if lindx == 0:
            return reslist[rindx:]
        return [reslist[:lindx] + reslist[rindx:]]

    def get_interval(self, interval):
        return [interval.start, interval.end]


if __name__ == '__main__':
    alist = [[1,3],[4,5],[2,6],[8,10],[15,18]]
    alist1 = [[1, 4], [0, 2], [3, 5]]
    alist2 = [[4, 5], [2, 4], [4, 6], [3, 4], [0, 0], [1, 1], [3, 5], [2, 2]]
    alist3 = [[1,4], [4,5]]
    intervals = []
    for s, e in alist2:
        intervals.append(Interval(s, e))
    solut = Solution()
    print(solut.merge(intervals))
