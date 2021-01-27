import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])

# 1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
mean_english_score = np.mean(english_score)
mean_math_score = np.nanmean(math_score)
mean_chinese_score = np.mean(chinese_score)

std_english_score = np.std(english_score)
std_math_score = np.nanstd(math_score)
std_chinese_score = np.std(chinese_score)

max_english_score = np.amax(english_score)
max_math_score = np.nanmax(math_score)
max_chinese_score = np.amax(chinese_score)

min_english_score = np.amin(english_score)
min_math_score = np.nanmin(math_score)
min_chinese_score = np.amin(chinese_score)

print("[英文] 平均值: {}, 最大值: {}, 最小值: {}, 標準差: {}".format(mean_english_score,  max_english_score, min_english_score, std_english_score))
print("[數學] 平均值: {}, 最大值: {}, 最小值: {}, 標準差: {}".format(mean_math_score,  max_math_score, min_math_score, std_math_score))
print("[國文] 平均值: {}, 最大值: {}, 最小值: {}, 標準差: {}".format(mean_chinese_score,  max_chinese_score, min_chinese_score, std_chinese_score))

# 2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?

math_score = np.array([60,85,60,68,55,60])

mean_math_score = np.mean(math_score)

std_math_score = np.std(math_score)

max_math_score = np.amax(math_score)

min_math_score = np.amin(math_score)

print("[數學] 平均值: {}, 最大值: {}, 最小值: {}, 標準差: {}".format(mean_math_score,  max_math_score, min_math_score, std_math_score))

# 3. 用補考後資料找出與國文成績相關係數最高的學科?
print(np.corrcoef(chinese_score, math_score))
print(np.corrcoef(chinese_score, english_score))
# ANS: 英文
