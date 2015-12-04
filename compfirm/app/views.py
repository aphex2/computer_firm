from __future__ import division
from itertools import chain

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Count

from app.models import Product, PC, Printer, Laptop


class HomeView(View):
    """ Class based home view """

    template = 'home.html'

    def get(self, request):
        return render(request, self.template, {})


class GetPCMarkersView(View):
    """
    View returns markers producing at least three different PC models
    """

    template_name = "tasks/20.html"

    def get(self, request):
        products = Product.objects.order_by('maker')
        markers = Product.objects.filter(type="PC") \
                                 .values("maker") \
                                 .annotate(pc_count=Count("maker")) \
                                 .filter(pc_count__gte=3)
        data = {
            "products": products,
            "markers": markers,
        }
        return render(request, self.template_name, data)


class GetHighestPriceModelView(View):
    """
    Returns model numbers of all types, with the highest
    price of all the available database products.
    """

    template_name = "tasks/24.html"

    def get(self, request):
        pcs = PC.objects.values("model", "price")
        laptops = Laptop.objects.values("model", "price")
        printers = Printer.objects.values("model", "price")

        # Create an iterator for all models
        models_iterator = list(chain(pcs, laptops, printers))

        data = {
            "model": max(models_iterator, key=lambda x: x["price"]),
            "products": models_iterator,
        }
        return render(request, self.template_name, data)


class GetProductsRateView(View):
    """
    Returns the percentage ratio of the number of models of each type of
    products to the total number of models of the marker.
    """

    template_name = "tasks/58.html"

    @staticmethod
    def get_rate(ptype, marker):
        # Get number of models of each type of products 
        type_model = Product.objects.values("type", "maker").annotate(Count("model", distinct=True))

        # Get total number of models of the maker
        maker_model = Product.objects.values("maker").annotate(Count("model", distinct=True))

        total = [element["model__count"] for element in maker_model if element["maker"] == marker]
        type_count = [element["model__count"] for element in type_model
                      if element["maker"] == marker and element["type"] == ptype]

        if not type_count or not total:
            return "0%"
        return "{0:.2%}".format(type_count[0] / total[0])

    def get(self, request):
        products = Product.objects.order_by('maker')
        makers = products.values_list("maker", flat=True).distinct()
        types = Product.objects.values_list("type", flat=True).distinct()

        # Create dictionaries for each marker-type bunch
        result = (dict(maker=m, type=t, rate=self.get_rate(t, m)) for m in makers for t in types)

        data = {
            "result": result,
            "products": products
        }
        return render(request, self.template_name, data)


class GetOneTypeMarkersView(View):
    """
    Returns markers that produce only printers or only PC (at least 3 models)
    """

    template_name = "tasks/85.html"

    def get(self, request):
        products = Product.objects.order_by('maker')

        # Get markers produce only PC (at least 3 models)
        pcs = Product.objects.filter(type="PC") \
                             .values_list("maker", flat=True) \
                             .annotate(Count("model")) \
                             .filter(model__count__gte=3)

        printers = Product.objects.filter(type="Printer").values_list("maker", flat=True)

        # Get markers that produce only printers or only PC
        once = set(pcs) ^ set(printers)
        markers = Product.objects.filter(maker__in=once) \
                                 .values("maker") \
                                 .annotate(Count("type", distinct=True)) \
                                 .filter(type__count=1)
        data = {
            "products": products,
            "markers": markers
        }
        return render(request, self.template_name, data)
