
# Returns the number of precursor golems and non-precursor golems 
# after casting a copy spell, including the originals.

# DO NOT INCLUDE THE ORIGINAL TARGET OF THE COPY SPELL IN THE PARAMETER COUNT
def copy_precursor_golem(precursors: int, golems: int, copies: int, precursor_triggers: int) -> tuple[int, int]:
    new_precursors = precursors * copies
    new_golems = (new_precursors * 2) + (copies * golems)
    if precursor_triggers == 0:
        # Add back in the original (assumed non-precursor) golem + copies from the original spell
        return (precursors, golems + 1 + copies)
    else:
        return copy_precursor_golem(precursors + new_precursors, golems + new_golems, copies, precursor_triggers - 1)

first_rite_precursors, first_rite_golems = copy_precursor_golem(1,1,5,1)
print(first_rite_precursors, first_rite_golems)
second_rite_precursors, second_rite_golems = copy_precursor_golem(6, 21, 5, 6)
print(second_rite_precursors, second_rite_golems)