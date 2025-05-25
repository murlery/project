from django.db import models


class WeightCategory(models.Model):
    gender = models.CharField(max_length=10)
    weight = models.FloatField()

    class Meta:
        verbose_name = "Весовая категория"
        verbose_name_plural = "Весовые категории"

    def __str__(self):
        return f"{self.gender}, до {self.weight} кг"

class Tournament(models.Model):
    LEVEL_CHOICES = [
        ('областной', 'Областной'),
        ('федеральный', 'Федеральный'),
        ('всероссийский', 'Всероссийский'),
        ('международный', 'Международный')
    ]

    name = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    age_category = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    registration_deadline = models.DateField()

    class Meta:
        verbose_name = "Турнир"  # Пример verbose name на русском языке.
        verbose_name_plural = "Турниры" # Пример для множественного числа

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

    def __str__(self):
        return self.name

class ApplicationStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)


    class Meta:
        verbose_name = "Статус заявки"
        verbose_name_plural = "Статусы заявок"

    def __str__(self):
        return self.name


class Application(models.Model):
   
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE,null=True)
    trainer_name = models.CharField(max_length=255)
    sport_rank = models.CharField(max_length=50)
    status = models.ForeignKey(ApplicationStatus, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    weight_category = models.ForeignKey(WeightCategory, on_delete=models.SET_NULL, null=True)

    # Анкетные данные
    athlete_name = models.CharField(max_length=255)
    athlete_birth_date = models.DateField()
    athlete_gender = models.CharField(max_length=10)
    athlete_region = models.CharField(max_length=100)
    athlete_federal_district = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка от {self.athlete_name} "


class Document(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='documents')
    
    passport = models.FileField(upload_to='documents/passport/', null=True, blank=True)
    birth_certificate = models.FileField(upload_to='documents/birth_certificate/', null=True, blank=True)
    oms_policy = models.FileField(upload_to='documents/oms_policy/', null=True, blank=True)
    accident_insurance = models.FileField(upload_to='documents/accident_insurance/', null=True, blank=True)
    medical_clearance = models.FileField(upload_to='documents/medical_clearance/', null=True, blank=True)
    school_certificate = models.FileField(upload_to='documents/school_certificate/', null=True, blank=True)
    rank_assignment_order = models.FileField(upload_to='documents/rank_assignment/', null=True, blank=True)
    antidoping_certificate = models.FileField(upload_to='documents/antidoping/', null=True, blank=True)
    consent_to_personal_data = models.FileField(upload_to='documents/consent/', null=True, blank=True)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return f"Документы для заявки {self.application.id}"


class ParticipantList(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE,null=True)
    userApplication = models.ForeignKey(Application, on_delete=models.CASCADE,null=True)
    sport_rank = models.CharField(max_length=50)
    weight_category = models.ForeignKey(WeightCategory, on_delete=models.SET_NULL, null=True)
    federal_district = models.CharField(max_length=100)
    birth_date = models.DateField()

    class Meta:
        verbose_name = "Участник турнира"
        verbose_name_plural = "Список участников"

    def __str__(self):
        return f"участник на {self.tournament.name}"


class RankSignificance(models.Model):
    tournament = models.OneToOneField(Tournament, on_delete=models.CASCADE,null=True)
    region_count = models.IntegerField()
    participant_count = models.IntegerField()
    rank_level = models.CharField(max_length=50)  # МС, КМС, 1 разряд и т.д.

    class Meta:
        verbose_name = "Разрядная значимость"
        verbose_name_plural = "Разрядные значимости"

    def __str__(self):
        return f"Разрядная значимость для {self.tournament.name}"