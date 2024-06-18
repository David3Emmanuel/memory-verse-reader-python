import requests
import pyttsx3
import os


class Mode:
    '''
    Enum for the different write modes: APPEND, OVERWRITE
    '''
    APPEND = 'append'
    OVERWRITE = 'overwrite'


class Verse:
    '''
    Verse class to store the reference, text and translation of a verse
    '''
    def __init__(self, reference: str, text: str, translation: str):
        self.reference = reference
        self.text = text
        self.translation = translation

    def __str__(self):
        return f'{self.reference} {self.translation} - {self.text}'
    
    def to_audio_text(self) -> str:
        """Returns the text of the verse in a format suitable for audio

        Returns:
            str
        """        
        book, chapter_verse = self.reference.split(' ')
        chapter, verse = chapter_verse.split(':')
        return f'{book} chapter {chapter} verse {verse}\n{self.text}'


class Reader:
    """Reader class to get verses from the Bible API and export them to an mp3 file
    """    
    def __init__(self):
        self.verses: list[Verse] = []
        self.audio: None | pyttsx3.Engine = None
        self.transcription: list[str] = []

    def get_verses(self, references:list[str], translation='kjv', mode=Mode.APPEND):
        """Gets verses from the Bible API and stores them in self.verses

        Args:
            references (list[str]): a list of Bible references e.g. ['John 3:16', 'Genesis 1:1']
            translation (str, optional): the translation of the Bible. Defaults to 'kjv'.
            mode (str, optional): the write mode. Defaults to Mode.APPEND.

        Yields:
            Verse: a verse object
        """       
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
        """Reads the verses aloud
        """        
        self._export()
        for verse in self.transcription:
            self.audio.say(verse)
        self.audio.runAndWait()

    def export(self, filename: str | os.PathLike, with_transcription=True):
        """Exports the verses to an mp3 file

        Args:
            filename (str | os.PathLike)
            with_transcription (bool, optional): whether to include the transcription in a text file. Defaults to True.
        """        
        self._export()
        for verse in self.transcription:
            self.audio.save_to_file(verse, f'{filename}.mp3')
        self.audio.runAndWait()

        if with_transcription:
            with open(f'{filename}.transcription.txt', 'w') as file:
                for verse in self.transcription:
                    file.write(verse)
