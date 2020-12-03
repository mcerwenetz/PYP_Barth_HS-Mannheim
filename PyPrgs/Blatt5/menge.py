class Set():

    def __init__(self, liste=None):
        self.runningIndex=0
        self.liste=[]
        if liste is not None:
            for ele in liste:
                self.add(ele)
    
    def add(self, elem):
        if elem not in self.liste:
            self.liste.append(elem)

    def union_update(self, seq):
        for ele in seq:
            self.add(ele)

    def union(self, seq):
        neuesSet = Set(self.liste)
        neuesSet.unionupdate(seq)
        return neuesSet

    def __len__(self):
        return len(self.liste)
    
    def __iter__(self):
        return self

    def __next__(self):
        self.runningIndex+=1
        if self.runningIndex < len(self.liste):
            return self.liste[self.runningIndex]
        else:
            raise StopIteration

    def __contains__(self, ele):
        if ele in self.liste:
            return True
        else:
            return False

    def __ne__(self, other):
        if len(self.liste) != len(other.liste):
            return True
        else:
            for elem in self.liste:
                if elem not in other.liste:
                    return False
        return False

    def __eq__(self, other):
        return not (self != other)

    def remove(self, elem):
        if elem in self.liste:
            self.liste.remove(elem)


    
if __name__ == "__main__":
    s1 = Set()
    s1.add([1,2,3])
    s2 = Set()
    s2.add([2,3,4])
    s3 = s1.union(s2.liste)
    print(s3.liste)
