from django.conf.urls import patterns, include, url

from app import views

urlpatterns = patterns("",
    url(r"^$", views.HomeView.as_view(), name="home"),
    url(r"^pc_markers/", views.GetPCMarkersView.as_view(), name="pc_markers"),
    url(r"^hightest_price/", views.GetHighestPriceModelView.as_view(), name="hightest_price"),
    url(r"^product_rate/", views.GetProductsRateView.as_view(), name="product_rate"),
    url(r"^one_type_markers/", views.GetOneTypeMarkersView.as_view(), name="one_type_markers"),
)