from django.contrib import admin
# from .models import Brand
import app.models

# Register your models here.
admin.site.register(app.models.Brand)
admin.site.register(app.models.Bodywood)
admin.site.register(app.models.Neckwood)
admin.site.register(app.models.Pickups)
admin.site.register(app.models.Color)
admin.site.register(app.models.GuitarPic)
admin.site.register(app.models.Order)
