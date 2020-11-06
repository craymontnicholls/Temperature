def CtoF(C):
  return (C * 1.8) + 32


def FtoC(F):
  return (F / 1.8) - 32


C = 30

F = CtoF(C)


print(C ,"degress C is", F,"degress F")