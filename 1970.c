#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NUM_MUSICS 100
#define MAX_DURATION 50
#define MAX_CARTRIFGE 3

int main() {
    int n, k, i, j;
    scanf("%d %d", &n, &k);

    // leitura da duração das músicas
    int music_duration[MAX_NUM_MUSICS];
    for (i = 0; i < n; i++)
    {
        scanf("%d", &music_duration[i]);
    }

    // leitura da duração dos cartuchos
    int max_recording[MAX_CARTRIFGE] = {0, 0, 0};
    for (i = 0; i < k; i++)
    {
        scanf("%d", &max_recording[i]);
    }

    // preenche os cartuchos restantes com 0
    for (int i = k; i < 3; i++) {
        max_recording[i] = 0;
    }

    int cartridge1 = max_recording[0];
    int cartridge2 = max_recording[1];
    int cartridge3 = max_recording[2];

    // ordena músicas em ordem decrescente (bubble sort)
    for (i = 0; i < n - 1; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (music_duration[i] < music_duration[j])
            {
                int temp = music_duration[i];
                music_duration[i] = music_duration[j];
                music_duration[j] = temp;
            }
        }
    }

    // DP: dp[cap1][cap2][cap3] = máximo de minutos gravados
    int dp[MAX_DURATION][MAX_DURATION][MAX_DURATION];
    memset(dp, -1, sizeof(dp));
    dp[cartridge1][cartridge2][cartridge3] = 0;
    int max_minutes = 0;

    // para cada música
    for (int idx = 0; idx < n; idx++) {
        int duration = music_duration[idx];
        int new_dp[MAX_DURATION][MAX_DURATION][MAX_DURATION];
        memcpy(new_dp, dp, sizeof(dp));

        for (int rem1 = 0; rem1 <= cartridge1; rem1++)
        {
            for (int rem2 = 0; rem2 <= cartridge2; rem2++)
            {
                for (int rem3 = 0; rem3 <= cartridge3; rem3++)
                {
                    if (dp[rem1][rem2][rem3] != -1) {
                        int current = dp[rem1][rem2][rem3];
                        if (current > max_minutes)
                        {
                            max_minutes = current;
                        }

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
    for (int rem1 = 0; rem1 <= cartridge1; rem1++)
    {
        for (int rem2 = 0; rem2 <= cartridge2; rem2++)
        {
            for (int rem3 = 0; rem3 <= cartridge3; rem3++)
            {
                if (dp[rem1][rem2][rem3] > max_minutes) {
                    max_minutes = dp[rem1][rem2][rem3];
                }
            }
        }
    }

    printf("%d\n", max_minutes);
    return 0;
}