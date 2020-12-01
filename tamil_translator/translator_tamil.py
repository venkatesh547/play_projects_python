from translate import Translator


translator= Translator(to_lang="ta")

try:
	with open('./test.txt') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		print(translation)
except FileNotFoundError as err:
	print('Check the path you idiot!!!!')



####### Below code is to translate and write output in new file


	
from translate import Translator


translator= Translator(to_lang="ta")

try:
	with open('./test.txt') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		with open('./test-tamil.txt', mode='w') as translated_tamil_file:
			translated_tamil_file.write(translation)
except FileNotFoundError as err:
	print('Check the path you idiot!!!!')
