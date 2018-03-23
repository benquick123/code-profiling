
def besedilo(tvit):
    return tvit.split(":", 1)[1].strip()

def get_author(tweet):
    return tweet.split(":")[0]

def zadnji_tvit(tviti):
    authors_and_tweets = {}

    for tweet in tviti:
        author = get_author(tweet)
        authors_and_tweets[author] = besedilo(tweet)

    return authors_and_tweets

def prvi_tvit(tviti):
    authors_and_tweets = {}

    for tweet in tviti:
        author = get_author(tweet)
        if author not in authors_and_tweets:
            authors_and_tweets[author] = besedilo(tweet)

    return authors_and_tweets

def prestej_tvite(tviti):
    authors_and_number_of_tweets = {}

    for tweet in tviti:
        author = get_author(tweet)
        authors_and_number_of_tweets[author] = authors_and_number_of_tweets.get(author, 0) + 1

    return authors_and_number_of_tweets

def trim_not_alphanumerical(string):
    start = 0
    for char in string:
        if char.isalnum():
            break
        start += 1

    end = len(string)
    for char in reversed(string):
        if char.isalnum():
            break
        end -= 1

    return string[start:end]

def extract_word_starting_with(content, char):
    mentioned_people = []

    words = content.split(" ")

    for word in words:
        # Check if the first char in a word in a '@'
        if word[0] == char:
            mentioned_people.append(trim_not_alphanumerical(word))

    return mentioned_people

from collections import defaultdict

def omembe(tviti):
    authors_and_mentioned_people = defaultdict(list)

    for tweet in tviti:
        author = get_author(tweet)
        mentioned_people = extract_word_starting_with(tweet, '@')
        if author in authors_and_mentioned_people:
            authors_and_mentioned_people[author].extend(mentioned_people)
        else:
            authors_and_mentioned_people[author] = mentioned_people

    return dict(authors_and_mentioned_people)

def neomembe(ime, omembe):
    not_mentioned = []
    mentioned_persons = omembe.get(ime)

    for person in omembe.keys():
        if person == ime:
            continue

        if person not in mentioned_persons:
            not_mentioned.append(person)

    return not_mentioned

