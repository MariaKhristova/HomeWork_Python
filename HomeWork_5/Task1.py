# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'ыва ываыва абв авра абвабв цукабв'
splitted_text = text.split('абв')

result = [s for s in splitted_text]

print("".join(result))
