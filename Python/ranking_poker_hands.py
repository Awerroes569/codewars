class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]
    FIGURES={"T":10,"J":11,"Q":12,"K":13,"A":14}    
    
    def __init__(self, hand):
        self.__flush=False
        self.__street=False
        self.__values={4:[],3:[],2:[],1:[]}
        self.__index=""
        self.__rank=10
        elements=hand.split()
        color=elements[0][-1]
        self.__flush=all([True if x[-1]==color else False for x in elements ])
        values=sorted([int(x[:-1]) if x[0].isdigit() else PokerHand.FIGURES[x[0]]for x in elements],reverse=True)
        cards={x:0 for x in values}
        for i in values:
            cards[i]+=1
        for k,v in cards.items():
            self.__values[v].append(k)
        if len(self.__values[1])==5 and self.__values[1][0]-self.__values[1][-1]==4:
            self.__street=True
        self.__rank=self.rank()
        for k,v in self.__values.items():
            if len(v)>0:
                for i in v:
                    self.__index+=str(hex(i))                                
        
    def compare_with(self, other):
        if self.__rank<other.__rank:
            return PokerHand.RESULT[2]
        elif self.__rank>other.__rank:
            return PokerHand.RESULT[0]
        elif self.__index>other.__index:
            return PokerHand.RESULT[2]
        elif self.__index<other.__index:
            return PokerHand.RESULT[0]
        else:
            return PokerHand.RESULT[1]
    
    def rank(self):
        if all([self.__flush,self.__street]):
            return 1
        elif len(self.__values[4])>0:
            return 2
        elif all([len(self.__values[3])>0,len(self.__values[2])>0]):
            return 3
        elif self.__flush:
            return 4
        elif self.__street:
            return 5
        elif len(self.__values[3])>0:
            return 6
        elif len(self.__values[2])>1:
            return 7
        elif len(self.__values[2])>0:
            return 8
        else:
            return 9