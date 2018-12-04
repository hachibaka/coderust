def reverse_words(sentence):
	return ' '.join(sentence.split()[::-1])

print(reverse_words("Hara Chaitanya Buddhiraju"))


def remove_duplicates(string):
	seen = []
	for ch in string:
		if ch not in seen:
			seen.append(ch)
	
	return ''.join(seen)

def remove_whitespace(string):
	output = ""
	for ch in string:

		if ch != ' ' and ch != '\t':
			output += ch
	return output

print(remove_duplicates("aabbccddefffgfijk"))
print(remove_whitespace("    All greek  to    me.    "))



