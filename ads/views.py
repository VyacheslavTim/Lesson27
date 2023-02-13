import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Job


# Create your views here.


def root(request):
    return JsonResponse({"status": "ok"})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({"id": category.pk, "name": category.name})


class JobDetailView(DetailView):
    model = Job

    def get(self, request, *args, **kwargs):
        job = self.get_object()
        return JsonResponse({"id": job.pk,
                             "name": job.name,
                             "author": job.author,
                             "price": job.price,
                             "description": job.description,
                             "address": job.address,
                             "is_published": job.is_published
                             })


@method_decorator(csrf_exempt, name='dispatch')
class JobListCreateView(View):
    def get(self, request):
        job_list = Job.objects.all()
        return JsonResponse([{"id": job.pk,
                              "name": job.name,
                              "author": job.author,
                              "price": job.price,
                              "description": job.description,
                              "address": job.address,
                              "is_published": job.is_published
                              } for job in job_list], safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)
        new_ad = Job.objects.create(**ad_data)
        return JsonResponse({"id": new_ad.pk,
                             "name": new_ad.name,
                             "author": new_ad.author,
                             "price": new_ad.price,
                             "description": new_ad.description,
                             "address": new_ad.address,
                             "is_published": new_ad.is_published
                             })


@method_decorator(csrf_exempt, name='dispatch')
class CatListCreateView(View):
    def get(self, request):
        cat_list = Category.objects.all()
        return JsonResponse([{"id": cat.pk,
                              "name": cat.name
                              } for cat in cat_list], safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)
        new_cat = Category.objects.create(**ad_data)
        return JsonResponse({"id": new_cat.pk,
                             "name": new_cat.name
                             })
