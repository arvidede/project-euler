names = sorted([name.replace('"', '')
                for name in open('./inputs/22.txt', 'r').read().split(',')])

scores = [sum([ord(char) - (ord('a') - 1)
               for char in name.lower()]) for name in names]

print(sum([score * (i + 1) for i, score in enumerate(scores)]))
