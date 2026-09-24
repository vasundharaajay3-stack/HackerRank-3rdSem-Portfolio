n = int(input())

strings = []

for _ in range(n):
    strings.append(input().strip())

q = int(input())

queries = []

for _ in range(q):
    queries.append(input().strip())

for query in queries:
    count = 0

    for string in strings:
        if string == query:
            count += 1

    print(count)
