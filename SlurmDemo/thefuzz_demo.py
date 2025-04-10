#!/usr/bin/env python

from thefuzz import fuzz
from state_capitals import capitals

# Seach capitals list for a given string:


def Score(search_text,values):
    max_score=0
    for item in values:
        item_score = fuzz.ratio( search_text, item )
        max_score = max( max_score, item_score )
    return ( max_score, values )

search_text='virginia'

print(f"Top three matches to '{search_text}':")
scored_names = list( map( lambda x: Score( search_text, x), capitals ) )
scored_names.sort()
scored_names.reverse()

print( scored_names[0:3] )
