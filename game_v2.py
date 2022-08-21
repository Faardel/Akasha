"""Guess the number game..
The computer itself makes a guess and guesses the number
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guess number

    Args:
        number (int, optional): The hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # estimated number
        if number == predict_number:
            break # exit the loop if guessed right
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """For how many attempts on average out of 1000 approaches does our algorithm guess

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    """

    count_ls = [] # list to save the number of attempts
    np.random.seed(1) #we fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # made a list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # we find the average number of attempts

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)