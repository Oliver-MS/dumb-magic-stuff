import argparse

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
    

def main():
    parser = argparse.ArgumentParser(description="Calculator for Copying Precursor Golems")
    parser.add_argument("precursors", type=int)
    parser.add_argument("golems", type=int, help="Do not include the original target of the copy spell in this count.")
    parser.add_argument("copies", type=int)
    parser.add_argument("triggers", type=int)

    args = parser.parse_args()
    precursors, golems = copy_precursor_golem(args.precursors, args.golems, args.copies, args.triggers)
    print(f"You will now have {precursors} Precursor Golems and {golems} golem tokens/other golems.")

if __name__ == "__main__":
    main()
