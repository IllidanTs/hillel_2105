def sum_numbers_in_strings(strings):
    results = []

    for string in strings:
        try:
            numbers = list(map(int, string.split(',')))
            total = sum(numbers)
            results.append(total)
        except ValueError:
            results.append("Не можу це зробити!")

    return results


input_strings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

output = sum_numbers_in_strings(input_strings)
for result in output:
    print(result)
