fid = open('text_file.txt', 'w')

while True:
    text = input("Введіть дані: ")
    if text == ' ':
        print('Введення даних заврешено!')
        break
    fid.write(text+'\n')

fid.close()
