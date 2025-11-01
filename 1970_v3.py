def main():
    import sys
    
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    songs = list(map(int, data[2:2+n]))
    capacities = list(map(int, data[2+n:2+n+k]))
    
    # Preenche com zeros se tiver menos de 3 cartuchos
    while len(capacities) < 3:
        capacities.append(0)
    
    cap1, cap2, cap3 = capacities
    
    # DP iterativa - usa apenas 2 arrays alternados para economizar memória
    dp = [[[False] * (cap3 + 1) for _ in range(cap2 + 1)] for _ in range(cap1 + 1)]
    dp[0][0][0] = True
    
    for song in songs:
        # Cria nova matriz baseada na anterior
        new_dp = [[[False] * (cap3 + 1) for _ in range(cap2 + 1)] for _ in range(cap1 + 1)]
        
        for c1 in range(cap1 + 1):
            for c2 in range(cap2 + 1):
                for c3 in range(cap3 + 1):
                    if dp[c1][c2][c3]:
                        new_dp[c1][c2][c3] = True
                        if c1 + song <= cap1:
                            new_dp[c1 + song][c2][c3] = True
                        if c2 + song <= cap2:
                            new_dp[c1][c2 + song][c3] = True
                        if c3 + song <= cap3:
                            new_dp[c1][c2][c3 + song] = True
        
        dp = new_dp
    
    # Encontra o máximo
    max_minutes = 0
    for c1 in range(cap1 + 1):
        for c2 in range(cap2 + 1):
            for c3 in range(cap3 + 1):
                if dp[c1][c2][c3]:
                    max_minutes = max(max_minutes, c1 + c2 + c3)
    
    print(max_minutes)

if __name__ == "__main__":
    main()