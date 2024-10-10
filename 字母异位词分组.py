from typing import List
from itertools import groupby


def groupAnagrams(strs: List[str]) -> List[List[str]]:
	map_strings: dict[int, List[tuple[str, str]]] = {}
	for word in strs:
		if len(word) not in map_strings:
			map_strings[len(word)] = []
		map_strings[len(word)].append((''.join(sorted(word)), word))
	result: List[List[str]] = []
	for length, words in map_strings.items():
		group = [list(group) for key, group in groupby(sorted(words, key=lambda x: x[0]), key=lambda x: x[0])]
		for word in group:
			result.append(list(element[1] for element in word))
	return result

print(groupAnagrams(["a"]))