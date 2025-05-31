# Scouts UK News RSS Feed Generator

This project scrapes the latest articles from [scouts.org.uk/news](https://www.scouts.org.uk/news) and generates a valid RSS feed (`scouts_news.xml`) that can be subscribed to with any RSS reader.

## 🚀 Features

- Scrapes the latest news posts from The Scouts UK website
- Generates a valid RSS feed
- Automatically updates daily via **GitHub Actions**
- Hosted on **GitHub Pages** for public access

## 🛠️ Setup

### 1. Clone or Fork this repository

```bash
git clone https://github.com/yourusername/scouts-news-feed.git
cd scouts-news-feed
```

### 2. Install dependencies (for local testing)

```bash
pip install -r requirements.txt
```

## 🔁 Automate with GitHub Actions

This project includes a GitHub Actions workflow that:

1. Runs the Python scraper once per day
2. Commits the updated `scouts_news.xml` file
3. Deploys to GitHub Pages

### ✅ Enabled by default

After pushing this repo, go to **Settings → Pages** and:

- Set source to `gh-pages` branch
- Use `/` root folder

Your public RSS feed URL will be:

```
https://yourusername.github.io/scouts-news-feed/scouts_news.xml
```

## 📅 Cron Schedule

The workflow is scheduled to run **daily at 07:00 UTC**. Modify it in `.github/workflows/rss-update.yml`:

```yaml
schedule:
  - cron: '0 7 * * *'
```

## 📄 License

MIT License

## 🙌 Credits

Created by [Your Name]. Not affiliated with The Scout Association.
