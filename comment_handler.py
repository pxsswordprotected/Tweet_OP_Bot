import praw
import random

def handle_random_fact_comments():
    reddit = praw.Reddit(
        client_id='PNe3JFwv98HkByNteLMG3Q',
        client_secret='rbcFOP4a9tlZh9t0IvbM9KhnmUgNGw',
        user_agent='OnePiece Tracker',
        username='OnePieceHypeTracker',
        password='JamesTennis!111'
    )

    subreddit_name = 'u_OnePieceHypeTracker'
    subreddit = reddit.subreddit(subreddit_name)

    for comment in subreddit.stream.comments(skip_existing=True):
        if 'give me a random fact' in comment.body.lower():
            fact = get_random_one_piece_fact()
            reply = f"Sure! Here's a random One Piece fact: {fact}"
            comment.reply(reply)
            print("success")

def get_random_one_piece_fact():
    facts = [
        "One Piece has been serialized since 1997.",
        "Eiichiro Oda is the author and illustrator of One Piece.",
        "One Piece has over 1000 chapters.",
        "The Straw Hat Pirates are the main crew in One Piece.",
        "The Straw Hat Pirates are the main crew in One Piece",
        "Tony Tony Chopper is a reindeer who ate the Human-Human Fruit, allowing him to transform into a human",
        "Brook, the musician of the Straw Hat Pirates, is a living skeleton who ate the Revive-Revive Fruit",
        "Nami, the navigator of the Straw Hat Pirates, has a special Climatact weapon that can control weather patterns",
        "Franky, the shipwright of the Straw Hat Pirates, is a cyborg who built his own body and can shoot powerful beams from his hands",
        "Robin, also known as 'Devil Child'"
    ]
    return random.choice(facts)

