#!/usr/bin/python


# https://www.hackerrank.com/challenges/crossword-puzzle/problem
import os
import sys
import random


def crossword_puzzle(crossword: list, words: list) -> str:
    cache = {'vertical': [], 'horizontal': []}

    for y in range(10):
        for x in range(10):
            for direction in cache.keys():
                entity = list(slots_by_axis(crossword, y, x, axis_y=direction is 'vertical'))
                if len(entity) > 1 and not \
                        any(set(entity).issubset(v) for v in cache[direction]):
                    cache[direction] += (entity,)

    placeholders = []
    for coordinates in cache.values():
        for coord in coordinates:
            placeholders.append(Placeholder(coord))

    return '\n'.join([''.join(x) for x in Crossword(words, placeholders).fill(crossword)])


class Crossword:
    def __init__(self, words: list, placeholders: list) -> None:
        self.__words = words
        self.__placeholders = placeholders

    def fill(self, matrix: list) -> list:
        matches = self.__populate()
        for (match, word) in matches.items():
            for (i, coord) in enumerate(match.coordinates):
                matrix[coord[0]][coord[1]] = word[i]
        return matrix

    def __populate(self):
        placeholders = list(self.__placeholders)
        words = list(self.__words)
        random.shuffle(words)

        matches = {}
        for placeholder in placeholders:
            for w in words:
                if len(placeholder) == len(w):
                    matches[placeholder] = w
                    words.remove(w)
                    break
        for (position, src, target) in self.__intersection():
            if src in matches and target in matches:
                if matches[src][position[0]] != matches[target][position[1]]:
                    return self.__populate()

        return matches

    def __intersection(self):
        results = tuple()

        pool = list(self.__placeholders)
        for i in range(len(pool)):
            item = pool.pop()
            for entry in pool:
                intersects_slot = item.intersects(entry)
                if intersects_slot:
                    results += ((intersects_slot, item, entry),)

        return results


class Placeholder:
    def __init__(self, coordinates: list) -> None:
        self.__coordinates = coordinates

    def __len__(self):
        return len(self.__coordinates)

    @property
    def coordinates(self):
        return self.__coordinates

    def intersects(self, placeholder: object):
        coord = next(filter(lambda coord: coord in self.coordinates, placeholder.coordinates), None)
        return None if not coord \
            else (self.coordinates.index(coord), placeholder.coordinates.index(coord))


def slots_by_axis(crossword: list, min_range: int, pos: int, axis_y: bool) -> tuple:
    for i in range(min_range, 10):
        sign = crossword[i][pos] if axis_y else crossword[pos][i]
        if sign is not '-':
            break
        yield (i, pos) if axis_y else (pos, i)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    data = sys.argv[1].split(" ")
    for idx in range(10):
        crossword.append(list(data[idx]))

    words = data[10].split(';')

    result = crossword_puzzle(crossword, words)

    fptr.write(result)
    fptr.write('\n')

    fptr.close()
