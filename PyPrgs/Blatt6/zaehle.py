import sys

def main(words):
    count = {}
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word] = 1

    biggest = max(count.values())
    ret = []
    
    for key in count:
        if count[key] is biggest:
            ret.append(key)

    ret = sorted(ret)
        
    print(ret, biggest)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        raise Exception("not enough arguments provided")