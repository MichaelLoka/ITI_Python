import random
import webbrowser

# List of websites to choose from
websites = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.reddit.com"
]

# Choose a random website
chosen_site = random.choice(websites)

# Open it in the default web browser
webbrowser.open(chosen_site)
