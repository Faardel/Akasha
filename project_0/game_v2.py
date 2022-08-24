"""Guess the number game..
The computer itself makes a guess and guesses the number
"""
import numpy as np

def game_core_v2(number: int = 1) -> int:
    """Guess number

Args:
    number (int, optional): The hidden number. Defaults to 1.

Returns:
    int: Number of attempts
"""
    limit_a = 0
    count = 0
    limit_b = 101
    predict = (limit_a + limit_b)//2
    
    while number != predict:
            count += 1
            if predict > number:
                limit_b = predict - 1
                predict = (limit_a + limit_b)//2

            elif predict < number:
                limit_a = predict + 1
                predict = (limit_a + limit_b)//2
    return count

print(f'Количество попыток: {game_core_v2()}')

def score_game(game_core_v2) -> int:
    """For how many attempts on average out of 1000 approaches does our algorithm guess

    Args:
        game_core_v2 ([type]): guessing function

    Returns:
        int: average number of attempts
    """

    count_ls = [] # list to save the number of attempts
    np.random.seed(1) #we fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # made a list of numbers

    for number in random_array:
        count_ls.append(game_core_v2(number))

    score = int(np.mean(count_ls)) # we find the average number of attempts

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(game_core_v2)