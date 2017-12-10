from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="index.html")


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        try:
            del request.session['name']
            del request.session['id']
            del request.session['status']
            #return render(request, template_name="index.html")
            return redirect('/')
        except:
            return redirect('/')

class VehicleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="vehicle.html")

class AgentView(View):
    def get(self, request, *args, **kwargs):

        return render(request, template_name="agent.html")

class AreaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="area.html")

class GameView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="game.html")
