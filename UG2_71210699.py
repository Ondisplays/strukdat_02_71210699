import timeit

#iteraktif
print("======Iteratif======")
def fib(n):
    v1, v2, v3 = 1, 1, 0  
    for rec in bin(n)[3:]: 
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2
for i in range (1, 101):
    starttime=timeit.default_timer()
    hasil = fib(i)
    endtime = timeit.default_timer()
    print ("fibonacci ke-",i,"adalah",hasil,"Waktu yang dibutuhkan menggunakan Iterative",endtime-starttime)

print()

#Rekursif
print("=====Rekursif=====")
def rekursi(n):
    if n < 2:
        return n
    return rekursi(n-2) + rekursi(n-1)
for i in range (1, 101):
    starttime=timeit.default_timer()
    hasil = rekursi(i)
    endtime = timeit.default_timer()
    print ("fibonacci ke-",i,"adalah",hasil,"Waktu yang dibutuhkan menggunakan rekursif",endtime-starttime)