from rest_framework.viewsets import GenericViewSet
from tournament.models import Tournament, RankSignificance, Application, ApplicationStatus, Document, Region, ParticipantList, WeightCategory
from rest_framework import mixins
from tournament.serializers   import TournamentSerializer, RankSignificanceSerializer, ApplicationSerializer, ApplicationStatusSerializer, DocumentSerializer, RegionSerializer, ParticipantListSerializer,  WeightCategorySerializer, TournamentCreateSerializer, RankSignificanceCreateSerializer, ApplicationCreateSerializer,ApplicationStatusCreateSerializer, DocumentCreateSerializer, RegionCreateSerializer, ParticipantListCreateSerializer,WeightCategoryCreateSerializer
from django.contrib.auth import authenticate, login, logout



class TournamentsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    def get_serializer_class(self):
        if self.action in ("create","update"):
            return TournamentCreateSerializer
        return super().get_serializer_class()

class RankSignificanceViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = RankSignificance.objects.all()
    serializer_class = RankSignificanceSerializer

    def get_serializer_class(self):
        if self.action in ("create","update"):
            return RegionCreateSerializer
        return super().get_serializer_class()

class ApplicationViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,GenericViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_serializer_class(self):
        if self.action in ("create","update"):
            return ApplicationCreateSerializer
        return super().get_serializer_class()


class ApplicationStatusViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerializer

    def get_serializer_class(self):
        if self.action in ("create","update"):
            return ApplicationCreateSerializer
        return super().get_serializer_class()


class DocumentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get_serializer_class(self):
        if self.action in ("create","update"):
            return DocumentCreateSerializer
        return super().get_serializer_class()


class RegionViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,GenericViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get_serializer_class(self):
        if self.action in ("create","update"):
            return RegionCreateSerializer
        return super().get_serializer_class()


class ParticipantListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = ParticipantList.objects.all()
    serializer_class = ParticipantListSerializer

    def get_serializer_class(self):
        if self.action in ("create","update"):
            return ParticipantListCreateSerializer
        return super().get_serializer_class()




class WeightCategoryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = WeightCategory.objects.all()
    serializer_class = WeightCategorySerializer

    def get_serializer_class(self):
        if self.action in ("create","update"):
            return WeightCategoryCreateSerializer
        return super().get_serializer_class()