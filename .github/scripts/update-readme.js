// Importing the required modules
const fs = require("fs"); // File System module to interact with the file system
const Parser = require("rss-parser"); // RSS Parser module to parse RSS feeds

// Asynchronous function to update the README file
async function updateReadme() {
  // Creating a new Parser object
  const parser = new Parser();

  // Parsing the RSS feed from the provided URL
  const feed = await parser.parseURL("https://rss.app/feeds/ttn0j4BIdOBQLG08.xml");

  // Reading the current README file
  let readme = fs.readFileSync("./README.md", "utf8");

  // Defining the start and end markers for the feed
  const markerStart = "<!-- FEED-START -->";
  const markerEnd = "<!-- FEED-END -->";

  // Finding the start and end indices of the feed in the README
  const startIndex = readme.indexOf(markerStart) + markerStart.length;
  const endIndex = readme.indexOf(markerEnd);

  // Getting the first 5 items from the feed and formatting them
  const feedItems = feed.items
    .slice(0, 10)
    .map((item) => `- ${item.title}`)
    .join("\n");

  // Updating the README with the new feed items
  readme = readme.substring(0, startIndex) + "\n" + feedItems + "\n" + readme.substring(endIndex);

  // Writing the updated README back to the file
  fs.writeFileSync("./README.md", readme);
}

// Calling the function to update the README
updateReadme();
