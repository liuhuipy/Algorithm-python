class Solution:
    def hasGroupsSizeX(self, deck: list) -> bool:
        if not deck:
            return False
        deck_dic = {}
        for dec_num in deck:
            deck_dic.setdefault(dec_num, 0)
            deck_dic[dec_num] += 1

        min_num = len(deck)
        for dec, num in deck_dic.items():
            if num < 2:
                return False
            min_num = min(min_num, num)
        min_l, i = set(), 2
        while i <= min_num:
            if min_num % i == 0:
                min_num = min_num // i
                min_l.add(i)
            else:
                i += 1
        res = [1] * len(min_l)
        index = 0
        for dec_l in min_l:
            for _, num in deck_dic.items():
                if num % dec_l != 0:
                    res[index] = 0
                    break
            index += 1
        return max(res) > 0
