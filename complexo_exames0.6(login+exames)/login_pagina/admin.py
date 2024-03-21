from django.contrib import admin
from .models import usuarios_cliente
from .models import usuarios_medico
from .models import exames

# Register your models here.
admin.site.register(usuarios_cliente)
admin.site.register(usuarios_medico)
admin.site.register(exames)