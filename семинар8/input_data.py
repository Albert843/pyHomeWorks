def AddData(name, number):
    with open('file.txt','a', encoding='utf-8') as file:
        file.write(f'{name} {number} \n')
 
def ChangeData(old_name, new_name, number):
    with open('file.txt','r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('file.txt','w', encoding='utf-8') as file:
        for line in lines:
            if line[0] != old_name:
                file.write(line)
                print(line)
                print(old_name)
    with open('file.txt','a', encoding='utf-8') as file:
        file.write(f'{new_name} {number} изменен \n')       
            
def DeleteData(name, number):
    with open('file.txt','r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('file.txt','w', encoding='utf-8') as file:
        for line in lines:
            print(name)
            print(line)
            if line[0] != name:
                file.write(line)
                print(f'{name} удален')
            

    