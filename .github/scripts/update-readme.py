import requests
from bs4 import BeautifulSoup

# Function to fetch and update blog posts


def update_blog_posts():
    base_url = 'https://my-digital-garden-green-seven.vercel.app'
    print("Fetching blog posts from:", base_url)
    try:
        response = requests.get(base_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all 'tr' elements in the 'tbody' with class 'table-view-tbody'
            rows = soup.find('tbody', class_='table-view-tbody').find_all('tr')

            blog_posts_markdown = ""

            for row in rows:
                # The title and link are within 'a' tags inside the first 'td' of each row
                link_tag = row.find('td').find('a')
                title = link_tag.text.strip()
                link = base_url + link_tag['href']

                blog_posts_markdown += f"- [{title}]({link})\n"

            print("Blog posts fetched successfully.")
            return blog_posts_markdown
        else:
            print(
                f"Failed to fetch blog posts, status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching blog posts: {e}")
        return None

# Function to update the README file


def update_readme(blog_posts_markdown):
    if blog_posts_markdown:
        readme_path = 'README.md'
        print("Updating README with the latest blog posts.")
        try:
            # Open the README file in read mode
            with open(readme_path, 'r') as f:
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
                with open(readme_path, 'w') as f:
                    f.write(updated_readme)

                print("README updated successfully.")
        except Exception as e:
            print(f"An error occurred while updating README: {e}")
    else:
        print("No blog posts markdown to update README.")


def git_commit_and_push():
    try:
        # Stage the README.md file
        subprocess.run(["git", "add", "README.md"], check=True)
        # Commit the changes
        subprocess.run(
            ["git", "commit", "-m", "Update README with the latest blog posts"], check=True)
        # Push the changes back to the repository
        subprocess.run(["git", "push"], check=True)
        print("Pushed the changes to the repository successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while committing and pushing: {e}")


# Main execution
if __name__ == "__main__":
    blog_posts_markdown = update_blog_posts()
    update_readme(blog_posts_markdown)
    git_commit_and_push()  # Call this new function to commit and push changes
