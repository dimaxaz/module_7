import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = {}
        self._read_files()

    def _read_files(self):
        punctuation = string.punctuation.replace("'", "") + " -"
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    for char in punctuation:
                        content = content.replace(char, ' ')
                    words = content.split()
                    self.all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")

    def get_all_words(self):
        return self.all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.all_words.items():
            if word in words:
                result[file_name] = [i + 1 for i, w in enumerate(words) if w == word]
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.all_words.items():
            result[file_name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')

with open('test_file.txt', 'w', encoding='utf-8') as file:
    file.write("It's a text for task. Найти везде, используйте его для самопроверки. Успехов в решении задачи! Text, text, text.")

print("Все слова:", finder2.get_all_words())

print("Позиции слова 'text':", finder2.find('text'))

print("Количество слова 'text':", finder2.count('text'))
