# Ankicli

A command line interface for managing Anki decks.

This is a proof-of-concept version which is currently only capable of adding new
cards to your decks from a simple text file format.

## Installation

1. Install python3 and pip (for python3), e.g. with `sudo apt install python3 python3-pip`.
2. Install [anki-connect](https://github.com/FooSoft/anki-connect) (anki addon 2055492159) and restart Anki
3. Clone this repository
4. Run `pip3 install -r requirements.txt` in the project root directory


## Usage

Example: from the project root directory run

    ./bin/anki-cli --card_file docs/example-card.txt

Run with `-h` for more details on other options.

Markdown example:

    ./bin/anki-cli --markdown --card_file docs/example-card.md


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


## Licence

The current licence is AGPLv3 because that's [what Anki uses](https://github.com/dae/anki/blob/master/LICENSE) and consistent licencing is nice. If you would like something less restrictive give me a shout.
