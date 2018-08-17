def bubbur(a_list):
    for i in range(0,len(a_list)):
        for j in range(0,len(a_list)-1):
            if a_list[j]>a_list[j+1]:
                a_list[j],a_list[j+1] = a_list[j+1],a_list[j]
    return a_list

if __name__ == '__main__':
    print(bubbur([1,421,434,12,4,23,423]))

