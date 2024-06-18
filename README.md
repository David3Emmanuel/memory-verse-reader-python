# memory-verse-reader-python
A simple python script that exports memory verses to mp3.

## Installation
1. Clone the repository: `git clone https://github.com/David3Emmanuel/memory-verse-reader-python.git`
2. Navigate to the project directory: `cd memory-verse-reader-python`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage
```python
from memory_verse_reader import Reader, Mode

# Initialize the reader
reader = Reader()

# Get the memory verse
verses = reader.get_verses(['John 3:16', 'Genesis 1:1'], translation='kjv', mode=Mode.APPEND)

# Read the verses aloud
reader.read_aloud()

# Export the verses to an mp3 file
reader.export('memory_verse.mp3', with_transcription=True)
```

Check out the [example](example/__main__.py) file for a simple example on how to use the script.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
If you have any questions or suggestions, feel free to reach out to me at david3emmanuel@gmail.com.
