
total_input = input()
input_array=[]
for i in range(0, int(total_input)):
    a = input()
    input_array.append(a)
    

for i in input_array:
    total_students = int(i.split()[0])
    target_score =list(map(lambda a: int(a), i.split()[1:len(i.split())]))
    
    target_avg = sum(list(map(lambda a: a, target_score))) / total_students
    target_avg = int(target_avg)
    over_than_avg_array = list(filter(lambda x : x > target_avg, target_score))
    answer = len(over_than_avg_array)/total_students * 100
    print("%0.3f%%"%answer)