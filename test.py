lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
 
def modificar(lista):
    lst = list(set(lista))
    print(lst)
    for i,n in enumerate(lst):
        print(f"lst[{i}] -> {n}%2 => {n%2}")
        if n%2 == 1:
            lst.remove(n)
            print("\tBorrando el ", n, "quedan", lst)
    lst.sort(reverse=True)        
    lst.insert(0,sum(lst))
    print(lst)
 
modificar(lista)