import time
import os
import random
clear = 'cls' if os.name == 'nt' else 'clear'
x = " "
N = input("qual seu apelido jogador 1 digite 5 letras ou menos ")
N2 = input("qual seu apelido jogador 2 digite 5 letras ou menos ")
for c in range(20):
    os.system('cls')
    print(x + "▆▆▆▆▆▆▆▆▆▆▆▆▆")
    print(x + "▆   ",N,"   ▆ ")
    print(x + "▆             ▆ ")
    print(x + "▆             ▆" )
    print(x + "▆▆▆▆◯▆▆▆▆▆◯▆▆▆▆")
    x = x + random.choice([ " ", "  ", "   "])
    time.sleep(0.1)
    print(x + "▆▆▆▆▆▆▆▆▆▆▆▆▆")
    print(x + "▆   ",N2,"   ▆ ")
    print(x + "▆             ▆ ")
    print(x + "▆             ▆" )
    print(x + "▆▆▆▆◯▆▆▆▆▆◯▆▆▆▆")
    x = x + random.choice([ " ", "  ", "   "])
    time.sleep(0.1)
    