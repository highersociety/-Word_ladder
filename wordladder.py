from collections import deque

def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque()
    queue.append((beginWord, 1))  # word and current depth/steps

    while queue:
        current_word, steps = queue.popleft()

        # Try changing each letter in the word
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word == endWord:
                    return steps + 1
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, steps + 1))

    return 0
