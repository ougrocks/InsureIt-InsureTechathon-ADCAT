from django.shortcuts import render
from django.views import View
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from rest_framework.decorators import detail_route, renderer_classes
from rest_framework.views import APIView

from api.models import TrueCallerData
from api.serializers import TrueCallerSerializer
import requests, json


# Create your views here.


class TruecallerViewSet(viewsets.ModelViewSet):
    queryset = TrueCallerData.objects.all()
    serializer_class = TrueCallerSerializer


class GetPolicyQuotes(APIView):
    renderer_classes = (JSONRenderer,)
    def get(self, request,*args, **kwargs):
        url = "https://api.easypolicy.com/quoteservice.svc/web/getquotes"

        payload = "{\"EPQuoteId\":3341938,\"PartnerAgentId\":\"\",\"PartnerLeadId\":\"\",\"RequestType\":\"\",\"Requests\":[{\"__type\":\"TermRequest:#ServiceEntities\",\"Features\":null,\"ProductId\":3,\"IsOffline\":true,\"CityID\":766,\"DateOfBirth\":\"/Date(744748200000)/\",\"Gender\":\"M\",\"IsTobacco\":false,\"PayingMode\":null,\"PolicyTerm\":0,\"SelectedRiders\":null,\"SumAssured\":8000000,\"UserInputIncome\":400000,\"MinAnnualIncomeRange\":3,\"MaxAnnualIncomeRange\":4,\"riderList\":null,\"MonthlyIncome\":30000}],\"ServiceTimeOut\":0,\"utmCompaign\":\"eTerm_Business\",\"utmMedium\":\"Compare_Life_Insurance\",\"utmSource\":\"Google_ppc\",\"utmTerm\":\"\",\"BrowserId\":\"1f6d4203a28bd497b1a1fb38d6171cec\"}"
        headers = {
            'accept': "application/json, text/plain, */*",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.9",
            'connection': "keep-alive",
            'content-length': "622",
            'content-type': "application/json;charset=UTF-8",
            'host': "api.easypolicy.com",
            'origin': "https://www.easypolicy.com",
            'referer': "https://www.easypolicy.com/Application/Term?CPID=MzM0MTkzOA",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            'cache-control': "no-cache",
            'postman-token': "23b360f7-a982-c6ff-af18-b7ac2628cc84"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        return Response(json.loads((response.text)))
