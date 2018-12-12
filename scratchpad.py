def dpMakeChange(coinValueList, change, minCoins):
   for cents in range(change+1):
      coinCount = cents
      l = [c for c in coinValueList if c <= cents]
      for j in l:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
      minCoins[cents] = coinCount
   return minCoins[change]

coins = [1, 5, 10, 25]

change = 7
min_coins = [0] * (change + 1)

print(dpMakeChange(coins, change, min_coins))
