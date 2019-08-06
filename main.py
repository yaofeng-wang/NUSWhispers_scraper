from src.scraper import WhispersScraper
from src.transfer_to_file_utils import TransferToFileUtils
import time
import threading

def main():
    old_time = time.time() 
    s1 = WhispersScraper()
    s2 = WhispersScraper()

    t1 = threading.Thread(target=s1.scrape_posts, args=(60000, 60002))
    t2 = threading.Thread(target=s2.scrape_posts, args=(61000, 61002))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    d1 = TransferToFileUtils()
    d1.write_to_empty_xlsx_file(s1.post_content, 'p1')
    d2 = TransferToFileUtils()
    d2.write_to_empty_xlsx_file(s2.post_content, 'p2')
    new_time = time.time()
    print(str((new_time - old_time)/60) + " minutes.")
    # 59minutes
    # 1 thread : 81 minutes

if __name__ == "__main__":
    main()
