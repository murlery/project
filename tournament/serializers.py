from rest_framework import serializers


from tournament.models import Tournament, RankSignificance, Application, ApplicationStatus,Document, Region, ParticipantList, WeightCategory


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = "__all__"
class TournamentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = "__all__"

class RankSignificanceSerializer(serializers.ModelSerializer):
    tournament = TournamentSerializer(read_only=True)
    class Meta:
        model = RankSignificance
        fields = [
            'id',
            'tournament',
            'region_count',
            'participant_count',
            'rank_level'
        ]

class RankSignificanceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankSignificance
        fields = "__all__"
    

class RegionSerializer(serializers.ModelSerializer):

    tournament = TournamentSerializer(read_only=True)
    class Meta:
        model = Region
        fields = ['id', 'name','tournament']

class RegionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"



class WeightCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightCategory
        fields = ['id', 'gender', 'weight']

class WeightCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightCategory
        fields = "__all__"
    

class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = ['id', 'name']

class ApplicationStatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = "__all__"

class ApplicationSerializer(serializers.ModelSerializer):
    tournament = TournamentSerializer(read_only=True)
    status = ApplicationStatusSerializer(read_only=True)
    weight_category = WeightCategorySerializer(read_only = True)
    class Meta:
        model = Application
        fields = "__all__"

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
class ParticipantListSerializer(serializers.ModelSerializer):

    tournament = TournamentSerializer(read_only=True)
    userApplication = ApplicationSerializer(read_only=True)
    class Meta:
        model = ParticipantList
        fields = [
            'id', 'tournament', 'userApplication', 'sport_rank',
            'weight_category', 'federal_district', 'birth_date'
        ]
class ParticipantListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantList
        fields = "__all__"

class DocumentSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(read_only = True)
    class Meta:
        model = Document
        fields = [
            'id', 'application',
            'passport', 'birth_certificate', 'oms_policy',
            'accident_insurance', 'medical_clearance',
            'school_certificate', 'rank_assignment_order',
            'antidoping_certificate', 'consent_to_personal_data'
        ]

class DocumentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"