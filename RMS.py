def findProduct(inputGrid, length):
    max_prod = 0
    ctr = 0
    for i in range(length):
        for j in range(length-3):
            prod = inputGrid[i][j]*inputGrid[i][j+1]*inputGrid[i][j+2]
            print(prod)
            ctr += 1
            if prod > max_prod:
                max_prod = prod
            prod = inputGrid[j][i]*inputGrid[j+1][i]*inputGrid[j+2][i]
            print(prod)
            ctr += 1
            if prod > max_prod:
                max_prod = prod
    for i in range(length-3):
        for j in range(length-3):
            prod = inputGrid[i][j]*inputGrid[i+1][j+1]*inputGrid[i+2][j+2]
            print(prod)
            ctr += 1
            if prod > max_prod:
                max_prod = prod
    for i in range(2, length):
        for j in range(length-3):
            prod = inputGrid[i][j]*inputGrid[i-1][j+1]*inputGrid[i-2][j+2]
            print(prod)
            ctr += 1
            if prod > max_prod:
                max_prod = prod
    print("Number of different combinations: ",ctr)
    print("Greatest product of 3 adjacent numbers: ",max_prod)

findProduct([[8,2,22,97,38,15,0,40,0,75],[49,49,99,40,17,81,18,57,60,87],[81,49,31,73,55,79,14,29,93,71],[52,70,95,23,4,60,11,42,69,24],[22,31,16,71,51,67,63,89,41,92],[24,47,32,60,99,3,45,2,44,75],[32,98,81,28,64,23,67,10,26,38],[67,26,20,68,2,62,12,20,95,63],[24,55,58,5,66,73,99,26,97,17],[21,36,23,9,75,0,76,44,20,45]],10)
