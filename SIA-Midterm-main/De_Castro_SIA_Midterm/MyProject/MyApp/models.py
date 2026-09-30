from django.db import models

class PlayerProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    player_level = models.IntegerField(default=1)
    pals_captured = models.IntegerField(default=0)
    playtime_hours = models.DecimalField(max_digits=8, decimal_places=1, default=0)
    favorite_pal = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Pal(models.Model):
    RARITY_CHOICES = [
        ('common', 'Common'),
        ('rare', 'Rare'),
        ('epic', 'Epic'),
        ('legendary', 'Legendary'),
    ]

    profile = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE, related_name='pals')
    name = models.CharField(max_length=100)
    pal_type = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES, default='common')
    nickname = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.profile.username})"