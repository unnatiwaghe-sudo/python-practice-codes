numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

print("Total number of items:", len(numbers))
print("Last item:", numbers[-1])
print("Tuple in reverse order:", numbers[::-1])

if 5 in numbers:
    print("Yes")
else:
    print("No")

if len(numbers) > 2:
    remaining = numbers[1:-1]
    sorted_remaining = tuple(sorted(remaining))
    print("After removing first and last and sorting:", sorted_remaining)
else:
    print("Not enough elements to remove first and last")
