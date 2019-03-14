from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q

from .models import RestaurantLoction

def restaurant_listview(request):
    template_name = 'restaurant/restaurants_list.html'
    queryset = RestaurantLoction.objects.all()
    context = {
        "object_list":queryset

    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    queryset = RestaurantLoction.objects.all()
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLoction.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )

        else:
            queryset = RestaurantLoction.objects.all()
        
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLoction.objects.all()

   
    def get_object(self, *args,**kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLoction, id=rest_id)#Also id=pk
        return obj

   
