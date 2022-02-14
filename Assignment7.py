file = open("two_cities_ascii.txt", "r")
# lines to dictionaries
data = file.read().splitlines()
while '' in data:
    data.remove('')
d_list = []
n = 1
for i in range(len(data)-1):
    d_list.append({"line": n, "content": data[i]})
    n += 1
# user input
print("Available keys: line,content\n")
key = input("Enter key: ")
if key == "line":
    print("Max value: ", len(data)-1, "\nMin value: ", 1)
elif key == "content":
    max_value = d_list[0]["content"]
    min_value = d_list[0]["content"]
    for i in range(len(d_list)-2):
        if len(d_list[i]["content"]) < len(d_list[i+1]["content"]):
            max_value = d_list[i+1]["content"]
    for i in range(len(d_list) - 2):
        if len(d_list[i]["content"]) > len(d_list[i+1]["content"]):
            min_value = d_list[i+1]["content"]
    print("Max value: ", max_value, "\nMin value: ", min_value)
else:
    print("Invalid key")
file.close()