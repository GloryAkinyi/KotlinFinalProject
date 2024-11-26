from django.contrib import admin
from myapp.models import User, Product, Appointment, Contact, Member

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(Member)


