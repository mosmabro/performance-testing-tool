import sys
import traceback
from datetime import datetime
from random import randint
from uuid import uuid4
from Crawlers import ImagesCrawler

def lambda_handler(event, context):
    imgCrawler = ImagesCrawler('https://www.colypointobserver.com.au/', 1)
    try:
        imgCrawler.crawle()
    except:
        print("Unexpected error:", sys.exc_info())
        traceback.print_exc()
        raise
    # Mocked result of a stock buying transaction
    return  {
        "Id": str(uuid4()),  # Unique ID for the transaction
        "ImageLinks": imgCrawler.imagesUrls,
        "Timestamp": datetime.now().isoformat(),  # Timestamp of the when the transaction was completed
    }
    
