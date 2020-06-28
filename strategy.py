__author__ = 'samuel'

#import numpy as np
import random as random


class Strategy(object):

    def next(self, n, me_prev, opp_prev):
        pass

    def setup(self):
        pass

    def reset_outcome(self):
        self.me = []
        self.opp = []


    def add_outcome(self, me_prev, opp_prev):
        self.me.append(me_prev)
        self.opp.append(opp_prev)

    def __init__(self):
        self.reset_outcome()


class Tit_tat(Strategy):

    def setup(self):
        self.name = 'Tit_tat'

    def next(self, n):
        if n == 0:
            answer = 'N'
        else:
            answer = self.opp[n-1]
        return answer


class Gang(Strategy):

    #def reset_outcome(self):

    def setup(self, n):
        self.name = 'Gangmember of rank ', n
        self.rank = n

    def next(self, n):
        if n == 0:
            self.code = True
            self.highrank = True
            self.countrank = 0
            return 'C'
        elif n <= 21 and self.code:
            if n % 3 == 0:
                if self.opp[n-1] == 'N':
                    return 'C'
                else:
                    self.code = False
                    return 'C'
            elif n % 3 == 1:
                if self.opp[n-1] == 'C':
                    return 'N'
                else:
                    self.code = False
                    return 'C'
            else:
                if self.opp[n-1] == 'N':
                    return 'N'
                else:
                    self.code = False
                    return 'C'
        elif self.code:
            if self.highrank:
                if self.opp[n-1] == 'C' and self.countrank > self.rank:
                    self.highrank = False
                    return 'N'
                else:
                    self.countrank += 1
                    return 'C'
            else:
                return 'N'
        else:
            return 'C'


class Tat_tit(Strategy):

    def setup(self):
        self.name = 'Tat_tit'

    def next(self, n):
        if n == 0:
            answer = 'C'
        else:
            answer = self.opp[n-1]
        return answer


class Always_C(Strategy):

    def setup(self):
        self.name = 'Always_C'

    def next(self, n):
        answer = 'C'
        return answer


class Always_NC(Strategy):

    def setup(self):
        self.name = 'Always_NC'

    def next(self, n):
        answer = 'N'
        return answer


class ForgivingTit_tat(Strategy):

    def setup(self):
        self.name = 'ForgivingTit_tat'

    def next(self, n):
        if n == 0:
            answer = 'N'
        else:
            if self.opp[n-1] == 'N':
                answer = self.opp[n-1]
            elif random.random() < 0.1:
                answer = 'N'
            else:
                answer = self.opp[n-1]

        return answer


def dilemma(strat1, strat2, n):
    new_list = []
    strat1.reset_outcome()
    strat2.reset_outcome()
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


def contest(strategies, n):
    averages = []
    final_avg = []
    for i in range(0,len(strategies)):
        avg =[]
        for j in range(0, len(strategies)):
            avg.append(dilemma(strategies[i], strategies[j], n))
        averages.append(avg)
        print([strategies[i].name,sum(avg)/len(avg)])

    #print(averages)
    #print(final_avg)
    return averages


if __name__ == '__main__':
    s1=[Tat_tit(),Always_C(),Tit_tat(), Always_NC()]
    s2=[ForgivingTit_tat(),Tat_tit(),Always_C(),Tit_tat(), Always_NC()]
    s3=[ForgivingTit_tat(),Tat_tit(),Always_C(),Tit_tat(), Always_NC()]
    s4=[Tit_tat()]*7 +[Tat_tit()]*12 +[ForgivingTit_tat()]*3+[Always_C()]+[Always_NC()]
    s5=[Tit_tat()]*10 +[Tat_tit()]*10 +[ForgivingTit_tat()]*10+[Always_C()]*10+[Always_NC()]*10
    s6=[]
    for i in range(0,10):
        s6.append(Gang())
        s6[len(s6)-1].setup(i+1)
        s6.append(Gang())
        s6[len(s6)-1].setup(i+2)
        s6.append(Gang())
        s6[len(s6)-1].setup(i+3)
        s6.append(Gang())
        s6[len(s6)-1].setup(i+4)
        s6.append(Gang())
        s6[len(s6)-1].setup(i+5)
        s6.append(Tit_tat())
        s6[len(s6)-1].setup()
        s6.append(Tat_tit())
        s6[len(s6)-1].setup()
        s6.append(ForgivingTit_tat())
        s6[len(s6)-1].setup()
        s6.append(Always_C())
        s6[len(s6)-1].setup()
        s6.append(Always_NC())
        s6[len(s6)-1].setup()


    #contest(s1, 1000)
    #contest(s2, 1000)
    #contest(s3, 1000)
    #contest(s5, 1000)
    contest(s6, 1000)



