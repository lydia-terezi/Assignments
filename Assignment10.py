file = open("C:\\Users\\lyndo\\PycharmProjects\\Project_unipi\\two_cities_ascii.txt", "r")

# file to list
content = file.read()

# string to binary
val = []
binary = []
for i in content:
    val.append(ord(i))
for i in val:
    binary.append(bin(i)[2:])
for i in range(len(binary)-1):
    if len(binary[i]) < 7:
        d = 7 - len(binary[i])
        while d > 0:
            binary[i] = "0" + binary[i]
            d -= 1

# div binary
binary = "".join(binary)
n = 16
binary = [binary[i:i+n] for i in range(0, len(binary), n)]
# str to int
for i in range(len(binary)-1):
    binary[i] = int(binary[i])
# a,b,c,d
even = 0
d3 = 0
d5 = 0
d7 = 0
for i in range(len(binary)-1):
    if binary[i] % 2 == 0:
        even += 1
    if binary[i] % 3 == 0:
        d3 += 1
    if binary[i] % 5 == 0:
        d5 += 1
    if binary[i] % 7 == 0:
        d7 += 1
per_e = 0
per_3 = 0
per_5 = 0
per_7 = 0
if even != 0:
    per_e = (even/(len(binary)-1))*100
if d3 != 0:
    per_3 = (d3/(len(binary)-1))*100
if d5 != 0:
    per_5 = (d5/(len(binary)-1))*100
if d7 != 0:
    per_7 = (d7/(len(binary)-1))*100
print(per_e, "% of the numbers are evenly divisible by 2\n",
      per_3, "% of the numbers are evenly divisible by 3\n",
      per_5, "% of the numbers are evenly divisible by 5\n",
      per_7, "% of the numbers are evenly divisible by 7")
file.close()
