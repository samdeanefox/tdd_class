''' Metaphor:  Real physical dictionary of the English language

O.E.D. --> Huge Dictionary

Key        -> Value
Word       -> Definition
Nonplussed -> Stunned into submission, not knowing how to react

Dicts have directionality.  They are arranged for fast lookup from key to value.
You COULD go in reverse but it would entail a slow O(n) linear search.

Gobsmacked -> Stunned into submission, not knowing how to react
Dicts have unique keys but many have duplicated values.
This is another reason not to go in reverse, you could have multiple matches.

Nonplussed -> Thrown for a loop
You can change the value for a given key at any time without reordering the dict.

Dizzified  -> Stunned into submission, not knowing how to react
If keys could be mutated, they would become unfindable
If you could mutate both the key and the value, all concept of identity is lost.

To make this change:
1) Cross-out BOTH the key and value, and remember the value.           v = d.pop('Nonplussed')
2) Insert the new key in the place and add the value you remember      d['Dizzified'] = v

Dicts require immutable keys for findability and identity.
    Mutable:     list     set     dict
    Immutable:   str      bytes   int     float    complex   decimal   Fraction  bool   None   tuple   frozenset

Compound keys:
    d['raymond', 'hettinger'] = 'red'

Covfefe  --> goes in the "C" section for findability
    dicts are unordered collections.  the are about quick lookups and don't remember insertion order (all Pythons before 3.6)
    But in Python 3.6, dicts do remember insertion order as well (this is not guaranteed but it will probably never go away.
    

'''




