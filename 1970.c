#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 105
#define MAX_C 55

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    
    int music_duration[MAX_N];
    for (int i = 0; i < n; i++) {
        scanf("%d", &music_duration[i]);
    }
    
    int max_recording[3] = {0, 0, 0};
    for (int i = 0; i < k; i++) {
        scanf("%d", &max_recording[i]);
    }
    
    // preenche os cartuchos restantes com 0
    for (int i = k; i < 3; i++) {
        max_recording[i] = 0;
    }
    
    int c1 = max_recording[0];
    int c2 = max_recording[1];
    int c3 = max_recording[2];
    
    // ordena músicas em ordem decrescente (bubble sort)
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (music_duration[i] < music_duration[j]) {
                int temp = music_duration[i];
                music_duration[i] = music_duration[j];
                music_duration[j] = temp;
            }
        }
    }
    
    // DP: dp[cap1][cap2][cap3] = máximo de minutos gravados
    int dp[MAX_C][MAX_C][MAX_C];
    memset(dp, -1, sizeof(dp));
    dp[c1][c2][c3] = 0;
    int max_minutes = 0;
    
    for (int idx = 0; idx < n; idx++) {
        int duration = music_duration[idx];
        int new_dp[MAX_C][MAX_C][MAX_C];
        memcpy(new_dp, dp, sizeof(dp));
        
        for (int rem1 = 0; rem1 <= c1; rem1++) {
            for (int rem2 = 0; rem2 <= c2; rem2++) {
                for (int rem3 = 0; rem3 <= c3; rem3++) {
                    if (dp[rem1][rem2][rem3] != -1) {
                        int current = dp[rem1][rem2][rem3];
                        if (current > max_minutes) max_minutes = current;
                        
                        if (rem1 >= duration) {
                            int new_val = current + duration;
                            if (new_val > new_dp[rem1 - duration][rem2][rem3]) {
                                new_dp[rem1 - duration][rem2][rem3] = new_val;
                            }
                        }
                        
                        if (rem2 >= duration) {
                            int new_val = current + duration;
                            if (new_val > new_dp[rem1][rem2 - duration][rem3]) {
                                new_dp[rem1][rem2 - duration][rem3] = new_val;
                            }
                        }
                        
                        if (rem3 >= duration) {
                            int new_val = current + duration;
                            if (new_val > new_dp[rem1][rem2][rem3 - duration]) {
                                new_dp[rem1][rem2][rem3 - duration] = new_val;
                            }
                        }
                    }
                }
            }
        }
        memcpy(dp, new_dp, sizeof(dp));
    }
    
    // verifica o estado final
    for (int rem1 = 0; rem1 <= c1; rem1++) {
        for (int rem2 = 0; rem2 <= c2; rem2++) {
            for (int rem3 = 0; rem3 <= c3; rem3++) {
                if (dp[rem1][rem2][rem3] > max_minutes) {
                    max_minutes = dp[rem1][rem2][rem3];
                }
            }
        }
    }
    
    printf("%d\n", max_minutes);
    return 0;
}