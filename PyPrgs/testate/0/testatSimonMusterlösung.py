#!/usr/bin/python3

def dictshortstingskeys(dic):
    
    newDic = {}

    for ele in dic:
        newKey = str(ele)[:3]
        newValue = dic[ele]
        if type(newValue) is tuple:
            newValue=list(newValue)
        else:
            newValue = [newValue]
        if newKey not in newDic:
            newDic[newKey] = newValue
        else:
            newDic[newKey] += newValue
            
            
    for ele in newDic:
        if len(newDic[ele]) == 1:
            newDic[ele] = newDic[ele][0]
        else:
            newDic[ele] = tuple(sorted(newDic[ele]))

    return newDic

def main():
    testliste = []
    #dic1 nicht gecovered im orginaltestat
    dic1 =  {12345: (42,43), 12349: (17,19), 12377: 39}
    #alle anderen schon
    dic2 = {12345: 43, 12349: (17,19), 12377: 39}
    dic3 = {12345: 43, 12349: 17, 12377: 39}
    dic4 = {12345: 43}
    testliste.append(dic1)
    testliste.append(dic2)
    testliste.append(dic3)
    testliste.append(dic4)
    for dic in testliste:
        print(dictshortstingskeys(dic))

if __name__ == '__main__':
    main()