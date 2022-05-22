for num in range(1, 101):
    string = ''

    # ここから記述
    string = str(num)
    if num % 15 == 0:
        string = 'FizzBuzz'
    elif num % 3 == 0:
        string = 'Fizz'
    elif num % 5 == 0:
        string = 'Buzz'
    # ここまで記述

    print(string)
