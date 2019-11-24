# Multi-Directory Backup

Multi-Directory Backup is a Python program for backing-up multiple directories

## Installation

For now, just copy and paste `ap.py` and `settings.json` to your Desktop (or wherever you want)

## Usage

In the `settings.json` file you'll want to change the settings to fit your desires best, for more detail on each setting take a look at the [Reference](#reference)

```json
{
  "input": [
    "C:/PATH/TO/DIRECTORY/"
  ],
  "output": [
    "C:/PATH/TO/DIRECTORY/"
  ],
  "closeWhenDone": true,
  "askBeforeCopying": true
}
```

# Reference

## Input Key
`input` is used to tell the program what directory to backup,

## Output Key
`output` is used to tell the program where to put the backup.

## closeWhenDone Key
`closeWhenDone` is used to close the program after it's done copying all directories.

## askBeforeCopying Key
`askBeforeCopying` is really just a safety measure, but it asks if you want to copy files over so that you don't accidentally override a directory.


## License
[MIT](https://choosealicense.com/licenses/mit/)
