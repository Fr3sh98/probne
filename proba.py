import math

a = int(input("Podaj wspolczynnik rowniania a: "))
b = int(input("Podaj wspolczynnik rowniania b: "))
c = int(input("Podaj wspolczynnik rowniania c: "))

d = (b == 0 and
     (a == 0 and
      (c == 0 and ['wiele'] or ['brak'])
      or [-c / (a * 1.0)])
     or
     [
         (a == 0 and [-c / (b * 1.0)] or ['wiele'])
     ])[0]

print d
