## Help on package memory_verse_reader


### CLASSES
- Mode
- Reader
- Verse


### class Mode
Enum for the different write modes: APPEND, OVERWRITE
    
    APPEND = 'append'
    OVERWRITE = 'overwrite'


### class Reader
Reader class to get verses from the Bible API and export them to an mp3 file
    
    __init__(self)
    
    export(self, filename: stros.PathLike, with_transcription=True)
        Exports the verses to an mp3 file
        
        Args:
            filename (stros.PathLike)
            with_transcription (bool, optional): whether to include the transcription in a text file. Defaults to True.
    
    get_verses(self, references: list[str], translation='kjv', mode='append')
        Gets verses from the Bible API and stores them in self.verses
        
        Args:
            references (list[str]): a list of Bible references e.g. ['John 3:16', 'Genesis 1:1']
            translation (str, optional): the translation of the Bible. Defaults to 'kjv'.
            mode (str, optional): the write mode. Defaults to Mode.APPEND.
        
        Yields:
            Verse: a verse object
    
    read_aloud(self)
        Reads the verses aloud


### class Verse
Verse class to store the reference, text and translation of a verse
    
    __init__(self, reference: str, text: str, translation: str)
    
    __str__(self)
        Return str(self).
    
    to_audio_text(self) -> str
        Returns the text of the verse in a format suitable for audio

FILE: `memory_verse_reader\__init__.py`


