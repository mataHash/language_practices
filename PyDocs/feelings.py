import nltk
nltk.download('punkt_tab')
texto_ejemplo = "Python es increíblemente util en el procesamiento de lenguaje natural"

palabras = nltk.word_tokenize(texto_ejemplo)

sentimientos = nltk.sent_tokenize(texto_ejemplo, language="spanish")

print(palabras)
print(sentimientos)
