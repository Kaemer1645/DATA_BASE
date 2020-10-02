dict = {'Justyna':'08-04-1998','Szymon':'11-02-1997','Amadeusz':'11-11-2001'}

list = []
for name,date in dict.items():
    list.append((''.join(str(name)),''.join(str(date))))


print(list)