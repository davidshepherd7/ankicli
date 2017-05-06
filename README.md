# Anki-cli

A command line interface for managing Anki decks.

This is a proof-of-concept version which is currently only capable of adding new
cards to your decks from a simple text file format.

## Installation

Requires python3 and pip already installed (e.g. `sudo apt install python3 python3-pip`)

1. Install [anki-connect](https://github.com/FooSoft/anki-connect) (anki addon 2055492159) and restart Anki
2. Run `pip3 install -r` in this directory


## Usage

Example:

    ./bin/anki-cli --card_file docs/example-card.txt

run with `-h` for more details


## File format

The `@` character at the beginning of a line is used to mark the name of a
field. Everything else on the line is used as the field name (with leading and
trailing whitespace removed), everything from the next line until the start of
the next field is used as the contents of the field.

For example a standard "Basic" card type would be written as:

```
@Front
What is a foo?
@Back
A particularly vicious variety of dandelion.

```

No other parsing or modification is done, so html, cloze deletions, LaTeX, etc.
should all work as normal.
