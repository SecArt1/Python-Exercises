

nums_rng = range(1 , 21)

nums_list = []

for nums in nums_rng :
    if nums < 10 :
        
        if nums == 6  or nums ==8 or nums ==12: 
            continue
        
        lums = str(nums) 
        print(f'"{str(lums.zfill(2))}"')
        
    else :
        print(f'"{nums}"')    

else : 
    print('"All Numbers Printed"')
