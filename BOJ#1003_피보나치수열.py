import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  fibo = [ [0,0] for i in range(n+1) ] 
  # print(fibo)
  fibo[0][0] = 1
  if n > 0:
    fibo[1][1] = 1
  for i in range(2, n+1):
    fibo[i] = [ fibo[i-1][0] + fibo[i-2][0],  fibo[i-1][1] + fibo[i-2][1] ]
  print( fibo[n][0], fibo[n][1] )
  # print( fibo )
