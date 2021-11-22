# def solution(s):
#     answer = 0
    
#     alpha = ['zero', 'one', 'two', 'three', 'four', 'five',
#          'six', 'seven', 'eight', 'nine']
#     num = [0,1,2,3,4,5,6,7,8,9]
    
#     for a in range(len(alpha)) :
#         if s.find(alpha[a]) > -1 :
#             s_replace = s.find(alpha[a])
#             s = s.replace(alpha[a], "")
#             first, last = s[0:s_replace], s[s_replace:]
#             s = first + str(num[a]) + last
    
#     answer = s
#     return answer
  
# s = "one4seveneight"
# solution(s)


import re

alpha = ['zero', 'one', 'two', 'three', 'four', 'five','six', 'seven', 'eight', 'nine']

num = [0,1,2,3,4,5,6,7,8,9]

s = "one4seveneighteight"

for i in range(len(alpha)) :
  s = re.sub(alpha[i], str(num[i]), s)

print(s)