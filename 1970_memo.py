def main():
    # leitura dos dados de entrada
    n, k = map(int, input().split())
    music_duration = list(map(int, input().split()))
    max_recording = list(map(int, input().split()))
    
    # preenche os cartuchos restantes com 0
    while len(max_recording) < 3:
        max_recording.append(0)
    
    capacity1, capacity2, capacity3 = max_recording
    
    # dicionário para memoização
    memo = {}
    
    def solution(i, cap1, cap2, cap3):
        # verifica se já calculamos este estado
        state = (i, cap1, cap2, cap3)
        if state in memo:
            return memo[state]
        
        # caso base: processou todas as músicas
        if i == n:
            return 0
        
        # opção 1: não gravar esta música
        result = solution(i + 1, cap1, cap2, cap3)
        
        # opção 2: gravar no cartucho 1 (se couber)
        if cap1 >= music_duration[i]:
            result = max(result, music_duration[i] + solution(i + 1, cap1 - music_duration[i], cap2, cap3))
        
        # opção 3: gravar no cartucho 2 (se couber)
        if cap2 >= music_duration[i]:
            result = max(result, music_duration[i] + solution(i + 1, cap1, cap2 - music_duration[i], cap3))
        
        # opção 4: gravar no cartucho 3 (se couber)
        if cap3 >= music_duration[i]:
            result = max(result, music_duration[i] + solution(i + 1, cap1, cap2, cap3 - music_duration[i]))
        
        # armazena o resultado no memo antes de retornar
        memo[state] = result
        return result
    
    result = solution(0, capacity1, capacity2, capacity3)
    print(result)

if __name__ == "__main__":
    main()