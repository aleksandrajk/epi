import urllib.request
from bs4 import BeautifulSoup

# Input the URL of the web page you want to analyze
url = input("Enter the URL: ")

try:
    # Open and read the web page
    with urllib.request.urlopen(url) as response:
        html = response.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all paragraph (p) tags
    paragraphs = soup.find_all('p')

    # Count the number of paragraphs
    paragraph_count = len(paragraphs)

    # Print the count of paragraphs
    print(f"Number of paragraphs: {paragraph_count}")

except urllib.error.URLError as e:
    print(f"Error accessing the URL: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# We used 'pip install beautifulsoup4'
