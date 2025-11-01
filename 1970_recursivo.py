def main():
    n, k = map(int, input().split())
    songs = list(map(int, input().split()))
    caps = list(map(int, input().split())) + [0] * (3 - k)
    c1, c2, c3 = caps
    
    def dfs(i, cap1, cap2, cap3):
        if i == len(songs):
            return 0
        
        best = dfs(i + 1, cap1, cap2, cap3)  # Skip
        
        if cap1 >= songs[i]:
            best = max(best, songs[i] + dfs(i + 1, cap1 - songs[i], cap2, cap3))
        if cap2 >= songs[i]:
            best = max(best, songs[i] + dfs(i + 1, cap1, cap2 - songs[i], cap3))
        if cap3 >= songs[i]:
            best = max(best, songs[i] + dfs(i + 1, cap1, cap2, cap3 - songs[i]))
        
        return best
    
    print(dfs(0, c1, c2, c3))

if __name__ == "__main__":
    main()