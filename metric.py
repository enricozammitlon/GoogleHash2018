def distance(loc_one,loc_two):
    dist=abs(loc_one[0]-loc_two[0])+abs(loc_one[1]-loc_two[1])
    return dist

print(distance([3,6],[7,8]))
