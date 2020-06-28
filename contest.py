__author__ = 'samuel'

import numpy as np

class Strategy(object):
    def __init__(self):
        self.me = []
        self.opp = []

    def next(self, n, me_prev, opp_prev):
        pass


    def add_outcome(self, me_prev, opp_prev):
        self.me.append(me_prev)
        self.opp.append(opp_prev)

class Tit_tat(Strategy):
    def next(self, n):
        if n == 0:
            answer = 'N'
        else:
            answer = self.opp[n-1]
        return answer


class Thirds(Strategy):

    def next(self, n):
        if n % 3 == 0:
            answer = 'C'
        else:
            answer = 'N'
        return answer


# write your custom strategies like this:
class Tat_tit(Strategy):

    def next(self, n):
        if n == 0:
            answer = 'C'
        else:
            answer = self.opp[n-1]
        return answer

class Always_C(Strategy):

    def next(self, n):
        answer = 'C'
        return answer

class Always_NC(Strategy):

    def next(self, n):
        answer = 'N'
        return answer

zeroes = [0]*5
baverages = zeroes*5
averages = []


def dilemma(strat1, strat2, n):
    new_list=[]
    for i in range(n):
        p1 = strat1.next(i)
        p2 = strat2.next(i)

        if p1 == 'C' and p2 == 'C':
            new_list.append(5.)
        elif p1 == 'C' and p2 == 'N':
            new_list.append(0.)
        elif p1 == 'N' and p2 == 'N':
            new_list.append(1.)
        else:
            new_list.append(10.)
        #print(p1, p2)
        strat1.add_outcome(p1, p2)
        strat2.add_outcome(p2, p1)
    #print(new_list)
    return (sum(new_list)/n)
    #averages.append(a)



def contest(strat1, strat2, strat3, strat4, strat5, n):
    strategies = [strat1, strat2, strat3, strat4, strat5]
    for i in range(0,5):
        avg =[]
        for j in range(0, 5):
            avg.append(dilemma(strategies[i], strategies[j], n))
        averages.append(avg)
    print(averages)

    final_avg = []
    for k in range(0, len(averages)):
        final_avg.append(sum(averages[k])/len(averages[k]))
    print(final_avg)





if __name__ == '__main__':
    s1 = Thirds()
    s2 = Tat_tit()
    s3 = Always_C()
    s4 = Tit_tat()
    s5 = Always_NC()

    contest(s1, s2, s3, s4, s5, 10)


"""
with open('test1.csv', 'wb') as test_file:
    csv_writer = csv.writer(test_file)
    for y in range(0,10):
        csv_writer.writerow(200)
"""

