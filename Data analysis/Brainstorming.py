import random

def generate_random_word():
    words = ['apple', 'mountain', 'jazz', 'robot', 'ocean', 'butterfly']
    return random.choice(words)

num_ideas = 5
brainstorming_results = [generate_random_word() for _ in range(num_ideas)]
print("Brainstorming Results:", brainstorming_results)
