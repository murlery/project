from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from tattoos.models import Style, Tattoo, Price, TattooArtist, TattooStudio
from tattoos.serializers import TattooSerializer,StyleSerializer,PriceSerializer,TattooArtistSerializer,TattooStudioSerializer, TattooCreateSerializer, TattooArtistCreateSerializer

class TattoosViewset(mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin,GenericViewSet):
    queryset = Tattoo.objects.all()
    serializer_class = TattooSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return qs 
            else:
                qs = qs.filter(user=self.request.user)
        return qs

    def get_serializer_class(self):
        if self.action in ("create","update"):
            return TattooCreateSerializer
        return super().get_serializer_class()
    

class StyleViewset(mixins.CreateModelMixin,mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

class PriceViewset(mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class TattooArtistViewset(mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = TattooArtist.objects.all()
    serializer_class = TattooArtistSerializer

    def get_serializer_class(self):
        if self.action in ("create","update"):
            return TattooArtistCreateSerializer
        return super().get_serializer_class()

class TattooStudioViewset(mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.RetrieveModelMixin,mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = TattooStudio.objects.all()
    serializer_class = TattooStudioSerializer

class UserProfileViewset(GenericViewSet):
    @action(url_path="info", detail = False, methods=["GET"])
    def get_url(self,reguest,*args,**kwargs):
        user = reguest.user
        data = {
            "is_authenticated" : user.is_authenticated
        }
        if user.is_authenticated:
            data.update({
                "is_superuser": user.is_superuser,
                "name":user.username
            })
        return Response(data)
    
            