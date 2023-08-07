import random
from guess import cek

jawaban = random.randint(1,10)

tebakan =int(input('tebak 1-10:'))


if cek(tebakan, jawaban):
    print("jawaban kamu benar!")
else:
    print("jawaban kamu salah!")
