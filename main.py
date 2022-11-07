import feedparser
import webbrowser


def main():
    print("\n")
    print("--Security Feed List--\n")
    print("[0]: The Hacker News")
    print("[1]: Mandiant Feed")
    print("[2]: Threat Post")
    print("[3]: Cisco Security Feed")
    print("[4]: Mcafee Security Feed")

    feed_list = ("https://feeds.feedburner.com/TheHackersNews?format=xml", "https://www.mandiant.com/resources/blog/rss.xml",
    "https://threatpost.com/feed/", "https://blogs.cisco.com%20/security/feed", "https://www.mcafee.com/blogs/feed/")

    user_input = int(input("\nEnter your selection (0-4): "))

    feed = feedparser.parse(feed_list[user_input])
    article_list = []
    article_link = []
    for i in range(5):
        article = feed.entries[i]
        titles = article.title
        link = article.link
        article_link.append(link)
        article_list.append(titles)

    article_num = 1
    for article in article_list:
        print("\n"'[{}] {}'.format(str(article_num), article))
        article_num += 1

    article_click = False
    while not article_click:
        user_click = int(input("\nChoose the article you would like to open (1-5): "))
        webbrowser.open(article_link[user_click - 1])
        article_click = True


main()

