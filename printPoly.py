#Input values into the list
a = []

def printPoly(poly):
    vysledek = []
    for i in range(len(poly)):
        if poly[i] == 0:
            continue
        elif len(vysledek) == 0:
            if i == 0:
                if poly[i] > 0:
                    vysledek.append(str(poly[i]))
                else:
                    vysledek.append("-")
                    vysledek.append(str(abs(poly[i])))
            elif i == 1:
                if poly[i] == 1:
                    if poly[i] > 0:
                        vysledek.append("x")
                    else:
                        vysledek.append("-")
                        vysledek.append("x")
                else:
                    if poly[i] > 0:
                        vysledek.append(f"{poly[i]}x")
                    else:
                        vysledek.append("-")
                        vysledek.append(f"{abs(poly[i])}x")
            else:
                if poly[i] == 1:
                    if poly[i] > 0:
                        vysledek.append(f"x^{i}")
                    else:
                        vysledek.append("-")
                        vysledek.append(f"x^{i}")
                else:
                    if poly[i] > 0:
                        vysledek.append(f"{poly[i]}x^{i}")
                    else:
                        vysledek.append("-")
                        vysledek.append(f"{abs(poly[i])}x^{i}")
        else:
            if i == 1:
                if poly[i] == 1:
                    if poly[i] > 0:
                        vysledek.append("+")
                        vysledek.append("x")
                    else:
                        vysledek.append("-")
                        vysledek.append("x")
                else:
                    if poly[i] > 0:
                        vysledek.append("+")
                        vysledek.append(f"{poly[i]}x")
                    else:
                        vysledek.append("-")
                        vysledek.append(f"{abs(poly[i])}x")
            else:
                if poly[i] == 1:
                    if poly[i] > 0:
                        vysledek.append("+")
                        vysledek.append(f"x^{i}")
                    else:
                        vysledek.append("-")
                        vysledek.append(f"x^{i}")
                else:
                    if poly[i] > 0:
                        vysledek.append("+")
                        vysledek.append(f"{poly[i]}x^{i}")
                    else:
                        vysledek.append("-")
                        vysledek.append(f"{abs(poly[i])}x^{i}")
    
    return " ".join(vysledek)

print(printPoly(a))
