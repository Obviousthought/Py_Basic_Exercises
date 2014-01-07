# More Function Practice

# splits a string of words at the space
def break_words(stuff):
	words = stuff.split(' ')
	return words

# sorts a string alphabetically
def sort_words(words):
	return sorted(words)

def print_first_word(words):
	word = words.pop(0)
	print word

def print_last_word(words):
	word = words.pop(-1)
	print word

# splits a string then sorts it alphabetically
def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

