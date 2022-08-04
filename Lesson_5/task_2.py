natural_number = int(input("Введіть число: "))

for i in range(natural_number):
    q = i ** 2
    q_str = str(q)

    k = len(str(i))

    i_str = str(i)
    len_i = int(len(i_str))

    len_q = len(str(q))
    qq = q_str[-len_i:]

    qq_str = str(qq)

    if i_str == qq_str:
        print(i_str + "*" + i_str + "=" + q_str)
