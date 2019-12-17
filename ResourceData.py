
class ResourceData:
    def __init__(self,resource,confidence,frequency,type):
        self.resouce=resource
        self.confidence=confidence
        self.frequency=frequency
        self.type=type
    def print(self):
        print(self.resouce, self.confidence, self.frequency)

class TripleData:
    def __init__(self,list,query):
        self.resource=[]
        for l in list:
            self.resource.append(l)
        self.tripleQuery=query
        self.calculateWeight()
        self.type='triple'
        self.alignment=set()
        self.answer=[]
        self.answerType=''
        self.pairanswer=[]
        self.leftalignment = set()
        self.rightalignment =set()
        self.pairalignment=set()
        self.lanswer=[]
        self.ranswer=[]


    def setanswer(self,a,type):
        self.answerType=type
        if type==0:
            self.answer=a
        if type==1:
            self.answer=a
        if type==2:
            self.pairanswer=a
            for an in a:
                self.lanswer.append(an[0])
                self.ranswer.append(an[1])
                self.answer.append(an[0])
                self.answer.append(an[1])


    def print(self):
        print(self.tripleQuery)
        # if self.answerType==2:
        #     print('R!:leftalign:',len(self.leftalignment))
        #     for j in self.leftalignment:
        #         print(j)
        #     print('right :',len(self.rightalignment))
        #     for k in self.rightalignment:
        #         print(k)
    def addalignment(self,a):
        for al in self.alignment:
            if a.sameLeft==al.sameLeft:
                return
        self.alignment.append(a)
    def calculateWeight(self):
        c=0
        i=0
        for t in self.resource:
            i=i+1
            c=c+t.confidence+t.frequency
        self.weight=c/i

    def con5(self):
        for a in self.pairanswer:
            for la in self.leftalignment:
                for ra in self.rightalignment:
                    if (a[0]==la[0] or a[0]==la[1]) and (a[1]==ra[0] or a[1]==ra[1]):
                        self.pairalignment.add((la,ra))




class AlignmentData:
    def __init__(self,sameL,sameR,con):
        self.sameLeft=sameL
        self.sameRight=sameR
        self.confidence=con
        self.type='alignment'
        self.leftTriple=set()
        self.rightTriple=set()

    def __eq__(self, other):
        return (self.sameLeft==other.sameLeft and self.sameRight==other.sameRight)or(self.sameLeft==other.sameRight and self.sameRight==other.sameLeft)
    def print(self):
        print(self.sameLeft+" sameas "+self.sameRight)
        # print('lefttriple:')
        # for i in self.leftTriple:
        #     print(i)
        # print('righttriple')
        # for j in self.rightTriple:
        #     print(j)

if __name__=="__main__":
    a=set()
    b=ResourceData("English",0.5,2)
    i=ResourceData("English",0.5,2)
    a.add(b)
    a.add(i)
    for c in a:
        c.print()