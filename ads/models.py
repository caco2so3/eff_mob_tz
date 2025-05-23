from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    CONDITION_CHOICES = [
        ('new', 'Новый'),
        ('used', 'Б/У'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
CATEGORY_CHOICES = [
    ('спорт', 'Спорт'),
    ('ремонт', 'Ремонт'),
    ('техника', 'Техника'),
    ('кухня', 'Кухня'),
    ('автомобиль', 'Автомобиль'),
    ('другое', 'Другое'),
]

class Ad(models.Model):
    CONDITION_CHOICES = [
        ('new', 'Новый'),
        ('used', 'Б/У'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    

class ExchangeProposal(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('accepted', 'Принята'),
        ('rejected', 'Отклонена'),
    ]

    ad_sender = models.ForeignKey(Ad, related_name='sent_proposals', on_delete=models.CASCADE)
    ad_receiver = models.ForeignKey(Ad, related_name='received_proposals', on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Обмен: {self.ad_sender} → {self.ad_receiver} [{self.status}]"
