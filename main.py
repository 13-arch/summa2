input_data = open('input.txt','r')
data = input_data.read()
output_data = open('output.txt','w')
Q = 0
N = int(data)
if N > 0 :
  for i in range(1, N+1):
    Q=Q+i
    
elif N < 0 :
    for i in range(N, 2):
        Q=Q+i
else:
    Q = '1'

output_data.write(str(Q))
output_data.close()
input_data.close()