# NUSWhispers_scraper ( :construction: Work in Progress :construction: )

A simple tool to scrape [NUSWhispers's website](https://www.nuswhispers.com/) and save the contents into a file.

This scrapper scraps the NUSWhispers's website by iteratively scrapping the posts by their post index. Therefore, we will need to specify a `start_idx` that denotes the the index of the first post that will be scrapped and `end_idx` that denotes the index of the last post that will be scrapped.

## Installation

    pip install -r requirements.txt

## Usage 

First make sure that you are in the root folder. Then, 

    python src/main.py <start_idx> <end_idx>

Example: 
To scrape the post with indices from 10 to 15 (inclusive).

    python src/main.py 10 15

## Output

After running the commands shown in the "Usage" section, you should be able to see a Mircrosoft Excel file in /src folder. Each post will have 7 columns of data consisting of:
- Index of the post
- Categoies given by NUSWhispers
- Textual content of the post
- Number of likes
- Number of comments
- Age of the post
- Number of favourites

*Note:
1. The column names were not included in the Excel file.
2. Sample outputs can be found in the /output folder.*

## Testing

First make sure that you are in the root folder. Then,

    cd test
    python -m unittest

