def paixu(test_list):
    for i in range(0,len(test_list)):
        for j in range(i+1,len(test_list)):
            if test_list[i]>test_list[j]:
                test_list[i],test_list[j] = test_list[j],test_list[i]
    return test_list

if __name__ == '__main__':
    print(paixu([12,321,4,35,2]))
