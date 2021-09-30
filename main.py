def function(x,y):
    count = 1
    overallcount = 1
    while overallcount <= y:
        while count <= x:
            print(count)
            count += 1
        overallcount += 1
        count = 1
    
function(10,10)
