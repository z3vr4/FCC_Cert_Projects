import numpy as np

def calculate(list):
  # Aarr - plain list || Barr - 2d || Carr - transposed Barr || Darr - All arrays
  Aarr = list
  Barr = []  # our (future) 3x3 array
  calcs = [[[], []], [[], []], [[], []], [[], []], [[], []], [[], []]]
  # required to raise error if length of list over 9
  if len(Aarr) != 9:
    raise ValueError("List must contain nine numbers.")

  # mean - variance - standard deviation - max - min - sum

  # IMPORTANT: order of return goes like this (in the dict):
  # 'sum': [[columns], [row], flat]

  # Creating our Barr, also creating a transposed version to work with later
  for i in range(0, len(Aarr), 3):
    Barr.append(np.array(Aarr[i:i + 3]))
  Carr = np.array(Barr).T
  Darr = [Carr, Barr, Aarr]

  lpi = 0  # loop counter, important for everything DO NOT DELETE
  # Friendly reminder of our calcs indices:
  # 0 - mean, 1 - variance, 2 - std_deviation, 3 - max, 4 - min, 5 - sum
  # BIG MAIN for loop
  for Iarr in Darr:

    #means
    if lpi != 2:
      for i in range(3):
        calcs[0][lpi].append(np.mean(Iarr[i]))
    elif lpi == 2:
      calcs[0].append(np.mean(Iarr))

    #variances
    if lpi != 2:
      for i in range(3):
        calcs[1][lpi].append(np.var(Iarr[i]))
    elif lpi == 2:
      calcs[1].append(np.var(Iarr))

    #standard deviation
    if lpi != 2:
      for i in range(3):
        calcs[2][lpi].append(np.std(Iarr[i]))
    elif lpi == 2:
      calcs[2].append(np.std(Iarr))

    #max
    if lpi != 2:
      for i in range(3):
        calcs[3][lpi].append(np.max(Iarr[i]))
    elif lpi == 2:
      calcs[3].append(np.max(Iarr))

    #max
    if lpi != 2:
      for i in range(3):
        calcs[4][lpi].append(np.min(Iarr[i]))
    elif lpi == 2:
      calcs[4].append(np.min(Iarr))

    #sum
    if lpi != 2:
      for i in range(3):
        calcs[5][lpi].append(np.sum(Iarr[i]))
    elif lpi == 2:
      calcs[5].append(np.sum(Iarr))

    lpi += 1

  finaldict = {}
  finaldict['mean'] = calcs[0]
  finaldict['variance'] = calcs[1]
  finaldict['standard deviation'] = calcs[2]
  finaldict['max'] = calcs[3]
  finaldict['min'] = calcs[4]
  finaldict['sum'] = calcs[5]

  return finaldict
