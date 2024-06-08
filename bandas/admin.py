from django.contrib import admin

from .models import Musica

admin.site.register(Musica)

from .models import Album

admin.site.register(Album)

from .models import Banda

admin.site.register(Banda)
