#!/usr/bin/env python3

liste = [1,2]

#Append mit slicing
liste[len(liste):] += [3]

#Append ist destruktiv? Wenn ich id(liste) eingebe, dann bekomm ich auch nach dem append die gleiche id wie vorher. 
#Dann müsste es doch das gleiche Objekt sein?
#Bei dem slicing-operator kommt allerdings auch die gleiche id raus.