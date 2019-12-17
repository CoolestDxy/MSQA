import re
import rdflib

class SparqlSearch:

    def __init__(self):
        self.Zhgraph=rdflib.Graph()
        self.Engraph=rdflib.Graph()
        self.Zhgraph.parse('zh_triple.rdf')
        self.Engraph.parse('En_triple.rdf')
        self.rule = re.compile('\'(.*?)\'')
    def search(self,s,v,type):
        result =[]
        if type==0:#En
            search = "select " + v + " where{" + s + "}"
            l = list(self.Engraph.query(search))
            for ll in l:
                filt = self.rule.findall(str(ll))
                for f in filt:
                    result.append(f.split('/')[-1])
            #print("EN search result! ", s, result)
        if type == 1:  # Zh
            search = "select " + v + " where{" + s + "}"
            l = list(self.Zhgraph.query(search))
            for ll in l:
                filt = self.rule.findall(str(ll))
                for f in filt:
                    result.append(f.split('/')[-1])
            #print("CN search result! ", s, result)
        return result

    def searchPair(self,s,v,type):
        result=[]
        if type==0:#EN
            search = "select " + v + " where{" + s + "}"
            l = list(self.Engraph.query(search))
            for pair in l:
                pair = list(pair)
                filtpair = []
                p0 = pair[0].split('/')[-1]
                p1 = pair[1].split('/')[-1]
                filtpair.append(p0)
                filtpair.append(p1)
                result.append(filtpair)
            print("search result! ", s, result)
            return result
        if type==1:#CN
            search = "select " + v + " where{" + s + "}"
            l = list(self.Zhgraph.query(search))
            for pair in l:
                pair = list(pair)
                filtpair = []
                p0 = pair[0].split('/')[-1]
                p1 = pair[1].split('/')[-1]
                filtpair.append(p0)
                filtpair.append(p1)
                result.append(filtpair)
            print("search result! ", s, result)
            return result

