# leitura dos dados de entrada
n, k = map(int, input().split())
music_duration = list(map(int, input().split()))
max_recording = list(map(int, input().split()))
    
# preenche os cartuchos restantes com 0
while len(max_recording) < 3:
  max_recording.append(0)
    


capacity1, capacity2, capacity3 = max_recording

# inicializa DP

memo = [[[0] * (capacity3 + 1) for _ in range(capacity2 + 1)] for _ in range(capacity1 + 1)]

for music in music_duration:
  new_memo = [[[0] * (capacity3 + 1) for _ in range(capacity2 + 1)] for _ in range(capacity1 + 1)]

  for i in range(capacity1 + 1):
    for j in range(capacity2 + 1):
      for k in range(capacity3 + 1):
        # armazena o estado atual, pegando do memo
        current = memo[i][j][k]

        # agora são 4 opções, não gravar a musica, gravar no 1, no 2 ou no 3

        # opção 1: não grava esta música
        new_memo[i][j][k] = max(new_memo[i][j][k], current)

        # opção 2: grava no cartucho 1 (se couber)
        if i + music <= capacity1:
          new_memo[i + music][j][k] = max(new_memo[i + music][j][k], current + music)
        
        # opção 3: grava no cartucho 2 (se couber)
        if j + music <= capacity2:
          new_memo[i][j + music][k] = max(new_memo[i][j + music][k], current + music)
        
        if k + music <= capacity3:
          new_memo[i][j][k + music] = max(new_memo[i][j][k + music], current + music)

  memo = new_memo

max_minutes = 0
for i in range(capacity1 + 1):
  for j in range(capacity2 + 1):
    for k in range(capacity3 + 1):
      max_minutes = max(max_minutes, memo[i][j][k])

print(max_minutes)