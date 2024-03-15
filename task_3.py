import requests
import time

# завантаження файлу з Google Drive
def download_file_from_google_drive(file_id):
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    response = requests.get(url)
    return response.text

# ID файлів
file_id_article_1 = '18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh'
file_id_article_2 = '13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ'

# Завантаження та зчитування вмісту файлів
content_article_1 = download_file_from_google_drive(file_id_article_1)
content_article_2 = download_file_from_google_drive(file_id_article_2)

# функція пошуку Кнута-Морріса-Пратта

def kmp_search(pattern, text):
    def compute_prefix(pattern):
        prefix = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[j] != pattern[i]:
                j = prefix[j-1]
            if pattern[j] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix

    prefix = compute_prefix(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and pattern[j] != text[i]:
            j = prefix[j-1]
        if pattern[j] == text[i]:
            j += 1
        if j == len(pattern):
            return i - j + 1
    return -1

# функція пошуку Боєра-Мура

def boyer_moore_search(pattern, text):
    def compute_last_occurrence(pattern):
        last = {char: -1 for char in set(text)}
        for i in range(len(pattern)):
            last[pattern[i]] = i
        return last

    last_occurrence = compute_last_occurrence(pattern)
    m = len(pattern)
    n = len(text)
    i = m - 1
    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            return i - m + 1
        i += m - min(k, 1 + last_occurrence.get(text[i], -1))
    return -1

# функція пошуку Рабіна-Карпа

def rabin_karp_search(pattern, text, d=256, q=101):
    M = len(pattern)
    N = len(text)
    i = j = 0
    p = t = 0
    h = 1
    for i in range(M-1):
        h = (h*d)%q
    for i in range(M):
        p = (d*p + ord(pattern[i]))%q
        t = (d*t + ord(text[i]))%q
    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break
            j+=1
            if j == M:
                return i
        if i < N-M:
            t = (d*(t-ord(text[i])*h) + ord(text[i+M]))%q
            if t < 0:
                t = t+q
    return -1

# підрядок для пошуку
substring = "Двійковий або логарифмічний пошук часто використовується через швидкий час пошуку. Цей вид пошуку вимагає попереднього сортування набору даних."

# Вимірювання часу виконання для кожного алгоритму
times = {}
for algo_name, search_func in [("KMP", kmp_search), ("Boyer-Moore", boyer_moore_search), ("Rabin-Karp", rabin_karp_search)]:
    start_time = time.time()
    search_func(substring, content_article_1)
    search_func(substring, content_article_2)
    times[algo_name] = time.time() - start_time

print(times)