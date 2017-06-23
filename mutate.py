#!/usr/bin/env python
"""Scramble a text but keep parts of speech in order."""
from __future__ import print_function

from collections import defaultdict
import random
import textwrap

import six
import gutenberg
import gutenberg.cleanup
import gutenberg.acquire
import nltk



def main(textid):
    """do all the work"""
    otext = gutenberg.cleanup.strip_headers(gutenberg.acquire.load_etext(textid)).strip()

    if textid == 11231:
        otext = otext.replace("BARTLEBY, THE SCRIVENER.\n\nA STORY OF WALL-STREET.", "").strip()

    # careful, what if # occurs in the original text?
    otext = otext.replace("\n\n", "#")

    otext = otext.replace("  ", " ")
    otext = otext.replace("  ", " ")

    text = nltk.word_tokenize(otext)
    pos = nltk.pos_tag(text)
    posdict = defaultdict(lambda: [])
    for item in pos:
        posdict[item[1]].append(item[0])

    out = six.StringIO()
    for item in pos:
        part = item[0]
        if part not in ['.', ',']:
            out.write(' ')
        out.write(random.choice(posdict[item[1]]))

    output = textwrap.wrap(out.getvalue())
    formatted_output = "\n".join(output)

    formatted_output = formatted_output.replace("#", "\n\n")
    print(formatted_output)

if __name__ == '__main__':
    main(11231) # bartleby
