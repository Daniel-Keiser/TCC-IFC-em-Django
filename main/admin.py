from django.contrib import admin
from .models import (Banda, Almossom, ProgramacaoAlmossom, Instrumento, Profile, Evento, Galeria)

class BandaInline(admin.TabularInline):

    model = Almossom.bandas.through
    extra = 3
    verbose_name = u"Banda"
    verbose_name_plural = u"Bandas"

class AlmossomAdmin(admin.ModelAdmin):
    model = Almossom
    exclude = ('bandas',)
    ('Advanced options', {
            'classes': ('collapse',),
            'inlines': ('BandaInline',)
            
    }),

class BandaAdmin(admin.ModelAdmin):
    model = Banda

    
admin.site.register(Banda, BandaAdmin)
admin.site.register(Profile)
admin.site.register(Almossom, AlmossomAdmin)
admin.site.register(ProgramacaoAlmossom)
admin.site.register(Instrumento)
admin.site.register(Evento)
admin.site.register(Galeria)