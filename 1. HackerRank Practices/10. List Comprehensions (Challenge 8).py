
if __name__ == '__main__':
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    n = int(input("Enter N: "))


def generate_coordinates(x, y, z, n):
    # Use List Comprehension to generate all possible coordinates (i, j, k)
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

    # Use Another List Comprehension to Filter out coordinates with sum equal to n
    filtered_coordinates = [coords for coords in coordinates if sum(coords) != n]

    return filtered_coordinates

# Print the Result
result = generate_coordinates(x, y, z, n)
print("All Permutations of [i, j, k] are: ")
print(result)
