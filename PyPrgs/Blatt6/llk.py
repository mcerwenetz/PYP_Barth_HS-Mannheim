import sys
def main(args):
    newwords = []
    for word in args:
        count={}
        newword = []
        for char in word:
            if char not in count:
                count[char] =1
            else:
                count[char] +=1
        
        for char in word:
            if char not in newword:
                if count[char] > 1:
                    newword.append(char)
                    newword.append(str(count[char]))
                else:
                    newword.append(char)
        newwordstring = "".join(newword)
        newwords.append(newwordstring)
    return newwords
    


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(main(sys.argv[1:]))
    else:
        raise Exception("not enough arguments provided")