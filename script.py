import pandas as pd
pd.set_option('display.max_colwidth', -1)

jeps = pd.read_csv('jeopardy.csv')

jeps.rename(columns={
    'Show Number' : 'show_number',
    ' Air Date' : 'air_date',
    ' Round' : 'round',
    ' Category' : 'category',
    ' Value' : 'value',
    ' Question' : 'question',
    ' Answer' : 'answer'}, inplace=True)

print(jeps['show_number'])
print(jeps[['air_date', 'round']])
print(jeps[['category', 'value']])
print(jeps[['question', 'answer']])

def word_filter(data, words):
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  return data.loc[data['question'].apply(filter)]

 
filtered = word_filter(jeps, ["King", "England"])
print(filtered["question"])

jeps['value_nonstring'] = jeps.value.apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)

filtered = word_filter(jeps, ["King"])
print(filtered["value_nonstring"].mean())

unique_ans = jeps.answer.nunique()
print(unique_ans)

filtered = word_filter(jeps, ["King"])
print(filtered["answer"].nunique())