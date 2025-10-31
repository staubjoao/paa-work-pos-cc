# leitura dos dados de entrada
n, k = map(int, input().split())
music_duration = list(map(int, input().split()))
max_recording = list(map(int, input().split()))
    
# preenche os cartuchos restantes com 0
while len(max_recording) < 3:
  max_recording.append(0)
    
# programação dinâmica com memoização
memo = {}
# idx: índice da música atual
# cap1, cap2, cap3: capacidades restantes dos cartuchos
def dp(idx, cap1, cap2, cap3):
  if idx == n:
    return 0
        
  state = (idx, cap1, cap2, cap3)
  if state in memo:
    return memo[state]
        
  # opção 1: não gravar esta música
  max_val = dp(idx + 1, cap1, cap2, cap3)
        
  # opção 2: tentar gravar em cada cartucho
  # obtem a duração da música atual
  duration = music_duration[idx]
  
  # tenta gravar no cartucho 1
  if cap1 >= duration:
      max_val = max(max_val, duration + dp(idx + 1, cap1 - duration, cap2, cap3))
  
  # tenta gravar no cartucho 2
  if cap2 >= duration:
      max_val = max(max_val, duration + dp(idx + 1, cap1, cap2 - duration, cap3))
  
  # tenta gravar no cartucho 3
  if cap3 >= duration:
      max_val = max(max_val, duration + dp(idx + 1, cap1, cap2, cap3 - duration))
  
  # armazena o resultado no memo
  memo[state] = max_val
  # retorna o valor máximo encontrado
  return max_val
    
result = dp(0, max_recording[0], max_recording[1], max_recording[2])
print(result)