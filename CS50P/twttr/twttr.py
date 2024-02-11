# twttr


def removeVowels(user_input, K):
	vowels = 'AEIOUaeiou'
	for word in vowels:

		user_input = user_input.replace(word, K)

	return user_input


input_str = input("Input: ")

K = ""

print("Output:", removeVowels(input_str, K))

