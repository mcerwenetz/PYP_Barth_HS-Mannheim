x = 10
epsilon = 1e-10

a0 = (1+x)/2

aprev = a0

while True:
    anext= (aprev + (x)/aprev)/2
    if (aprev - anext) < epsilon:
        break
    aprev = anext

print(anext)
