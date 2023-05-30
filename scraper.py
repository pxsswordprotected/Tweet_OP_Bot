import praw
import re
from twilio.rest import Client

def scrape_and_post():
    reddit = praw.Reddit(
        client_id='PNe3JFwv98HkByNteLMG3Q',
        client_secret='rbcFOP4a9tlZh9t0IvbM9KhnmUgNGw',
        user_agent='OnePiece Tracker',
        username='OnePieceHypeTracker',
        password='JamesTennis!111'
    )

    subreddit_name = 'OnePiece' #one piece sub
    title_pattern = r'one piece chapter (\d{4}) spoilers'  # updated regex

    # Search for the post with the matching pattern in the subreddit
    subreddit = reddit.subreddit(subreddit_name)
    post = None
    for submission in subreddit.hot(limit=1):
        if re.search(title_pattern, submission.title, re.IGNORECASE):
            post = submission
            break

    if post is not None:
        # Get the chapter number from the post title using regex
        chapter_number = None
        match = re.search(title_pattern, post.title, re.IGNORECASE)
        if match:
            chapter_number = match.group(1)

        # getting comment count
        comment_count = post.num_comments
        print(f"The post 'One Piece chapter {chapter_number} spoilers' has {comment_count} comments.")

        hype_threshold = 3600  # threshhold

        if comment_count > hype_threshold:
            hype_level = 'Hype'
        else:
            hype_level = 'Not Hype'

        title = 'Is the One Piece chapter hype this week?'
        text = f"The upcoming chapter of One Piece is {hype_level}! 🎉\n\nChapter: {chapter_number}\n\nTotal Comments in the spoiler thread by Tuesday 5 PM: {comment_count}"

    else:
        # No post found, indicating a break week
        chapter_number = "Break Week"
        comment_count = 0
        print("No post found. It's a break week.")

        title = 'No New Chapter This Week'
        text = "There is no new chapter of One Piece this week. Enjoy the break!"

    subreddit_name = 'u_OnePieceHypeTracker'  # Reddit username

    subreddit = reddit.subreddit(subreddit_name)
    submission = subreddit.submit(title, selftext=text)

        # Twilio client
    twilio_account_sid = 'AC11650a6322d6a5aa8a88b5f28e9c32d1'
    twilio_auth_token = 'bfab406c855a7cb13a6aac842accf1bc'
    twilio_phone_number = '+18442241878'
    recipient_phone_number = '+19367775168' #my own phone number

    client = Client(twilio_account_sid, twilio_auth_token)

    # Send a text
    sms_message = f"The upcoming chapter of One Piece is {hype_level}!\nChapter: {chapter_number}\nTotal Comments: {comment_count}"
    message = client.messages.create(
        body=sms_message,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print(f"SMS sent: {message.sid}")