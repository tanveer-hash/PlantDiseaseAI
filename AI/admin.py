from django.contrib import admin
from .models import Profile, Disease, Plant, Detection

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'plant', 'name', 'keyword',)

    sortable_by = ('plant', 'name')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'premium', 'detections_count', 'detections_allowed',)


class DetectionAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'profile', 'start_time', 'plant_type' , '_complete', 'time_taken')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Plant)
admin.site.register(Disease,DiseaseAdmin)
admin.site.register(Detection, DetectionAdmin)
