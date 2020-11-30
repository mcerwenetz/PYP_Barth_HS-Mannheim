import sys
def main(args):
    newwords = []
    for word in args:
        chars = list(word)
        index1 = 0
        index2 = index1+1
        newword=[]
        while index1 <= len(word)-1:
            
            while index2 <= len(word)-1 and chars[index1] is chars[index2]:
                index2+=1
                
            if index2 - index1 > 1:
                newword.append(str(index2-index1))
            newword.append(chars[index1])

            index1 = index2
            index2+=1
        newwordAsString = "".join(newword)
        newwords.append(newwordAsString)
    return newwords

    


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(main(sys.argv[1:]))
    else:
        raise Exception("not enough arguments provided")