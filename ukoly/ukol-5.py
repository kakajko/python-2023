teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumerne = [sum(den) / len(den) for den in teploty]

ranni = [den[0] for den in teploty]

nocni = [den[3] for den in teploty]

poledni_nocni = [[den[1], den[3]] for den in teploty]

print("Průměrné denní teploty:", prumerne)
print("Ranní teploty:", ranni)
print("Noční teploty:", nocni)
print("Polední a nočni teploty:", poledni_nocni)
