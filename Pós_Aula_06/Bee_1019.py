s = int(input())
hr = s // 3600
min = (s - (hr * 3600)) // 60
s = s - (hr*3600) - (min*60)

print(f'{hr}:{min}:{s}')

# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.