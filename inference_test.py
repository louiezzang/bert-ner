# Do this in a separate python interpreter session, since you only have to do it once
import nltk
nltk.download('punkt')

from ner import Ner

model = Ner("out_base/")

output = model.predict("Steve went to Paris")

print(output)

