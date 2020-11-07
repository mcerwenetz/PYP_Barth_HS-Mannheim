dictionary = {"abcd":(1,2), "abce":(3,4)}

def testat1(dictionary : dict) -> dict:
    "kürzt keys, macht bei doppelten keys n tupel aus values"
    newdictionary = {}
    count = {}
    for ele in dictionary:
        newkey = str(ele)[:3]
        value = dictionary[ele]
        if newkey in count:
            if count[newkey] > 1:
                newdictionary[newkey] = tuple(sorted((newdictionary[newkey], value)))
            else:
                if not isinstance(value, tuple):
                    newdictionary[newkey] = tuple(sorted(newdictionary[newkey] + (value, )))
                else:
                    newdictionary[newkey] = tuple(sorted((newdictionary[newkey], value)))

            count[newkey] +=1
        else:
            newdictionary[newkey] = value
            count[newkey] = 1
    return newdictionary
        
print(testat1(dictionary))