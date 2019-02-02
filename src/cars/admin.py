from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email', 'name', 'user__id']

    class Meta:
        model = Car

    def save_model(self, request, obj, form, change):
        '''Override admin save model'''
        if not change:
            obj.user = request.user
        else:
            obj.updated_by = request.user
        obj.save()

    def get_queryset(self, request):
        '''Limit the query set only for CUSTOMER to prevent information leaking'''
        qs = super(CarAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(Car, CarAdmin)


