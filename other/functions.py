

def comb(l):
    buff = []
    
    def helper(arr,s,c):
        
        if len(arr) == 1:
            print(c+[s])
            buff.append(c+[s])
        else:
            exc = arr[:]
            exc.remove(s)
            
            for item in exc:
                
                helper(exc,item,c+[s])
    
    for it in l:
        helper(l,it,[])
    
    return buff

#print(len(comb([1,2,3,4])))


def rec_line(l):
    global count
    
    print(l)
    if len(l) > 2:
        first_item = l[0]
        l2 = l[1:]
        
        for pos in l2:
            #combs = [[x+y for y in get_combinations(pos)] for x in get_combinations(first_item)]
            #combs = combs[0] + combs[1]
            
            combs = get_combinations(first_item+pos)
            
            for comb in combs:
                count = count + 1
                
                if comb[0] != comb[2] and comb[1] != comb[3]:
                
                    filler = (round(first_item[0]),round(first_item[1]),round(pos[1]),255)
                    draw2.line(tuple(comb), fill=filler)
                
                
        rec_line(l2)
    else:
        
        draw2.line((l[0][0],l[0][1],l[1][0],l[1][1]), fill=(0,0,0,0))


def get_slope(coor):
    print(coor)
    print((coor[1]-coor[3])/(coor[0]-coor[2]))
    return (coor[1]-coor[3])/(coor[0]-coor[2])
    
def near_point(point, bound, line):
    slope = (line[1]-line[3])/(line[0]-line[2])
    b_component = point[1]-slope*point[0]
    test_line = point[0]*slope+b_component
    
    return test_line

