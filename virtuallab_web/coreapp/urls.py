from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from coreapp import views

app_name = 'coreapp'

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('lab/', views.lab, name='lab'),
    path('experiment/<int:id>', views.experiment, name='experiment'),
    # path('lab/physics/', views.lab_detail, name='lab-physics'),
    # path('lab/chemistry/', views.lab_detail, name='lab-chemistry'),
    # path('lab/biology/', views.lab_detail, name='lab-biology'),
    path('class/', views.classview, name='class'),
    path('result/', views.result, name='result'),
    path('recording/', views.recording, name='recording'),
    path('assignment/', views.lab, name='assignment'),
    path('chart/', views.chart, name='chart')
    # path('browse/', views.OrderView.as_view(), name='package-list'),
    # path('offer/', views.OfferView, name='offer-list'),
    # path('about/', views.aboutSection),
    # path('contact/', views.contactSection),
    # path('browse/item/<int:id>/', views.PackageDetails.as_view(), name='package-details'),
    # path('browse/item/<int:id>/submitReview/', views.submitReview),
    # path('browse/item/<int:id>/submitRating/', views.submitPackageRating),
    # path('browse/item/<int:id>/reactOn/', views.reactSubmit),
    #
    # path('browse/restaurants/<int:id>/', views.RestaurantDetails.as_view(), name='restaurant_detail'),
    #
    # path('browse/branches/<int:id>/', views.RestaurantBranchDetails.as_view(), name='Branch_detail'),
    # path('browse/branches/<int:id>/submitRating/', views.submitBranchRating),
    # path('browse/branches/<int:id>/submitReview/', views.submitReview),
    # path('browse/branches/<int:id>/reactOn/', views.reactSubmit),
    #
    # path('order/checkout/', views.CheckoutView.as_view(), name='checkout'),
    # path('order/checkout/bkashPayment', views.bkashPayment, name='bkashPayment'),

]
