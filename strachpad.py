# # arr1 = [100,100,200,300,300,400,400]
# # arr2 = [14,90,100,100,200,200,450,450,0,0,0,0,0,0,0]
# # arr1 = [1,3,5]
# # arr2 = [2,4,6,0,0,0]
# arr1 = [1,1,1,1,1,1]
# arr2 = [12,1,1,1,1,1,2,0,0,0,0,0,0]

# # arr1_ptr, arr2_ptr = 0,0
# # while arr2_ptr <= len(arr1) - 1:
# #     if arr2[arr2_ptr] <= arr1[arr1_ptr]:
# #         arr2_ptr += 1
# #     else: # arr2_ptr > arr1_ptr
# #         arr2[arr2_ptr], arr1[arr1_ptr] = arr1[arr1_ptr], arr2[arr2_ptr]
# #         arr2_ptr += 1
# #         arr1.sort()
    
# #     arr2[len(arr1):] = arr1
# # print(arr2)

# ptr1, ptr2 = len(arr1) - 1, len(arr2) -1
# run_ptr = len(arr2) - len(arr1) - 1
# while ptr2 > 0:
#     if arr2[run_ptr] < arr1[ptr1]:
#         arr2[ptr2] = arr1[ptr1]
#         ptr2 -= 1
#         ptr1 -= 1

#     else:
#         arr2[ptr2] = arr2[run_ptr]
#         ptr2 -= 1
#         run_ptr -= 1

# while ptr1 >= 0:
#     arr2[ptr2] = arr1[ptr1]
#     ptr1 -= 1
        

# # ptr1, ptr2 = 0,0
    
# # while ptr2 <= len(arr1) - 1:
# #     if arr2[ptr2] > arr1[0]:
# #         arr2[ptr2], arr1[0] = arr1[0], arr2[ptr2]
# #         ptr2 += 1
# #         # arr1.sort()
# #         while ptr1 < len(arr1) - 1:
# #             if arr1[ptr1] > arr1[ptr1 + 1]:
# #                 arr1[ptr1], arr1[ptr1 + 1] = arr1[ptr1 + 1], arr1[ptr1]
# #                 ptr1 += 1
# #             else: # arr1[ptr1] <= ptr1+1
# #                 ptr1 = 0
# #                 break
# #     else: # arr2 < arr1
# #         ptr2 += 1

# # arr2[len(arr1):] = arr1
# print(arr2)
# # s = "abcde"
# # # res = [""]
# # # new_elm = ""

# # # for str in s:
# # #     new_elm += str
# # #     res.append(new_elm)

# # # print(res)
# # # string = [char for char in s]

# # # string2=''
# # # string2= "".join(string[0])

# # def generate_all_subsets(s):
# #     res = []
# #     string = [char for char in s]
# #     def helper(data, index, slate):
# #         #base case
# #         if index < 0:
# #             res.append("")
# #             return
# #         #recurssion
# #         slate = helper(data, index-1, slate)
# #         slate += ''.join(data[index])
# #         res.append(slate)
# #         return slate
# #     helper(string,len(s)-1,"")
# #     return res

# # if __name__ == "__main__":
# #     print(generate_all_subsets(s))

def generate_all_subsets(s):
    res = []
    
    def helper(data, index, slate):
        #base case 
        if index == len(data):
            # if slate == slate[::-1]:
            res.append("|".join(slate))
            return
        
        #rcursion 
        for i in range(index+1,len(data)+1):
            curr = string[index,i]
            
        slate.append(data[index])
        helper(data, index+1, slate)
        
        slate.pop()

        return
    helper(s,len(s)-1,[])
    return res

if __name__ == "__main__":
    s = "abracadabra"
    print(generate_all_subsets(s))


