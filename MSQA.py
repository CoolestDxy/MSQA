import Levenshtein
import time
from googleTranslate import *
from ResourceData import *
from SparqlSearch import *
from gurobipy import *
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize

Zhfile = 'data/zh_triples.txt'
Enfile = 'data/en_triples.txt'
AlgnmentfileZE = 'data/zh_en_alignment.txt'
AlgnmentfileEZ = 'data/en_zh_alignment.txt'
resourcePrexEn = "http://dbpedia.org/resource/"
propertyPrexEn = "http://dbpedia.org/property/"
resourcePrexZh = "http://zh.dbpedia.org/resource/"
propertyPrexZh = "http://zh.dbpedia.org/property/"
EnRDF = "En_triple.rdf"
ZhRDF = "Zh_triple.rdf"
ThresHold=0.84
EnResourceDic={}
EnPropertyDic={}
ZhResourceDic={}
ZhPropertyDic={}
zhSameAs={}
enSameAs={}



def listToDic(list):
    diclist=[]
    for l in list:
        dic={}
        for index, i in enumerate(l):
            dic[index] =i
        diclist.append(tupledict(dic))
    return diclist

def buildResourceDic():
    with open(Enfile, "r", encoding='UTF-8') as enTriple:
        for line in enTriple:
            line = line.strip('\n')
            parse_line = line.split('@@@')
            dicAddSet(EnResourceDic, parse_line[0], parse_line[1])
            dicAddSet(EnPropertyDic, parse_line[1], parse_line[2])
    with open(Zhfile, "r", encoding='UTF-8') as enTriple:
        for line in enTriple:
            line = line.strip('\n')
            parse_line = line.split('@@@')
            dicAddSet(ZhResourceDic, parse_line[0], parse_line[1])
            dicAddSet(ZhPropertyDic, parse_line[1], parse_line[2])
    print('resourcedic build!')


def dicAddSet(dic, key, value):
    if key in dic:
        dic[key].add(value)
    else:
        dic[key] = set()
        dic[key].add(value)


def buildAlignmentDic():
    with open(AlgnmentfileZE, 'r', encoding='UTF-8')as sameAs:
        for line in sameAs:
            line = line.strip('\n')
            parse_line = line.split('@@@')
            zhSameAs[parse_line[0]] = parse_line[1]
    with open(AlgnmentfileEZ, 'r', encoding='UTF-8')as sameAs:
        for line in sameAs:
            line = line.strip('\n')
            parse_line = line.split('@@@')
            enSameAs[parse_line[0]] = parse_line[1]
    print('build alignment list done!')

def findSynonym(parse):#input the tokens of the question, output all the synonum of the token
    synparse=set()
    for p in parse:
        print(p)
        syn=wn.synsets(p)
        for s in syn:
            subsyn=s.lemma_names()
            for i in subsyn:
                synparse.add(i)
    for i in parse:
        synparse.add(i)
    return synparse


class QA:
    def __init__(self,question,pre):
        self.predicts=pre
        self.question=question
        self.samePharse=[]
        self.Con1Set=[]
        self.candidate=[]
        self.erTriple=[]
        self.result = []
        self.Con4=[]
        self.finalQuery =[]
        self.sparqlSearch=SparqlSearch()
    def analysisQuestion(self):
        ##deletePunc = re.sub(r'[^\w\s]', '', self.question)
        print('analyzing...')
        parse = self.question.split()
        # print('translating...')
        # transToken=transSentence(self.question,'en2zh')
        # print('trans done')
        # for i in transToken:
        #     parse.append(i)
        #parse=findSynonym(parse0)
        candidateResource = []
        candidateProperty = []
        for p in parse:
            if p == '':
                continue
            # print(p)
            num = 0  # record the num of one resource
            canSame=[]
            for res in EnResourceDic.keys():
                con = Levenshtein.ratio(res, p)
                if con >= ThresHold:  # the threshold in the paper
                    num = num + 1
                    flag = False
                    for redata in candidateResource:
                        if redata.resouce == res and redata.type==0:
                            flag = True
                            redata.frequency = redata.frequency + 1
                    if flag == False:
                        new=ResourceData(res, con, 1,0)
                        candidateResource.append(new)
                        canSame.append(new)
            for pro in EnPropertyDic.keys():
                con = Levenshtein.ratio(pro, p)
                if con >= ThresHold:
                    num = num + 1
                    flag = False
                    for prodata in candidateProperty:
                        if prodata.resouce == pro and prodata.type==0:
                            flag = True
                            prodata.frequency = prodata.frequency + 1
                    if flag == False:
                        new=ResourceData(pro, con, 1,0)
                        candidateProperty.append(new)
                        canSame.append(new)
            for res in ZhResourceDic.keys():
                # print(res)
                con = Levenshtein.ratio(res, p)
                if con >= ThresHold:  # the threshold in the paper
                    flag = False
                    num = num + 1
                    for redata in candidateResource:
                        if redata.resouce == res and redata.type==1:
                            flag = True
                            redata.frequency = redata.frequency + 1
                    if flag == False:
                        new=ResourceData(res, con, 1,1)
                        candidateResource.append(new)
                        canSame.append(new)
            for pro in ZhPropertyDic.keys():
                con = Levenshtein.ratio(pro, p)
                if con >= ThresHold:
                    num=num+1
                    flag = False
                    for prodata in candidateProperty:
                        if prodata.resouce == pro and prodata.type==1:
                            flag = True
                            prodata.frequency = prodata.frequency + 1
                    if flag == False:
                        new=ResourceData(pro, con, 1,1)
                        candidateProperty.append(new)
                        canSame.append(new)
            if num > 1:  # judge if the pharse have two mapped resources
                self.samePharse.append(canSame)

        for part in self.predicts:
            transpart=translate(part,'en2zh')
            for zhpro in ZhPropertyDic.keys():
                con = Levenshtein.ratio(zhpro, transpart)
                if con>0.8:
                    candidateProperty.append(ResourceData(zhpro, con, 1, 1))#find Chinese relation
            p=part.split("'s")
            parsepro=p[-1]
            #print(parsepro)
            prop=parsepro.replace(' ','')
            print(prop)
            for pro in EnPropertyDic.keys():
                con = Levenshtein.ratio(pro, prop)
                if con >= 0.8:
                    candidateProperty.append(ResourceData(pro, con, 1,0))#find combined relation
        self.candidate = [candidateResource, candidateProperty]
        for i in candidateResource:
            i.print()
        for i in candidateProperty:
            i.print()
        print('analyzing done!')
        return self.candidate

    def generateTriple(self):
        res = self.candidate[0]
        pro = self.candidate[1]
        erEnTriple =[]
        erZhTriple =[]
        for en in res:
            if en.type==0 and en.resouce in EnResourceDic:
                for p in pro:
                    if p.type==0 and p.resouce in EnResourceDic[en.resouce]:
                        triple = '<' + resourcePrexEn + en.resouce + '> <' + propertyPrexEn + p.resouce + "> ?V2"
                        erEnTriple.append(TripleData([en, p], triple))
            elif en.type==1:
                for p in pro:
                    if p.type==1 and p.resouce in ZhResourceDic[en.resouce]:
                        triple = '<' + resourcePrexZh + en.resouce + '> <' + propertyPrexZh + p.resouce + "> ?V2"
                        erZhTriple.append(TripleData([en, p], triple))

        for p in pro:
            if p.type==0 and p.resouce in EnPropertyDic:
                for en in res:
                    if en.type==0 and en.resouce in EnPropertyDic[p.resouce]:
                        triple = "?V1 <" + propertyPrexEn + p.resouce + "> <" + resourcePrexEn + en.resouce + '>'
                        erEnTriple.append(TripleData([en, p], triple))
            elif p.type==1:
                for en in res:
                    if en.type==1 and en.resouce in ZhPropertyDic[p.resouce]:
                        triple = "?V1 <" + propertyPrexZh + p.resouce + "> <" + resourcePrexZh + en.resouce + '>'
                        erZhTriple.append(TripleData([en, p], triple))


            if p.type==0 and p.resouce in EnPropertyDic:
                triple = "?V1 <" + propertyPrexEn + p.resouce + "> ?V2"
                erEnTriple.append(TripleData([p], triple))
            if p.type==1 and p.resouce in ZhPropertyDic:
                triple = "?V1 <" + propertyPrexZh + p.resouce + "> ?V2"
                erZhTriple.append(TripleData([p], triple))
        self.erTriple = [erEnTriple, erZhTriple]
        # for i in erEnTriple:
        #     i.print()
        # for i in erZhTriple:
        #     i.print()
        self.addSameTriple(self.erTriple)
        return self.erTriple

    def addSameTriple(self,ert):
        for sp in self.samePharse:
            s =[]
            for res in sp:
                for tr in ert[0]:
                    for trres in tr.resource:
                        if res.resouce == trres.resouce and trres.type==res.type:
                            s.append(tr)
                for tr in ert[1]:
                    for trres in tr.resource:
                        if res.resouce == trres.resouce and trres.type==res.type:
                            s.append(tr)
            self.Con1Set.append(s)
        print('con1set',self.Con1Set)
        # for i in self.Con1Set:
        #     for ii in i:
        #         ii.print()

    def alignmentByTable(self):
        same = []
        for t in self.erTriple[0]:  # English Triple
            # print(t)
            s = ''
            if t.tripleQuery[0] == '<':  # judge the type of triple
                s = self.sparqlSearch.search(t.tripleQuery, "?V2",0)
                if len(s) == 0:
                    continue
                t.setanswer(s,1)
            elif t.tripleQuery[-1] != '2':
                s = self.sparqlSearch.search(t.tripleQuery, "?V1", 0)
                if len(s) == 0:
                    continue
                t.setanswer(s, 0)
            else:
                s = self.sparqlSearch.searchPair(t.tripleQuery, "?V1?V2", 0)
                if len(s) == 0:
                    continue
                t.setanswer(s, 2)

        for t in self.erTriple[1]:  # Chinese Triple
            if t.tripleQuery[0] == '<':  # judge the type of triple
                s = self.sparqlSearch.search(t.tripleQuery, "?V2", 1)
                if len(s) == 0:
                    continue
                t.setanswer(s,0)
            elif t.tripleQuery[-1] != '2':
                s = self.sparqlSearch.search(t.tripleQuery, "?V1", 1)
                if len(s) == 0:
                    continue
                t.setanswer(s,1)
            else:
                s = self.sparqlSearch.searchPair(t.tripleQuery, '?V1?V2', 1)
                if len(s) == 0:
                    continue
                t.setanswer(s,2)

        # print("----------samecandidate-----------",sameCandidate)
        totalTriple = self.erTriple[0] + self.erTriple[1]
        # for tt in totalTriple:
        #     print(tt.answer)
        for sc in list(itertools.combinations(totalTriple, 2)):
            con4=[]
            for a1 in sc[0].answer:
                for a2 in sc[1].answer:
                    if a1 in enSameAs and a2 == enSameAs[a1]:
                        a = AlignmentData(a1, a2, 1)
                        f = 0
                        for sa in same:
                            if sa.sameLeft == a.sameLeft:
                                f = 1
                        if f == 0:
                            same.append(a)
                            con4.append(a)
                    if a2 in enSameAs and a1==enSameAs[a2]:
                        a = AlignmentData(a1, a2, 1)
                        f = 0
                        for sa in same:
                            if sa.sameLeft == a.sameLeft:
                                f = 1
                        if f == 0:
                            same.append(a)
                            con4.append(a)
            if len(con4)>1:
                self.Con4.append(con4)
        for a in same:
            for tr in totalTriple:
                for ta in tr.answer:
                    if a.sameLeft == ta:
                        a.leftTriple.add(tr)
                    if a.sameRight == ta:
                        a.rightTriple.add(tr)
                if tr.answerType==2:
                    for p in tr.pairanswer:
                        if p[0]==a.sameLeft or p[0]==a.sameRight:
                            tr.leftalignment.add((a.sameLeft,a.sameRight))
                        if p[1]==a.sameLeft or p[1]==a.sameRight:
                            tr.rightalignment.add((a.sameLeft,a.sameRight))
                else:
                    for ta in tr.answer:
                        if a.sameLeft==ta or a.sameRight==ta:
                            tr.alignment.add((a.sameLeft,a.sameRight))
        self.result = [list(totalTriple), list(same)]
        print("alignmnet Done")
        return self.result

    def tripleEqual(self,tp1,tp2):
        for i in tp1.resource:
            f=0
            for j in tp2.resource:
                if i.resouce==j.resouce:
                    f=1
            if f==0:
                return False
        return True

    def ILPByGurobi(self):
        triple=self.result[0]
        alignment=self.result[1]
        #construct weight array
        tripleLength=len(triple)
        alignmentLength=len(alignment)
        print('length',tripleLength,alignmentLength)
        tripleWeight=[]
        alignmentWeight=[]
        tripleCover=[]
        for t in triple:
            t.calculateWeight()
            tripleWeight.append(t.weight)
            tripleCover.append(len(t.resource))
        for a in alignment:
            alignmentWeight.append(a.confidence)
        print('construct the constraint set')
        Same=[]
        #Contraint1:
        if len(self.Con1Set)!=0:
            for s in self.Con1Set:
                subcon=[0]*tripleLength
                for t in s:
                    for index,tr in enumerate(triple):
                        if t.tripleQuery==tr.tripleQuery:
                            subcon[index]=1
                Same.append(subcon)
        else:
            Same.append([0]*tripleLength)
        #Constraint2
        ER=[]
        for t in triple:
            if len(t.resource)==2:
                ER.append(1)
            else:
                ER.append(0)
        #Constraint3
        AliLeft=[]
        AliRight=[]
        for a in alignment:
            left=[0]*tripleLength
            right=[0]*tripleLength
            for index,tr in enumerate(triple):
                for at in a.leftTriple:
                    if tr.tripleQuery==at.tripleQuery:
                        left[index]=1
                for at in a.rightTriple:
                    if tr.tripleQuery==at.tripleQuery:
                        right[index]=1
            AliLeft.append(left)
            AliRight.append(right)
        #Constraint4:
        SameAli=[]
        for c in self.Con4:
            con4=[0]*alignmentLength
            for index,a in enumerate(alignment):
                for ca in c:
                    if ca.leftTriple==a.leftTriple:
                        con4[index]=1
            SameAli.append(con4)
        #Constraint5:
        ConflictAli=[]
        for t in triple:#情况一：对于一个resource不能对应多个alignment
            if t.answerType==2:
                con5=[0]*alignmentLength
                for index,a in enumerate(alignment):
                    for ta in t.leftalignment:
                        if a.sameLeft==ta[0]:
                            con5[index]=1
                ConflictAli.append(con5)

                con5=[0]*alignmentLength
                for index,a in enumerate(alignment):
                    for ta in t.rightalignment:
                        if a.sameLeft==ta[0]:
                            con5[index]=1
                ConflictAli.append(con5)

                #情况二：对齐导致不存在三元组
                t.con5()
                for pa in t.pairalignment:
                    con5 = [1] * alignmentLength
                    for index, a in enumerate(alignment):
                        if a.sameLeft == pa[0][0] or a.sameLeft==pa[0][1] or a.sameRight==pa[1][0] or a.sameRight==pa[1][1]:
                            con5[index] = 0
                    ConflictAli.append(con5)
            else:
                con5 = [0] * alignmentLength
                for index,a in enumerate(alignment):
                    for ta in t.alignment:
                        if a.sameLeft == ta[0]:
                            con5[index] = 1
                ConflictAli.append(con5)
        # print('matrix done')
        # print('con1:',Same)
        # print('con2:',ER)
        # print('con3:left',AliLeft)
        # print('right',AliRight)
        # print('con4:',SameAli)
        # print('con5:',ConflictAli)
        #Gurobi
        print('gurobi begin!')
        m=Model('ILP')
        finalTriple=m.addVars(tripleLength, vtype=GRB.BINARY, name="finalTriple")
        finalAlignment=m.addVars(alignmentLength, vtype=GRB.BINARY, name="finalAlignment")
        m.setObjective(sum(finalTriple[i]*tripleWeight[i] for i in range(tripleLength))+sum(finalAlignment[i]*alignmentWeight[i] for i in range(alignmentLength))+sum(finalTriple[i]*tripleCover[i] for i in range(tripleLength)),GRB.MAXIMIZE)
        for i in range(len(Same)):
            m.addConstr((sum(finalTriple[j]*Same[i][j] for j in range(tripleLength))<=1),'con1_'+str(i))#constraint1
        m.addConstr(sum(finalTriple[i]*ER[i] for i in range(tripleLength))>=1 ,'con2')#constraint2
        for i in range(alignmentLength):
            m.addConstr(sum(finalTriple[j]*AliLeft[i][j] for j in range(tripleLength))*finalAlignment[i]>=1*finalAlignment[i],'con3l_'+str(i))#constraint3
            m.addConstr(sum(finalTriple[j]*AliRight[i][j] for j in range(tripleLength))*finalAlignment[i]>=1*finalAlignment[i],'con3r_'+str(i) )
        for i in range(len(SameAli)):
            m.addConstr(quicksum(finalAlignment[j]*SameAli[i][j] for j in range(alignmentLength))<=1,'con4_'+str(i))#constraint4
        for i in range(len(ConflictAli)):
            m.addConstr(quicksum(finalAlignment[j]*ConflictAli[i][j]  for j in range(alignmentLength))<=1,'con5_'+str(i))#constraint5
        print('gurobi optimize!')
        m.write('msqa.lp')
        start=time.time()
        m.optimize()
        print('optimize done!')
        end=time.time()
        status=m.Status
        if  status == GRB.Status.INF_OR_UNBD or  status == GRB.Status.INFEASIBLE or status == GRB.Status.UNBOUNDED:
            print('infeasible modle')
            return -1
        if status!=GRB.Status.OPTIMAL:
            print('stop with status',str(status))
            return 0
        for i in m.getVars():
            print(i.varName, i.x)
        for i in range(tripleLength):
            if finalTriple[i].x==1:
                self.finalQuery.append(triple[i])
                # print('triplechose',i)
        for i in range(alignmentLength):
            if finalAlignment[i].x==1:
                self.finalQuery.append(alignment[i])
                # print('alichose',i)
                # print('alignmentlink:',AliLeft[i],AliRight[i])
                # alignment[i].print()
        print(str(end-start))
        return 1


    def FindAnswer(self):
        self.analysisQuestion()
        self.generateTriple()
        self.alignmentByTable()
        for s in self.result[0]:
            s.print()
        for s in self.result[1]:
            s.print()
        self.alignmentByTable()
        status=self.ILPByGurobi()
        print('final query!',status)
        if status==-1 or status==0:
            print('answer failed')
            return 0
        print('len',len(self.finalQuery))
        for i in self.finalQuery:
            i.print()
        answer=self.SimpleSearch(self.finalQuery)

        return answer

    def SimpleSearch(self,q):
        print('search begin')
        for i in q:
            i.print()
        result = set()
        inter = set()
        for tri in q:
            if tri.type == 'triple' and len(tri.resource) == 2:
                if tri.tripleQuery[0] == '<':  # judge the type of triple
                    inter = self.sparqlSearch.search(tri.tripleQuery, "?V2", 0)
                if tri.tripleQuery[-1] != '2':
                    inter = self.sparqlSearch.search(tri.tripleQuery, "?V1", 0)
        same = ''
        for a in q:
            if a.type == 'alignment':
                for i in inter:
                    if i.split('/')[-1] == a.sameLeft:
                        same = a.sameRight
                    if i.split('/')[-1] == a.sameRight:
                        same = a.sameLeft

        for t in q:
            if t.type == 'triple' and len(t.resource) == 1:
                sameq = '<' + resourcePrexZh + same + '> <' + propertyPrexZh + t.resource[0].resouce + "> ?V2"
                res = self.sparqlSearch.search(sameq, '?V2', 1)
                for r in res:
                    result.add(r)
        return result

if __name__=='__main__':
    # print(Levenshtein.ratio('placeOfBirth','placeofbirth'))
    buildResourceDic()
    buildAlignmentDic()
    # parse="the main religion of James_ Martin_ -LRB- Australian_ politician -RRB-'s place of death #the main religion #James_ Martin_ -LRB- Australian_ politician -RRB-'s place of death #James_ Martin_ -LRB- Australian_ politician -RRB-'s place #James_ Martin_ -LRB- Australian_ politician -RRB- #James_ Martin_ #Australian_ politician #death"
    # aparse=parse.split('#')
    # q=QA("What is the main religion of James_Martin_(Australian_politician)'s place of death",aparse)
    # print(q.FindAnswer())

    trainList = []
    with open('data/en_en_zh.txt', "r", encoding='UTF-8')as trainQuestion:
        for line in trainQuestion:
            route = line.split('@@@')
            tuple = (route[0], route[1], route[2])
            trainList.append(tuple)
    preList=[]
    with open('data/question_predicate'
              's.txt','r',encoding='UTF-8')as pre:
        for line in pre:
            parse=line.split('#')
            preList.append(parse)

    for i in range(0,len(trainList)):
        tp=trainList[i]
        q=QA(tp[0],preList[i])
        answer=q.FindAnswer()
        records=''
        #-2 is ILP model infeasible
        #-1 is query cannot get answer
        #0 is worng answer
        can=''
        for i in q.candidate:
            for ii in i:
                can=can+'#'+ii.resouce
        r=tp[0]+'   '+tp[1]+'   '+str(answer)+'   resource recognize   '+can+'   '+tp[2]
        if answer==0:
            records='-2   '+r
        elif len(answer)==0:
            records='-1   '+r
        elif tp[1] in answer:
            records=' 1   '+r
        else:
            records=' 0   '+r
        with open('performance_record(stanfordParse).txt', "a", encoding='UTF-8')as record:
            record.write(records)

