# looping through a Dictionary
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

ranks_nums = {
    'A' : 100 ,
    'B' : 80 ,
    'C' : 40 ,
}

a=0

for ranks_kys , ranks_valus ,in my_ranks.items() :
 
       
    print(f"My Rank in {ranks_kys} Is {ranks_valus} And This Equal {ranks_nums[ranks_valus]} Points")
    a += ranks_nums[ranks_valus]
    
else : 
    print(f"Total Points Is {a}")
