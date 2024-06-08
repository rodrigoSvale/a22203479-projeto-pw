from django.contrib import admin

from .models import Festival

admin.site.register(Festival)

from .models import Localizacao

admin.site.register(Localizacao)

from .models import Banda

admin.site.register(Banda)

