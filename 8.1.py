import numpy as np

def binary_search(number: int) -> int:
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        predict_number = (low + high) // 2
        if predict_number < number:
            low = predict_number + 1
        elif predict_number > number:
            high = predict_number - 1
        else:
            break

    return count


def score_game(binary_search) -> int:
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(binary_search(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_search)