from utils import permutations

lexiographic_permutations = sorted(permutations(list(range(10))))

print(lexiographic_permutations[1000000-1])
