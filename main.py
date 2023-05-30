import schedule
import time
from scraper import scrape_and_post

def schedule_scraping_and_posting():
    # Schedule the task to run every Tuesday at 5 PM
    schedule.every().tuesday.at("17:29").do(scrape_and_post)

    # keep script running to execute scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)

# start the scheduling and execution
if __name__ == '__main__':
    schedule_scraping_and_posting()
