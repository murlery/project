from django.contrib import admin

# Register your models here.
from tournament.models import (
     Region, WeightCategory, Tournament, ApplicationStatus,
    Application, Document, ParticipantList, RankSignificance
)


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'age_category', 'location', 'start_date', 'end_date', 'registration_deadline']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'tournament']



@admin.register(WeightCategory)
class WeightCategoryAdmin(admin.ModelAdmin):
    list_display = ['gender', 'weight']
 


@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'tournament', 'trainer_name', 'sport_rank', 'status',
        'submission_date', 'athlete_name', 'athlete_region'
    ]
    

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = [
        'application',
        'passport',
        'birth_certificate',
        'oms_policy',
        'accident_insurance',
        'medical_clearance',
        'school_certificate',
        'rank_assignment_order',
        'antidoping_certificate',
        'consent_to_personal_data'
    ]
   


@admin.register(ParticipantList)
class ParticipantListAdmin(admin.ModelAdmin):
    list_display = ['userApplication', 'tournament', 'sport_rank', 'weight_category', 'federal_district', 'birth_date']
   


@admin.register(RankSignificance)
class RankSignificanceAdmin(admin.ModelAdmin):
    list_display = ['tournament', 'region_count', 'participant_count', 'rank_level']