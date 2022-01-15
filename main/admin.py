from django.contrib import admin
from .models import Diet
from .models import Cart
from .models import Customer
from .models import Category


admin.site.register(Diet)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Category)