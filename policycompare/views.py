from django.shortcuts import render

# Create your views here.
from django.views import View
import requests
import json


class PolicyCompareView(View):
    def get(self, request, *args, **kwargs):
        url = "http://127.0.0.1:8000/getquotes/"

        headers = {
            'cache-control': "no-cache",
            'postman-token': "279cc3d4-031d-527a-fbd3-1a5ff5f0802c"
        }

        response = requests.request("GET", url, headers=headers)

        json_obj = json.loads(response.text)
        quotes = json_obj['Quotes']
        return render(request, "policy.html", context={'quotes': quotes})
