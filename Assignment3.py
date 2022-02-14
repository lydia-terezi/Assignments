txt_file = open("C:\\Users\\lyndo\\PycharmProjects\\Project_unipi\\two_cities_ascii.txt", "r")
# Letters and spaces
content = txt_file.read()
char_allowed = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
content = ''.join(filter(char_allowed.__contains__, content))
# Word splitting
content = content.split(" ")
i = 1
while i <= (len(content)-1):
    if len(content[i-1]) + len(content[i]) == 20:
        content.remove(content[i-1])
        content.remove(content[i])
    else:
        i += 2
# Statistics
  # Max letter count
max_letters = len(max(content, key=len))
letters = 1
while letters <= max_letters:
    words = 0
    i = 0
    while i <= (len(content)-1):
        if len(content[i]) == letters:
            words += 1
        i += 1
    print("There are ", words, " words with ", letters, " letter(s)")
    letters += 1
txt_file.close()
