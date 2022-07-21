class Solution:
    def dailyTemperatures(self, temperatures):
        stack_store = []
        output_result = [0] * len(temperatures)
        for index,item in enumerate (temperatures):
            while stack_store and item > stack_store[-1][0]:
                item_value, item_index = stack_store.pop()
                output_result[item_index] = index - item_index
            stack_store.append([item, index])
        return output_result



# class Solution:
#     def dailyTemperatures(self, temperatures):
#         res = [0] * len(temperatures)
#         stack = [] # pair: [temp, index]
#         for i, t in enumerate (temperatures) :
#             while stack and t > stack[-1][0]:
#                 stackT, stackInd = stack. pop()
#                 res[stackInd] = (i - stackInd)
#             stack. append ([t, i])
#         return res

x = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]


print(x.dailyTemperatures(temperatures))
