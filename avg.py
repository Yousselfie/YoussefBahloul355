def mean(nums):
    total = 0
    for i in nums:
        total += i
    
    return round(total / len(nums), 2)


def main():
    nums = ['a', 11.5, 'b', 23, 19.60]
    print (mean(nums))
if __name__ == "__main__":
    main()

