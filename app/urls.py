"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from tournament import views
from rest_framework.routers import DefaultRouter
from tournament.api import TournamentsViewSet, RankSignificanceViewSet, ApplicationViewSet, ApplicationStatusViewSet, DocumentViewSet, RegionViewSet, ParticipantListViewSet, WeightCategoryViewSet
from django.urls import path
router = DefaultRouter()

router.register("rankSignificances", RankSignificanceViewSet, basename="rankSignificances")

router.register("applications", ApplicationViewSet, basename="applications")
router.register("applicationStatuses", ApplicationStatusViewSet, basename="applicationStatuses")
router.register("documents", DocumentViewSet, basename="documents")
router.register("regions", RegionViewSet, basename="regions")
router.register("participantLists", ParticipantListViewSet, basename="participantLists")
router.register("weightCategorys", WeightCategoryViewSet, basename="weightCategorys")
router.register("tournaments",TournamentsViewSet, basename="tournaments")


urlpatterns = [
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),  # endpoints для login/logout
    # path('api/login/', LoginView.as_view()),
    # path('api/logout/', LogoutView.as_view()),
    # path('api/whoami/', WhoAmIView.as_view()),
   # path('', views.ShowTattoosView.as_view()),
    path('', views.ShowTournamentsView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
