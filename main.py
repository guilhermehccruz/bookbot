import sys
from xml.dom.minidom import CharacterData
from stats import get_characters_count, get_num_words, sort_characters_count


def main():
	if len(sys.argv) != 2:
		print('Usage: python3 main.py <path_to_book>')
		sys.exit(1)

	file_path = sys.argv[1]

	print('============ BOOKBOT ============')

	file_content = get_book_text(file_path)

	print(f'Analyzing book found at {file_path}...')

	print('----------- Word Count ----------')

	words_count = get_num_words(file_content)

	print(f'Found {words_count} total words')

	print(f'{words_count} words found in the document')

	print('--------- Character Count -------')

	chars_count: dict[str, int] = get_characters_count(file_content)

	sorted = sort_characters_count(chars_count)

	for char in sorted:
		print(f'{char['text']}: {char['count']}')

	print('============= END ===============')


def get_book_text(file_path: str) -> str:
	file_contents: str

	with open(file_path) as f:
		file_contents = f.read()

	return file_contents


main()