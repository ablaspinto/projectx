
def linear_search(list,target):
    for i in range(len(list)-1):
        if list[i] == target:
            return list[i]
        

def main():
    lst = [1,245,5,6,7,2,5,]
    print(linear_search(lst , 5))
    

main()
    
