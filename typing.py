def load_words(filename: str) -> list:

	full_path = os.getcwd() + "/" + filename
	with open(full_path, 'r') as f:
		return [line.strip() for line in f]

	
all_words = load_words("words.txt")

typing_words = 