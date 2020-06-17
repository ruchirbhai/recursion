arr =  [1,1]
k = 0

def check_if_sum_possible(arr, k):
    results = []
    
    check_helper(arr, k, 0, [], results)
    
    if results:
        return True
    else:
        return False

def check_helper(data, target, index, slate, results):
    # base case
    
    if index == len(data) :
        if  target == sum(slate) and slate:
            results.append(slate[:])
            return
    else:
        #recursion
        #left side
        check_helper(data, target, index+1, slate, results)
        
        #right side
        slate.append(data[index])
        check_helper(data, target, index+1, slate, results)
        slate.pop()
    
    return


print(check_if_sum_possible(arr, k))