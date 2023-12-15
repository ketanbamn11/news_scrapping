from django.http import JsonResponse
from django.views import View


class NewsDataView(View):
    """
    Class-based view to get news data in JSON format.

    Attributes:
        data (list): List of dictionaries containing news data.
    """

    data = [
        {
            "title": "Russia accepts violations recorded by Armenia television, radio commission",
            "image": "https://news.am/img/news/79/77/58/default.jpg",
            "description": "A meeting between the Ministry of High-Tech Industry of Armenia and the Ministry of Digital Development, Communications and Mass Media of Russia was held Thursday in Yerevan, on the matter of maintaining the provisions of the agreement, signed between the governments of the two countries, on cooperation in mass telecommunications."
        },
        {
            "title": "Putin: I don't think it’s in Armenia's interest to stop membership in CIS, EAEU, CSTO",
            "image": "https://i.ytimg.com/vi/aWPJ6x1WAho/sddefault.jpg",
            "description": "I do not think that it is in Armenia's interest to somehow terminate membership in the CIS, EAEU, and CSTO. Russian President Vladimir Putin stated this, answering the Mir television reporter’s question about the future of the Commonwealth of Independent States (CIS), taking into account the respective positions of Armenia and Moldova."
        },
        {
            "title": "Baku is against troops’ withdrawal from Armenia-Azerbaijan border",
            "image": "https://news.am/img/news/79/77/20/default.jpg",
            "description": "I will answer in brief: I do not agree with the opinion of the Armenian foreign minister. Azerbaijani FM Jeyhun Bayramov said this at Thursday’s joint news conference with his Turkish colleague, Hakan Fidan, commenting on Armenian foreign minister Ararat Mirzoyan's statement about the need for withdrawing the troops of Armenia and Azerbaijan from their border."
        },
        {
            "title": "Putin: We were not the ones who left Karabakh, it was Armenia that recognized Karabakh as part of Azerbaijan",
            "image": "https://i.ytimg.com/vi/aWPJ6x1WAho/sddefault.jpg",
            "description": "It was not us that left Karabakh; it was Armenia that recognized that Karabakh is part of Azerbaijan. This was announced by Russian President Vladimir Putin, answering the Mir television reporter’s question about the future of the Commonwealth of Independent States (CIS), taking into account the respective positions of Armenia and Moldova."
        },
        {
            "title": "Armenia ex-President Serzh Sargsyan on European Council head’s statement on Karabakh: Such words are zero guarantee",
            "image": "https://ae01.alicdn.com/kf/S3619e57974f148d087c950fe497cdf55q/300x250.jpg",
            "description": "The time will come, we will elaborate on what we meant when we made that statement. Armenia's third President Serzh Sargsyan told this to reporters Thursday outside a Yerevan court—and addressing the question of what he meant by saying that the Artsakh (Nagorno-Karabakh) “chapter” is not closed."
        },
    ]

    def get(self, request):
        """
        Handle GET requests to fetch news data.

        Args:
            request: The HTTP request object.

        Returns:
            JsonResponse: JSON response containing the news data.
        """
        return JsonResponse(self.data, safe=False)

