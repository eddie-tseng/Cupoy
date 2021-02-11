import pandas as pd

q_df = pd.DataFrame([['male', 'teacher'],
                     ['male', 'engineer'],
                     ['female', None],
                     ['female', 'engineer']], columns=['Sex', 'Profession'])

# 1.缺失值填入字串'others'
q_df = q_df.fillna('others')
print(q_df)

# 2.更進一步將字串做編碼。 此時用什麼方式做編碼比較適合?為什麼?

pf = pd.get_dummies(q_df[['Sex']])
q_df = pd.concat([q_df, pf], axis=1)
print(q_df)
