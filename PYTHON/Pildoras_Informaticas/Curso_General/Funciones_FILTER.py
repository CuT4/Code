def num_par(num):

    if num % 2==0:

        return True


numeros=[17,9,8,25,43,45,76,22]

print(list(filter(num_par, numeros)))

