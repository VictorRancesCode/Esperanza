from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from protect.core.models import Person

admin.site.unregister(Group)


@admin.register(Person)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','type_publication', 'is_active', 'slug', 'created', 'action')
    readonly_fields = ("action",)

    def action(self, obj):
        from django.utils.safestring import mark_safe
        if obj.is_active:
            return mark_safe(f'<button class="button" onclick="{obj.id}">Desactivar</button>')
        return mark_safe(f'<button class="button" onclick="{obj.id}">Activar</button>')

    action.allow_tags = True
