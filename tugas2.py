e = 2.71828
lamda_t = float(input("masukkan nilai lamda t : "))
M = int(input("masukkan nilai M       : "))
print("")
print("misalkan N(t) adalah variabel acak poisson dengan parameter lamda_t > 0 sehingga : ")
print("-----------------------------------------------------------------------------------")
print(f"{'n':>3} | {'P(N(t) = n)' :>15}")
print("-" * 22)
for n in range (M + 1) :
    faktorial = 1
    for i in range (1, n + 1) :
        faktorial *= i
    problem = (e ** (-lamda_t)) * (lamda_t ** n) / faktorial
    print(f"{n :> 3} | {problem : 15.5f}")