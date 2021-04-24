# 2.1_給定 (n,k,m)，請寫一個程式 program_1，可求出組合序列 cobidic(𝑠𝑘,𝑠𝑘−1,…,𝑠1)。

# 計算Cn取m
def combination(n, m):
    if n < m:
        return 0
    else:
        return int((factorial(n)/factorial(m))/factorial(n-m))


# 計算n階層
def factorial(n):
    sum = 1
    for i in range(1, n+1):
        sum = sum*i

    return sum


# 防呆
while True:
    n, k, m = map(int, input().split())

    if not (n >= 1 and n <= 81):
        print("n必須在1~81之間，請再重新輸入一次!")
        continue
    if not (k >= 1 and k <= n):
        print("k必須在1~"+str(n)+"之間，請再重新輸入一次!")
        continue
    if not (m >= 0 and m <= (combination(n, k)-1)):
        print("m必須在0~"+str(combination(n, k)-1)+"之間，請再重新輸入一次!")
        continue
    else:
        break


# 貪婪演算法，求出組合序列，存入list中
cobi = list()
for i in range(k, 0, -1):
    for j in range(n-1, i-2, -1):
        if combination(j, i) <= m:
            print("j = "+str(j))
            print("i = "+str(i))
            print("m = "+str(m))
            print("cobi = "+str(combination(j, i)))
            print("------------")
            cobi.append(j)
            m = m-combination(j, i)
            n = j
            break

# 印出組合序列
for x in cobi:
    print(x, end=" ")
