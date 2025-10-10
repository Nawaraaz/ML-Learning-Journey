import random

subjects = [
    "Rambarani",
    "Laxman",
    "Hari",
    "Shyam",
    "Gopal",
    "Sita",
    "Radha",
    "Rama",
    "Krishna",
    "Radha",
]

actions=[
    "launches",
    "attacked",
    "cancels",
    "dances with",
    "loves",
    "hates",
    "wants",
    "declares war",
    "orders",
    "celebrates",
    "sings"
]

places_or_things=[
    "the sky",
    "the moon",
    "the stars",
    "the sun",
    "the clouds",
    "the trees",
    "the mountains",
    "the ocean",
    "the river",
    "the sand",
    "in the stadium",
    "in the garden",
    "in the forest",
    "in the city",
    "in the village",
    "in the house"
]


def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    headline = f"{subject} {action} {place_or_thing}"
    return headline

headline = generate_headline()
print(headline)

while input("Do you want another headline? (yes/no): ").lower() == "yes":
    headline = generate_headline()
    print(headline)

print("Goodbye!")