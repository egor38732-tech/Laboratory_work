def load_data():
    return [3,17,8,25,6,12,25,9,14]
def filter_above(values, threshold=10):
    sp =[]
    for i in values:
        if i>threshold:
            sp.append(i)
        else: continue
    return sp
def mean(values):

    return sum(values) / len(values)
if __name__ == '__main__':
    # Выполнится только при прямом запуске файла: python my_stats.py
    print('Самопроверка:', mean([1, 2, 3]))
