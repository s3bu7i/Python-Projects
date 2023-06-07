import emoji

# Define a dictionary mapping keywords to emojis
emoji_mapping = {
    'happy': ':smile:',
    'sad': ':cry:',
    'love': ':heart:',
    'laugh': ':joy:',
    'angry': ':rage:'
}

# Function to generate emoji art from text
def generate_emoji_art(text):
    words = text.lower().split()
    emoji_art = ''
    for word in words:
        if word in emoji_mapping:
            emoji_art += emoji.emojize(emoji_mapping[word]) + ' '
        else:
            emoji_art += word + ' '
    return emoji_art

# Get user input
text_input = input("Enter your text: ")

# Generate and display the emoji art
generated_art = generate_emoji_art(text_input)
print(generated_art)
