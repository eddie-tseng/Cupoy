import numpy as np

english_score = np.array([55, 89, 76, 65, 48, 70])
math_score = np.array([60, 85, 60, 68, 55, 60])
chinese_score = np.array([65, 90, 82, 72, 66, 77])
# 1.有多少學生英文成績比數學成績高?
# ANS: 3
print(np.sum(np.greater(english_score, math_score)))

# 2.是否全班同學最高分都是國文?
# ANS: yes
print(np.logical_and(np.greater(chinese_score, math_score), np.greater(chinese_score, english_score)).any())
