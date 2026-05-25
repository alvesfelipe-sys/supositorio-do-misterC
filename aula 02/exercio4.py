temperaturas = (36.5, 37.2, 38.0, 36.8, 39.1)
for temp in temperaturas:
    if temp < 37.5:
        print(temp, "-> Normal")           # 36.5 -> Normal
                                           # 37.2 -> Normal
                                           # 36.8 -> Normal
    elif temp <= 38.5:
        print(temp, "-> Febre moderada")   # 38.0 -> Febre moderada
    else:
        print(temp, "-> Febre alta")       # 39.1 -> Febre alta
