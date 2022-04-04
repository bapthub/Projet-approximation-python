def genererPoint(N, incertitude, borneX, borneY):
  if (borneX[1] - borneX[0] < N):
    print("N ne peut pas être plus grand que ", borneX[1] - borneX[0])
    return []
  X = np.arange(borneX[0], borneX[1])
  shuffle(X)
  X = X[:N]
  X.sort()
  Y = [randint(borneY[0], borneY[1]) + random_sample()]
  while (len(Y) < N):
    add = random_sample() * incertitude
    inf = Y[-1] - add if Y[-1] - add > borneY[0] else borneY[0]
    sup = Y[-1] + add if Y[-1] + add < borneY[1] else borneY[1]
    if (randint(2) == 0):
      Y.append(inf)
    else:
      Y.append(sup)
  return X, Y