from memory_verse_reader import Reader
import os


dir = os.path.dirname(os.path.abspath(__file__))
file_path = dir + '/verses.txt'

with open(file_path) as file:
    references = file.readlines()

reader = Reader()
for verse in reader.get_verses(references):
    print(verse)

reader.export(dir + '/verses')
os.system(f'start {dir}/verses.mp3')