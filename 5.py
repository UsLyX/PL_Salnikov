N = int(input('Введите ограничивающее число: '))
i = 1

while(i <= N):
    if(i*i <= N):
        print(i*i)
        i += 1
    else:  
        break;    
