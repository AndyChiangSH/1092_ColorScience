# 2.2_給定 (n, k, m)，請寫一個程式 ，請寫一個程式 program_2，求出索引序列 element(𝑒0, 𝑒1, …, 𝑒𝑘−1)。

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


# main
print("please input n, k, m：")

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

# 取 m 的雙數 d
d = combination(n, k)-1-m
sk = n

# 貪婪演算法，求出組合序列(n, k, d)，存入list中
cobi = list()
for i in range(k, 0, -1):
    for j in range(sk-1, i-2, -1):
        if combination(j, i) <= d:
            cobi.append(j)
            d = d-combination(j, i)
            sk = j
            break

# # 印出組合序列
# for x in cobi:
#     print(x, end=" ")

elem = [(n-1)-x for x in cobi]  # 索引序列為(n-1)-組合序列

# 印出索引序列
for x in elem:
    print(x, end=" ")
