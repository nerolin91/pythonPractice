def sum_of_even(st):
    sum=0.0
    for i in st:
        if i.isdigit():
            if int(i)%2==0:
                sum+=int(i)
    return sum
val = "rtuy3qw84"
print(sum_of_even(val))
