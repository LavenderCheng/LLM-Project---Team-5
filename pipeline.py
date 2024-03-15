from transformers import pipeline

classifer = pipeline("sentiment-analysis")
res = classifer("Today is a nice day")

print(res)