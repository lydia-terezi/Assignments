import ast
from urllib.request import Request, urlopen
# Latest round
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data_d = data.decode('ASCII')
data_d = ast.literal_eval(data_d)
binary = data_d["randomness"]
# 100 rounds
r = data_d["round"]-1
for i in range(99):
    req_99 = Request('https://drand.cloudflare.com/public/' + str(r), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data_99 = urlopen(req_99).read()
    data_d99 = data_99.decode('ASCII')
    data_d99 = ast.literal_eval(data_d99)
    binary += data_d99["randomness"]
    r -= 1
# randomness to binary
val = ''
for i in binary:
    val += str(bin(ord(i))[2:])
# max sequences
num_0 = []
c = 0
for i in val:
    if i == "0":
        c += 1
    else:
        num_0.append(c)
        c = 0
print("The length of the longest sequence of 0s is", max(num_0))
num_1 = []
c = 0
for i in val:
    if i == "1":
        c += 1
    else:
        num_1.append(c)
        c = 0
print("The length of the longest sequence of 1s is", max(num_1))
