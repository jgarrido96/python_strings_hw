print('\n')

# 1. Product Review Analysis

# Task 1: Keyword Highlighter
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

for review in reviews:
    print(review.replace("good", "GOOD").replace("excellent", "EXCELLENT").replace("bad", "BAD").replace("Poor", "POOR").replace("average", "AVERAGE"))
print('\n')

# Task 2: Sentiment Tally
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
# print(f"There are {len(positive_words)} positive words")
# print(f"There are {len(negative_words)} negative words")


def tally(reviews, words):
    tally = 0
    for review in reviews:
        for item in words:
            if item.upper() in review.upper():
                tally += 1
    return tally

print('\n')

positive_word_tally = tally(reviews, positive_words)
print(f"The total number of positive words is {positive_word_tally}")
negative_word_tally = tally(reviews, negative_words)
print(f"The total number of negative words is {negative_word_tally}")
print('\n')

# Task 3: Review Summary
print("Review previews:")
for review in reviews:
    final_review = review[0:29]
    x = 29
    while True:
        if review[x] == " " or review[x] == "." or review[x] == "!":
            break
        else:
            final_review = final_review + review[x]
        x += 1
    print(f"{final_review}...")



























































































































































































































# This is for my own understanding of the above. Please ignore!

# def word_count():
#     positive_word_tally = 0
#     negative_word_tally = 0
#     for review in reviews:
#         for positive in positive_words:
#             if positive.upper() in review.upper():
#                 positive_word_tally += 1
#         for negative in negative_words:
#             if negative.upper() in review.upper():
#                 negative_word_tally += 1
#     print(positive_word_tally)
#     print(negative_word_tally)
