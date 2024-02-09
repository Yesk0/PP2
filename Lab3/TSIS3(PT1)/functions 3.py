def solve(numheads, numlegs):
     chicken = 2
     rabbit = 4
     numc = 0
     numr = 0

     for i in range(1, numheads+1):
        numc = numheads - i
        numr = i
        if(numc + numr == numheads and (((chicken * numc) + (rabbit * numr))==numlegs)):
            print("Rabbits: ", numr)
            print("Chicken: ", numc)
            break
numheads = 70
numlegs = 188
solve(numheads, numlegs)
          