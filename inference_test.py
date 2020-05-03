from ner import Ner

model = Ner("out_base/")

output = model.predict("Steve went to Paris")

print(output)

