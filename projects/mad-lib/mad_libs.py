def get_word(prompt):
    """Get a word from the user."""
    return input(prompt)

def main():
    print("Welcome to Mad Libs!")
    print("Please provide the following words to create your story:\n")
    
    # Get words from user
    adjective1 = get_word("Enter an adjective: ")
    noun1 = get_word("Enter a noun: ")
    verb1 = get_word("Enter a verb (past tense): ")
    adverb = get_word("Enter an adverb: ")
    adjective2 = get_word("Enter another adjective: ")
    noun2 = get_word("Enter another noun: ")
    noun3 = get_word("Enter another noun: ")
    adjective3 = get_word("Enter another adjective: ")
    verb2 = get_word("Enter another verb: ")
    adverb2 = get_word("Enter another adverb: ")
    verb3 = get_word("Enter another verb (past tense): ")
    adjective4 = get_word("Enter another adjective: ")
    
    # Create the story
    story = f"""
    Today I went to the zoo. I saw a {adjective1} {noun1} jumping up and down in its tree.
    He {verb1} {adverb} through the large tunnel that led to its {adjective2} {noun2}.
    I got some peanuts and passed them through the cage to a gigantic gray {noun3}
    towering above my head. Feeding that animal made me hungry. I went to get a {adjective3}
    scoop of ice cream. It filled my stomach. Afterwards I had to {verb2} {adverb2} to catch our bus.
    When I got home I {verb3} my mom for a {adjective4} day at the zoo.
    """
    
    print("\nYour Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main() 