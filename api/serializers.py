from rest_framework import serializers
from api.models import TrueCallerData
import json
import requests
from datetime import datetime


class TrueCallerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrueCallerData
        fields = ('id', 'name', 'gender', 'mobile', 'email', 'area', 'create_time')

    def create(self, validated_data):
        mobile = self.context['request'].query_params.get('mobile', None)
        url = 'https://www.truecaller.com/api/search?type=4&countryCode=in&q=' + mobile
        header = {
            'authorization': 'Bearer pS-iaJAgya6ng9wr5kB_tFfwY3r2-UHR',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'accept': 'application/json, text/plain, */*',
            'referer': 'https://www.truecaller.com/search/in/8527326325',
            'authority': 'www.truecaller.com',
            'cookie': '__cfduid=d24db64dda3e55355e61aa19fb96d43861512806307; G_ENABLED_IDPS=google; G_AUTHUSER_H=0; _ga=GA1.2.39977844.1512805092; _gid=GA1.2.1116580210.1512805092; XLBS3=XLBS2|Wiup+|WiuXp'
        }
        r = requests.get(url=url, headers=header)
        print(r.text)
        js = json.loads(r.text)["data"][0]
        validated_data['name'] = js.get("name")
        validated_data['gender'] = js.get("gender")
        validated_data['mobile'] = mobile
        try:
            validated_data['email'] = js["internetAddresses"][0]["id"]
            validated_data['area'] = js['addresses'][0]['area']
        except IndexError:
            validated_data['email'] = None
            validated_data['area'] = None
        validated_data['create_time'] = datetime.now()
        truecaller_data = TrueCallerData.objects.create(**validated_data)
        self.context['request'].session['id'] = truecaller_data.id
        self.context['request'].session['name'] = validated_data['name']
        self.context['request'].session['status'] = True
        self.context['request'].session['area'] = validated_data['area']
        return truecaller_data



class GameDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameData
        fields = ('id','user','car_type','nil_depreciation_cover','idv',
                  'personal_accident_cover',
                    'member_of_automobile_association',
                    'protection_for_accessories',
                    'voluntary_deductible',
                    'create_time',
                    'PA_cover_for_un_named_passengers')
        def create(self, validated_data):
            user = self.context['request'].query_params.get('user', None)
            game_data=GameData.objects.get(user=user)
            return  game_data

        def update(self, instance,validated_data):
            instance.car_type=validated_data.get('car_type', instance.car_type)
            instance.nil_depreciation_cover=validated_data.get('nil_depreciation_cover', instance.nil_depreciation_cover)
            instance.idv=validated_data.get('idv', instance.idv)
            instance.personal_accident_cover=validated_data.get('personal_accident_cover', instance.personal_accident_cover)
            instance.protection_for_accessories=validated_data.get('protection_for_accessories', instance.protection_for_accessories)
            instance.voluntary_deductible=validated_data.get('voluntary_deductible', instance.voluntary_deductible)
            instance.create_time=validated_data.get('create_time', datetime.now())
            instance.PA_cover_for_un_named_passengers=validated_data.get('PA_cover_for_un_named_passengers', instance.PA_cover_for_un_named_passengers)

            return instance




