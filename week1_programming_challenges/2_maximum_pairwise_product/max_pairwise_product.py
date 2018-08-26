# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product

def max_pair_faster(numbers):
    return(numbers[-1]*numbers[-2]) 

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    input_numbers.sort()
    print(max_pair_faster(input_numbers)) #modifies the list
