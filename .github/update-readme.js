const fs = require("fs");
const Parser = require("rss-parser"); // You'll need to install this package

async function updateReadme() {
  const parser = new Parser();
  const feed = await parser.parseURL("https://rss.app/feeds/ttn0j4BIdOBQLG08.xml");

  let readme = fs.readFileSync("./README.md", "utf8");

  const markerStart = "<!-- FEED-START -->";
  const markerEnd = "<!-- FEED-END -->";
  const startIndex = readme.indexOf(markerStart) + markerStart.length;
  const endIndex = readme.indexOf(markerEnd);

  const feedItems = feed.items
    .slice(0, 5)
    .map((item) => `- ${item.title}`)
    .join("\n");
  readme = readme.substring(0, startIndex) + "\n" + feedItems + "\n" + readme.substring(endIndex);

  fs.writeFileSync("./README.md", readme);
}

updateReadme();
