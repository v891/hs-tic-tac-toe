# work with the preset variable `words`

# print([x for x in words if x.startswith('a') or x.startswith('A')])

school = [["Mary", "Jack", "Tiffany"],
          ["Brad", "Claire"],
          ["Molly", "Andy", "Carla"]]

print([y for y in (x for x in school)])
print([student for class_group in school for student in class_group])

matrix = [j for j in range(5) for i in range(2)]
print(matrix)

M = [[34, 77, 8,  45],
     [10, 15, 93, 57],
     [78, 82, 19, 98]]
print(M[2][0])
