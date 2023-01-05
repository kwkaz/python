# N番目の素数を返す
# エラトステネスのふるいで実装

import time

def prime(N):
    # 見込みでNの20倍の数まで調べる
    MAX_N = N * 20
    prime = [True]*(MAX_N+2)

    # N番目の素数が見つからない場合、-1が返却
    ret = -1
    count = 0

    for i in range(2,MAX_N+1):
        # prime=Falseは素数ではない
        if prime[i] == False:
            continue
        p = i
        count += 1
        # N番目の素数が見つかった場合処理終了
        if count == N:
            ret = i
            break
        # MAX_Nまでの数の倍数を素数から除外
        while p <= MAX_N:
            prime[p] = False
            p += i

    return ret

# N番目を入力
N = int(input())
sttime = time.perf_counter()

print(prime(N))

edtime = time.perf_counter()

print('Time(sec)=>',edtime-sttime)
