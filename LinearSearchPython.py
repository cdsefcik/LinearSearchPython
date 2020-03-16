

def linearSearch(key, searchlist):

    for i in range(len(searchlist)):

        if searchlist[i] == key:
            return print(i)
        
    return print(key, 'is not in the list')



