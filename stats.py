def get_num_words(text: str)-> int:
	return len(text.split())


def get_characters_count(text: str) -> dict[str, int]:
	chars = {}

	for i in text.lower():
		if i in chars:
			chars[i] += 1
		else:
			chars[i] = 1

	return chars


def sort_on(items):
    return items["count"]


def sort_characters_count(chars: dict[str, int]) -> list[dict[str,int]]:
	chars_list = []

	for key, value in chars.items():
		if key.isalpha():
			chars_list.append({'text': key, 'count': value})

	chars_list.sort(reverse=True, key=sort_on)

	return chars_list