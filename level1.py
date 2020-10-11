def get_index(numbers, num):
    if num in numbers:
        return(numbers.index(num))

    else:
        return(-1)

if __name__ == '__main__':
    num = 4
    numbers = [3, 6, 5, 8]
    index = get_index(numbers, num)
    print(index)
