from scraper import WhispersScraper
from transfer_to_file_utils import TransferToFileUtils
from incorrect_idx_order_exception import IncorrectIdxOrderException
import datetime
import argparse

def main():
    try:
        parser = argparse.ArgumentParser(description = \
            'Scrape NUSWhispers by post index.')
        parser.add_argument("start_idx", type=int,
                help="the starting index to be scraped")
        parser.add_argument("end_idx", type=int, 
                help= "the ending index to be scraped which is larger than or equals to start_idx")
        
        args = parser.parse_args()
        start_idx = args.start_idx
        end_idx = args.end_idx
        
        if start_idx > end_idx:
            raise IncorrectIdxOrderException(start_idx, end_idx)

    except IncorrectIdxOrderException as e:
        print(e.message)
    
    else:
        old_time = datetime.datetime.now()
        s = WhispersScraper()
        s.scrape_posts(start_idx, end_idx)
        d = TransferToFileUtils()
        file_name = 'posts' + str(start_idx) + 'to' + str(end_idx)
        d.write_to_empty_xlsx_file(s.post_content, file_name)
        time_elapsed = (datetime.datetime.now() - old_time).seconds
        hours, remainder = divmod(time_elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)
        print('\nTime taken: {:02} hours {:02} minutes {:02} seconds.'\
            .format(int(hours), int(minutes), int(seconds)))

if __name__ == "__main__":
    main()
