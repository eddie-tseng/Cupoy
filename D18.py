import pandas as pd

score_df = pd.DataFrame([[1, 50, 80, 70, 'boy', 1],
                         [2, 60, 45, 50, 'boy', 2],
                         [3, 98, 43, 55, 'boy', 1],
                         [4, 70, 69, 89, 'boy', 2],
                         [5, 56, 79, 60, 'girl', 1],
                         [6, 60, 68, 55, 'girl', 2],
                         [7, 45, 70, 77, 'girl', 1],
                         [8, 55, 77, 76, 'girl', 2],
                         [9, 25, 57, 60, 'girl', 1],
                         [10, 88, 40, 43, 'girl', 3],
                         [11, 25, 60, 45, 'boy', 3],
                         [12, 80, 60, 23, 'boy', 3],
                         [13, 20, 90, 66, 'girl', 3],
                         [14, 50, 50, 50, 'girl', 3],
                         [15, 89, 67, 77, 'girl', 3]],
                        columns=['student_id', 'math_score', 'english_score', 'chinese_score', 'sex', 'class'])

# 1.找出全年級各科成績最高分與最低分?
print('max_math_score :', score_df.max(axis=0)['math_score'])
print('max_english_score :', score_df.max(axis=0)['english_score'])
print('max_chinese_score :', score_df.max(axis=0)['chinese_score'])
print('min_math_score :', score_df.min(axis=0)['math_score'])
print('min_english_score :', score_df.min(axis=0)['english_score'])
print('min_chinese_score :', score_df.min(axis=0)['chinese_score'])
# 2.找出數學班平均最高的班級?
print(score_df.groupby('class').mean())
# 3.分析全校女生與男生國文平均差幾分?
boy_score_df = score_df.loc[score_df.sex == 'boy']
girl_score_df = score_df.loc[score_df.sex == 'girl']
print(girl_score_df.mean()['chinese_score'] - boy_score_df.mean()['chinese_score'])
