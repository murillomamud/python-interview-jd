from test import calculate

tests = ['AAAABAAAA','ABBA','BAAB','AABB','ABAB','AAAA','AAAAAAAAAAABBBBBBBBAAAAAAAAABABABABAAAAAAAAAAB']
results = [6,1,1,2,0,3,34]
count = 0
if __name__ == '__main__': 
    for letters in tests:     
        print('----------------------------------------------------------')
        print('Testing: ' + str(count))            
        if calculate(letters) == results[count]:
            print(letters + ' - ' + 'OK ' + str(calculate(letters)))
        else:
            print(letters + ' - ' + 'ERROR ' + str(calculate(letters)))
        
        count += 1
