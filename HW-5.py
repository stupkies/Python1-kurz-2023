
from statistics import mean

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# seznam průměrných teplot pro každý den
prumerne=[round(mean(den), 1) for den in teploty]
print(prumerne)
# seznam ranních teplot
ranni=[den[0] for den in teploty]
print(ranni)
# seznam nočních teplot
nocni=[den[-1] for den in teploty]
print(nocni)
# seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu
poledni_nocni=[[den[1], den[3]] for den in teploty]
print(poledni_nocni)