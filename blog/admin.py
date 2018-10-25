from django.contrib import admin
from .models import Post
from .models import Perfil

admin.site.register(Post)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')