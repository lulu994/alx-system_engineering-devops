import requests
from collections import Counter

def count_words(subreddit, word_list, after=None, results=None):
    if results is None:
        results = Counter()

    # URL for the Reddit API to get hot articles for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    # Make the GET request
    response = requests.get(url, headers=headers, params={'after': after})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        after = data['data']['after']

        # Extract and tokenize the titles
        titles = [post['data']['title'].lower().split() for post in data['data']['children']]

        # Count word occurrences
        for title in titles:
            for word in title:
                # Remove punctuation
                word = word.strip('.,!?():;')
                if word in word_list:
                    results[word] += 1

        # If there are more pages, recursively call the function
        if after is not None:
            return count_words(subreddit, word_list, after, results)
        else:
            # Sort the results by count (descending) and then alphabetically (ascending)
            sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_results:
                print(f'{word}: {count}')
    else:
        # Invalid subreddit or other error, print nothing
        return

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)
