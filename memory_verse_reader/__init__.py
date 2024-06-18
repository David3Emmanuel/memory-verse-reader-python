import requests
import pyttsx3

# Create an enum for the different modes: APPEND, OVERWRITE
class Mode:
    APPEND = 'append'
    OVERWRITE = 'overwrite'

class Verse:
    def __init__(self, reference, text, translation):
        self.reference = reference
        self.text = text
        self.translation = translation

    def __str__(self):
        return f'{self.reference} {self.translation} - {self.text}'
    
    def to_audio_text(self):
        book, chapter_verse = self.reference.split(' ')
        chapter, verse = chapter_verse.split(':')
        return f'{book} chapter {chapter} verse {verse}\n{self.text}'

class Reader:
    def __init__(self):
        self.verses = []
        self.audio = None
        self.transcription = []

    def get_verses(self, references=[], translation='kjv', mode=Mode.APPEND):
        if mode == Mode.OVERWRITE:
            self.verses = []
        
        for ref in references:
            response = requests.get(f'https://bible-api.com/{ref}?translation={translation}').json()
            verse = Verse(response['reference'], response['text'].strip(), response['translation_id'].upper())
            self.verses.append(verse)
            yield verse

    def _export(self):
        if self.audio:
            return

        self.transcription = []
        for verse in self.verses:
            self.transcription.append(verse.to_audio_text())

        self.audio = pyttsx3.init()

    def read_aloud(self):
        self._export()
        for verse in self.transcription:
            self.audio.say(verse)
        self.audio.runAndWait()

    def export(self, filename, with_transcription=True):
        self._export()
        for verse in self.transcription:
            self.audio.save_to_file(verse, f'{filename}.mp3')
        self.audio.runAndWait()

        if with_transcription:
            with open(f'{filename}.transcription.txt', 'w') as file:
                for verse in self.transcription:
                    file.write(verse)