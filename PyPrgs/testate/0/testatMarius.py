dictionary = {123:("1", "3"), 1234:"2"}

def testat1(dictionary : dict) -> dict:
    "kürzt keys, macht bei doppelten keys n tupel aus values"
    newdictionary = {}
    for ele in dictionary:
        newkey = str(ele)[:3]
        value = dictionary[ele]
        if newkey not in newdictionary:
            newdictionary[newkey] = value
        else:
            if not isinstance(newdictionary[newkey],tuple):
                newdictionary[newkey] = tuple(sorted((newdictionary[newkey],) + (dictionary[ele],)))
            else:
                newdictionary[newkey] = tuple(sorted((newdictionary[newkey]) + (dictionary[ele],)))

    return newdictionary
        
print(testat1(dictionary))