def get_even_numbers(numbers):
    even_nums = [ ]
    for num in numbers:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]))

