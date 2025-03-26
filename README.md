# Anime Directory and File Name Cleaner

A non-destructive Python script to clean anime folder and file names by removing release group tags, technical information, and other unnecessary elements while preserving essential information such as titles, episode numbers, and years.

## Features

- Removes release group tags, technical specifications, and video/audio format information
- Preserves essential information like titles, episode numbers, and years
- Shows preview of changes before applying
- Works on both individual files and entire directory structures
- Non-destructive operation with confirmation prompt

## Examples of Transformations

### Folder Names

Before:
```
[Moozzi2] Girls Band Cry [ x265-10Bit Ver. ] - TV + SP
```

After:
```
Girls Band Cry
```

### File Names

Before:
```
[Moozzi2] Girls Band Cry - 01 (BD 1920x1080 x265-10Bit FLACx2).mkv
```

After:
```
Girls Band Cry - 01.mkv
```

Before:
```
[Beatrice-Raws] Suzume no Tojimari [BDRip 3840x1608 HEVC HDR DTSHD].mkv
```

After:
```
Suzume no Tojimari.mkv
```

## Requirements

- Python 3.6 or higher
- No external dependencies

## Installation

Clone this script:

```bash
wget https://raw.githubusercontent.com/wvrlow/decancer-anime/refs/heads/main/decancer.py
```

## Usage

### Basic Usage

To clean the current directory:

```bash
python decancer.py
```

To clean a specific directory:

```bash
python decancer.py /path/to/anime
```

### Preview Mode

The script will always show a preview of changes first and ask for confirmation before applying any changes:

```
======= PREVIEW OF CHANGES =======
Number of changes: 42

DIRECTORY CHANGES:
1. FROM: [Anime Time] Death Parade + Special [BD][Dual Audio][1080p][HEVC 10bit x265][AAC][Eng Sub]
   TO:   Death Parade

FILE CHANGES:
1. FROM: Death Parade - 01.mkv
   TO:   Death Parade - 01.mkv
...

Apply these changes? (y/N) or (s) to show all:
```

### Testing

For testing purposes, you can generate a sample anime directory structure and then run the cleaner on it:

```bash
python test_generator.py && python decancer.py anime_test/
```

This will:
1. Create an anime_test directory with sample anime files and folders
2. Run the cleaner on this test directory to see how files would be renamed
