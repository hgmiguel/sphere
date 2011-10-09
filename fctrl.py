n = int(raw_input())

while n>0:
    num_zeros=0
    magic_five=5
    num=int(raw_input())
    while num >= magic_five:
        num_zeros += num/magic_five
        magic_five *= 5

    print num_zeros
    n-=1
