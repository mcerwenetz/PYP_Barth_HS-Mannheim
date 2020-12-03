class Set:
    def __init__(self, liste=None):
        self.liste=[]
        if liste is not None:
            for ele in liste:
                self.add(liste)
    
    def add(self, elem):
        if elem not in self.liste:
            self.liste.append(elem)

    def unionupdate(self, seq):
        for ele in seq:
            self.add(ele)

    def union(self, seq):
        neuesSet = Set(self.liste)
        neuesSet.unionupdate(seq)
        return neuesSet

    
if __name__ == "__main__":
    s1 = Set()
    s1.add([1,2,3])
    s2 = Set()
    s2.add([2,3,4])
    s3 = s1.union(s2.liste)
    print(s3.liste)
