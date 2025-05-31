import cloudscraper
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from datetime import datetime
import re

def fetch_news_articles(url="https://www.scouts.org.uk/news"):
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []
    for article_div in soup.select("div.col-md-6.col-lg-4"):
        link_tag = article_div.find("a", href=True)
        title_tag = article_div.find("a", class_="h5")
        summary_tag = article_div.find("p", class_="mt-2")
        date_tag = article_div.find("p", class_="small")

        if not link_tag or not title_tag:
            continue

        link = "https://www.scouts.org.uk" + link_tag["href"]
        title = title_tag.get_text(strip=True)
        summary = summary_tag.get_text(strip=True) if summary_tag else ""

        pub_date = None
        if date_tag:
            date_match = re.search(r"(\d{1,2}(st|nd|rd|th)?\s\w+\s\d{4})", date_tag.text)
            if date_match:
                try:
                    pub_date = datetime.strptime(date_match.group(1), "%d %B %Y")
                except ValueError:
                    pass

        articles.append({
            "title": title,
            "link": link,
            "summary": summary,
            "pubDate": pub_date,
        })

    return articles

def generate_rss(articles, output_file="scouts_news.xml"):
    fg = FeedGenerator()
    fg.title("Scouts UK News")
    fg.link(href="https://www.scouts.org.uk/news", rel="alternate")
    fg.description("Latest news from The Scouts UK")
    fg.language("en")

    for item in articles:
        fe = fg.add_entry()
        fe.title(item["title"])
        fe.link(href=item["link"])
        fe.description(item["summary"])
        if item["pubDate"]:
            fe.pubDate(item["pubDate"])
        fe.guid(item["link"], permalink=True)

    fg.rss_file(output_file)
    print(f"RSS feed generated: {output_file}")

if __name__ == "__main__":
    articles = fetch_news_articles()
    generate_rss(articles)
