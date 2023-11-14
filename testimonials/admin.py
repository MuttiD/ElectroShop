from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    """ Class to handle Testimonial in Admin Panel """
    list_display = ['name', 'product', 'delivery', 'quality',
                    'overall', 'posted_date']
    search_fields = ['name', 'product__name']
    actions = ['delete_selected_testimonials']

    def delete_selected_testimonials(self, request, queryset):
        for testimonial in queryset:
            testimonial.delete()

    delete_selected_testimonials.short_description = "Delete \
        selected testimonials"


admin.site.register(Testimonial, TestimonialAdmin)
