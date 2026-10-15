N = int(input())

for _ in range(N):
    X = int(input())
    numbers = list(map(int, input().split()))

    total = sum(y ** 4 for y in numbers if y <= 0 and len(numbers) == X)

    print(total)
