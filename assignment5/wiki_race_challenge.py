import os
import time
from collections import deque

from requesting_urls import get_html
from filter_urls import find_urls
from filter_urls import find_articles


def shortest_path(start, end):
    """ Function to find shortest path between two url's using BFS (Breadth First Search).

    :param start (str): The url to start from
    :param end (str):   The target url

    :return: Path of urls.
    """

    path = {}
    path[start] = [start]
    Q = deque([start]) # Double ended queue of pages to visit.

    while len(Q) != 0:

        page = Q.popleft() # Check next page to visit

        print(page)

        html_content = get_html(page)       # Get html content
        links = find_urls(html_content[1], base_url=html_content[0])  # First get all the links in page, html_content[0] is the base url
        articles = find_articles(links, language='en')     # Then get all articles

        # print(articles)

        for article in articles: # Go through every article link on page

            if article == end: # Check if article is destination
                return path[page] + [article] # Done!

            if (article not in path) and (article != page): # Checks if article not already are in path, or in current page
                path[article] = path[page] + [article]
                Q.append(article)

    return None  # Return none if all links (articles) are checked

def result(start, end, path):
    """ Function that returns a list as the result.

    :param start (str): The url to start from
    :param end (str):   The target url
    :param path (str):  List of urls in path

    :return: Result containing start url, end url, and the result, which can be a path or None.
    """

    if path:
        result = path
    else:
        result = None

    result = [start, end, result]

    return result

if __name__ == '__main__':
    start_time = time.time()

    start = 'https://en.wikipedia.org/wiki/Nobel_Prize'
    # end = 'https://en.wikipedia.org/wiki/Array_data_structure'
    end = 'https://en.wikipedia.org/wiki/Natural_science'

    path = shortest_path(start, end)
    result = result(start, end, path)

    end_time = time.time()
    totaltime = end_time - start_time

    # Write to file
    if not os.path.exists('wiki_race_challenge'):
        os.makedirs('wiki_race_challenge')

    file = open("wiki_race_challenge/shortest_path.txt", 'w', encoding='utf-8')
    file.write('Wiki Race Challenge finished in:\n\t{} seconds\n'.format(totaltime))
    file.write('Start Url:\n\t{}\n'.format(result[0]))
    file.write('Target Url:\n\t{}\n'.format(result[1]))
    file.write('Number of steps in Shortest path:\n\t{}\n'.format(len(result[2])))
    file.write('Links (articles) visited:\n')
    if result[2] is not None:
        for article in result[2]:
            file.write('\t{}\n'.format(article))
    else:
        file.write("Did not find a path.")

    file.close()