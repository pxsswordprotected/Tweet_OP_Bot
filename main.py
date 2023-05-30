import schedule
import time
import threading
from scraper import scrape_and_post
from comment_handler import handle_random_fact_comments

def schedule_scraping_and_posting():
    # Schedule the task to run every Tuesday at 5 PM
    schedule.every().tuesday.at("18:41").do(scrape_and_post)

    # Keep the script running to execute scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)

def process_comments():
    handle_random_fact_comments()

# Start the scheduling and comment processing in separate threads
if __name__ == '__main__':
    # Create a thread for scheduling and posting
    scraping_thread = threading.Thread(target=schedule_scraping_and_posting)
    scraping_thread.start()

    # Create a thread for comment processing
    comments_thread = threading.Thread(target=process_comments)
    comments_thread.start()

    # Wait for both threads to finish
    scraping_thread.join()
    comments_thread.join()
