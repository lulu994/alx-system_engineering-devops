# 0x16. API advanced

This project involves writing a Python script to query the Reddit API and retrieve information about subreddits. The script includes functions to fetch the number of subscribers for a given subreddit and handle various scenarios such as invalid subreddit names.

## Project Structure

- `0-subs.py`: Python script containing the function to retrieve the number of subscribers for a given subreddit.
- `1-top_ten.py`: Write a function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
- `2-recurse.py`: Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
- `100-count.py`: Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords. The results should be printed in descending order by count, and if counts are the same, alphabetically.

## Requirements

- The scripts are written in Python 3 and should be compatible with Ubuntu 20.04 LTS.
- The `Requests` module is used for sending HTTP requests to the Reddit API.
- PEP 8 style guidelines are followed for code formatting.
- All scripts are executable and organized in a modular fashion.
- The project adheres to best practices for code documentation and organization.
- The project includes a comprehensive README file to explain the project structure and usage.

## Tasks

* **0. How many subs?**
  * [0-subs.py](./0-subs.py): Python function that returns the total number of
  subscribers for a given subreddit.
  * Returns `0` if an invalid subreddit is given.

* **1. Top Ten**
  * [1-top_ten.py](./1-top_ten.py): Python function that prints the top ten
  hottest posts for a given subreddit.
  * Prints `None` if an invalid subreddit is given.

* **2. Recurse it!**
  * [2-recurse.py](./2-recurse.py): Python function that recursively returns a
  list of titles for all hot articles on a given subreddit.
  * Returns `None` if no results are found on the given subreddit.

* **3. Count it!**
  * [100-count.py](./100-count.py): Python function that recursively prints a
  sorted count of given keywords parsed from titles of all hot articles on a given
  subreddit.
  * Keywords are case-insensitive and delimited by spaces.
  * Results are printed in descending order by count.
  * Words with identical counts are sorted alphabetically.
  * Words with no matches are skipped.
  * Results are based on the number of times a keyword appears - ie.,
  `java java java` counts as three separate instances of `java`.
