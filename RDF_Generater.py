import rdflib
import re
resourcePrexEn="http://dbpedia.org/resource/"
propertyPrexEn="http://dbpedia.org/property/"
resourcePrexZh="http://zh.dbpedia.org/resource/"
propertyPrexZh="http://zh.dbpedia.org/property/"

def buildEnRDFKB():
    rule0 = re.compile('\'(.*?)\'')
    rule1=re.compile('<(.*?)>')
    graph = rdflib.Graph()
    with open("MyEntriple", "r",encoding='UTF-8') as enTriple:
        i=0
        j=0
        for line in enTriple:
            i=i+1
            resource = rule0.findall(line)
            valid = 1
            if len(resource) != 3:
                valid = 0
                j=j+1
                #print(line)
            for p in resource:
                if p == '':
                    valid = 0
            if valid == 0:
                continue
            if len(rule1.findall(resource[0]))==0:
                continue
            re1 = rule1.findall(resource[0])[0]
            re2 = rule1.findall(resource[1])[0]
            if len(rule1.findall(resource[2]))==0:
                re3=resource[2]
            else:
                re3 = rule1.findall(resource[2])[0]
            entity1=rdflib.URIRef(re1)
            relation=rdflib.URIRef(re2)
            entity2=rdflib.URIRef(re3)
            graph.add((entity1,relation,entity2))
            if i==20:
                print("wrong triple",j)
                graph.serialize("en_triple.rdf")
                break
            if i%10000==0:
                print("build ",i)
        graph.serialize("en_triple.rdf")


def buildZhRDFKB():
    rule0 = re.compile('\'(.*?)\'')
    rule1=re.compile('<(.*?)>')
    graph = rdflib.Graph()
    with open("MyZhtriple", "r",encoding='UTF-8') as enTriple:
        i=0
        j=0
        for line in enTriple:
            i=i+1
            resource = rule0.findall(line)
            valid = 1
            if len(resource) != 3:
                valid = 0
                j=j+1
                #print(line)
            for p in resource:
                if p == '':
                    valid = 0
            if valid == 0:
                continue
            if len(rule1.findall(resource[0]))==0:
                continue
            re1 = rule1.findall(resource[0])[0]
            re2 = rule1.findall(resource[1])[0]
            if len(rule1.findall(resource[2]))==0:
                re3=resource[2]
            else:
                re3 = rule1.findall(resource[2])[0]
            entity1=rdflib.URIRef(re1)
            relation=rdflib.URIRef(re2)
            entity2=rdflib.URIRef(re3)
            graph.add((entity1,relation,entity2))
            if i==20:
                print("wrong triple",j)
                graph.serialize("zh_triple.rdf")
                break
            if i%10000==0:
                print("build ",i)
        graph.serialize("zh_triple.rdf")
def buildMyZhRDFKB():
    graph = rdflib.Graph()
    with open("data/zh_triples.txt", "r",encoding='UTF-8') as enTriple:
        for line in enTriple:
            line=line.strip('\n')
            sparse_line=line.split('@@@')
            entity1 = rdflib.URIRef(resourcePrexZh+sparse_line[0])
            relation = rdflib.URIRef(propertyPrexZh+sparse_line[1])
            entity2 = rdflib.URIRef(resourcePrexZh+sparse_line[2])
            graph.add((entity1, relation, entity2))
    graph.serialize("Zh_triple.rdf")

def buildMyEnRDFKB():
    graph = rdflib.Graph()
    with open("data/en_triples.txt", "r",encoding='UTF-8') as enTriple:
        for line in enTriple:
            line=line.strip('\n')
            sparse_line=line.split('@@@')
            entity1 = rdflib.URIRef(resourcePrexEn+sparse_line[0])
            relation = rdflib.URIRef(propertyPrexEn+sparse_line[1])
            entity2 = rdflib.URIRef(resourcePrexEn+sparse_line[2])
            graph.add((entity1, relation, entity2))
    graph.serialize("En_triple.rdf")

def sparqlTest():
    g = rdflib.Graph()
    g.parse("zh_triple.rdf", format="xml")
    search="select ?Q where{<http://zh.dbpedia.org/resource/杜昕昱> <http://zh.dbpedia.org/property/玩> ?Q}"
    l=list(g.query(search))
    print(l)

def sparQLSearch(s,v,file):
    rule=re.compile('\'(.*?)\'')
    result=[]
    g = rdflib.Graph()
    g.parse(file, format="xml")
    search = "select "+v+" where{"+s+"}"
    l = list(g.query(search))
    print(l)
    for ll in l:
        filt=rule.findall(str(ll))
        for f in filt:
            result.append(f.split('/')[-1])
    print("search result! ",s,result)
    return result

def sparqlPairSearch(s,v,file):
    rule = re.compile('\'(.*?)\'')
    result = []
    g = rdflib.Graph()
    g.parse(file, format="xml")
    search = "select " + v + " where{" + s + "}"
    l = list(g.query(search))
    print(l)
    for pair in l:
        filtpair=[]
        p0=pair[0].split('/')[-1]
        p1=pair[1].split('/')[-1]
        filtpair.append(p0)
        filtpair.append(p1)
        result.append(filtpair)
    print("search result! ", s, result)
    return result

if __name__=='__main__':
    #sparQLSearch('?V1 <http://dbpedia.org/property/birthPlace> <http://dbpedia.org/resource/Vanua_Balavu>','?V1','En_triple.rdf')
    trainList=[]
    with open('data/en_en_zh.txt', "r",encoding='UTF-8')as trainQuestion:
        for line in trainQuestion:
            route=line.split('@@@')
            tuple=(route[0],route[1],route[2])
            trainList.append(tuple)
    print('tuple done')
    for i in range(10):
        print(trainList[i])
