# Import the necessary libraries
import requests
from bs4 import BeautifulSoup

# The URL of the blog
base_url = 'https://my-digital-garden-green-seven.vercel.app'

# Send a GET request to the URL
response = requests.get(base_url)

# Parse the HTML data from the response
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table body in the HTML
table_body = soup.find('tbody', {'class': 'table-view-tbody'})

# Find all table rows in the table body
rows = table_body.find_all('tr')

# Start the blog posts content with a heading
blog_posts = ''

# Loop over each table row
for row in rows:
    # Extract the title and link from the link element in the row
    title = row.find('a').text
    link = base_url + row.find('a')['href']

    # Add the title and link to the blog posts content
    blog_posts += f'## {title}\n'

# Open the README file in read mode
with open('README.md', 'r') as f:
    # Read the README content from the file
    readme = f.read()

# Split the README content into two parts: before and after the blog posts section
before, _, after = readme.partition('<!--START_SECTION:blog-->')

# Combine the parts and the new blog posts content to get the updated README content
readme = before + '<!--START_SECTION:blog-->\n' + \
    blog_posts + '<!--END_SECTION:blog-->\n' + after

# Open the README file in write mode
with open('README.md', 'w') as f:
    # Write the updated README content to the file
    f.write(readme)
