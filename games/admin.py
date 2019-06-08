from django.contrib import admin

from .models import GameCategory, Game, Player, PlayerScore
# Register your models here.
admin.site.register(GameCategory)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(PlayerScore)