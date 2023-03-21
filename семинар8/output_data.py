def ShowAll():
    with open('file.txt','r', encoding='utf-8') as file:
        for line in file:
            print(line)

def Search(name):
    with open('file.txt','r', encoding='utf-8') as file:
        flag = False
        for line in file:
            if name in line:
                print(f'\n {line} \n')
                flag = True
        if flag == False:
            print('\n "не найдено" \n')
        
    return flag