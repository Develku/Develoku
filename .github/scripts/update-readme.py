import requests
from bs4 import BeautifulSoup

base_url = 'https://my-digital-garden-green-seven.vercel.app'
response = requests.get(base_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML data from the response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table body in the HTML
    # NOTE: The actual class or HTML structure may vary, adjust the selector accordingly
    table_body = soup.find('tbody', {'class': 'table-view-tbody'})
    rows = table_body.find_all('tr')  # Find all table rows in the table body

    # Initialize the blog posts content with a heading
    blog_posts_markdown = ""

    # Loop over each table row
    for row in rows:
        # Extract the title and link from the link element in the row
        title = row.find('a').text
        link = base_url + row.find('a')['href']

        # Add the title and link to the blog posts content
        blog_posts_markdown += f"- [{title}]({link})\n"

    # Open the README file in read mode
    with open('README.md', 'r') as f:
        # Read the README content from the file
        readme = f.read()

    # Define the start and end markers
    start_marker = "<!--START_SECTION:blog-->"
    end_marker = "<!--END_SECTION:blog-->"

    # Split the README content into parts
    start_index = readme.find(start_marker) + len(start_marker)
    end_index = readme.find(end_marker)

    # Check if both markers are present
    if start_index == -1 or end_index == -1:
        print("Could not find markers in the README.md file.")
    else:
        # Replace the old list of blog articles with the new one in the README content
        updated_readme = readme[:start_index] + "\n" + \
            blog_posts_markdown + readme[end_index:]

        # Write the updated README content back to the README.md file
        with open('README.md', 'w') as f:
            f.write(updated_readme)

else:
    print(f"Failed to fetch blog posts, status code: {response.status_code}")
