import logging
import openai
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.views import View


class NewsDataView(View):
    """
    Class-based view to get news data in JSON format.

    Attributes:
        data (list): List of dictionaries containing news data.
    """

    def get_top_news_url_list(self):
        url = "https://news.am/eng/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        top_news_div = soup.find("div", class_="news-list short-top")
        top_news_url = [a.get("href") for a in top_news_div.find_all("a")]
        return top_news_url

    def get_ai_summary(self, paragraph):
        try:
            openai.api_key = "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"
            paragraph_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": paragraph
                        + " Give me short summary for this paragraph",
                    }
                ],
            )
            return paragraph_completion.choices[0]["message"]["content"]
        except Exception as e:
            logging.info(e)
            return paragraph

    def get_new_data(self, url):
        """
        Extracts title, image, and description from a news article URL.

        Args:
        - url (str): URL of the news article.

        Returns:
        - dict: Contains 'title', 'image', and 'description' keys with corresponding values.
        """
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            if "tech.news.am" in url:
                article = soup.find(id="opennewstext")
                title = article.find("h1").get_text() if article.find("h1") else None
                image = article.find("img").get("src") if article.find("img") else None
                if image and "https" not in image:
                    image = f"https://tech.news.am/{image}"
                video = ""
            else:
                article = soup.find("div", class_="article-text")
                title = str(soup.find("div", class_="article-title").text.strip())
                if article.find("iframe"):
                    video = article.find("iframe").get("src")
                    image = ""
                else:
                    image = (
                        article.find("img").get("src") if article.find("img") else None
                    )
                    if image and "https" not in image:
                        image = f"https://news.am/{image}"
                    video = ""
            paragraph = article.find("p").get_text() if article.find("p") else None
            return {
                "title": title,
                "image": image,
                "description": self.get_ai_summary(paragraph),
                "video": video,
            }

        except Exception as e:
            logging.info(f"Unable to scrape the site URL: {url}")
            logging.info(e)
            return {"title": "", "image": "", "description": "", "video": ""}

    def get(self, request):
        """
        Handle GET requests to fetch news data.

        Args:
            request: The HTTP request object.

        Returns:
            JsonResponse: JSON response containing the news data.
        """
        data = []
        for url in self.get_top_news_url_list():
            if "https" not in url:
                url = f"https://news.am{url}"
            data.append(self.get_new_data(url))
        return JsonResponse(data, safe=False)
