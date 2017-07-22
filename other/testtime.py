import time, json, platform, sys


def count_time(n=int(sys.argv[1])):

    start = time.time()
    r = 5
    y = 0
    s = 500

    store = []

    for i in range(n):
        
        a = str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.') + ' ' + str(y + r).rstrip('0').rstrip('.')
        b = str(y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(y + r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.')
        c = str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(s + y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.') + ' ' + str(s + y + r).rstrip('0').rstrip('.')
        d = str(s + y - r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i - r).rstrip('0').rstrip('.') + ' ' + str(s + y + r).rstrip('0').rstrip('.') + ' ' + str(s / (n - 1) * i + r).rstrip('0').rstrip('.')
        
        st = [a,b,c,d]
        
        for ele in st:
            if ele not in store:
                #print(ele)
                #print('printed')
                store.append(ele)
                
        #print('\n\n\n')
        #print('end')



    store2 = [[float(y) for y in x.split()] for x in store]
    store3 = [[z[0]/2+z[2]/2,z[1]/2+z[3]/2] for z in store2]
    store5 = []

    for pos in store3:
        for pos2 in store3:
            if pos[0] != pos2[0] and pos[1] != pos2[1]:
                arr = pos+pos2
                
                if [arr[2],arr[3],arr[0],arr[1]] not in store5:
                    
                    #print('\n\n\n')
                    #print(pos[0] != pos2[0])
                    #print('\n\n\n')
                    #print(pos[1] != pos2[1])
                    #print('\n\n\n')
                    #print(tuple(pos+pos2))
                    #print('\n\n\n')
                    
                    store5.append(arr)
                    

    print('Store5 length: '+str(len(store5)))
    print('Canvas size: '+str(n))
    end = time.time()
    print('Time it took to run: '+str(round(end - start))+' s\n')
    return {'time':end - start,'store_len':len(store5)}
    
points = [count_time(x+2) for x in range(int(sys.argv[2]))]

with open('./json/'+platform.node()+'.json','w') as out:
    json.dump({'points':points},out,indent=4)
