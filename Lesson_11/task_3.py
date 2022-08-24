def prime_numbers(n_1, n_2):
    lst_prime_numbers = []
    for j in range(n_1, n_2):
        prime_number = True
        for i in range(2, j):
            if j % i == 0:
                prime_number = False
        if prime_number:
            lst_prime_numbers.append(j)

    print(lst_prime_numbers)
    print('*'*220)


prime_numbers(1, 1000)

prime_numbers(30, 50)
