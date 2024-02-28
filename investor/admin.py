# from django.contrib import admin
# from investor.models import Investor,IndustrySubcategory, IndustryCategory


# class InvestorAdmin(admin.ModelAdmin):
#     list_display = ('investor', 'company_name', 'created_at', 'updated_at', 'deleted_at')
#     list_filter = ('is_active', 'is_deleted')
#     search_fields = ['investor','company_name']
 

# admin.site.register(Investor, InvestorAdmin)
# admin.site.register(IndustrySubcategory, IndustryCategory)

from django.contrib import admin
from investor.models import Investor, IndustryCategory, IndustrySubcategory

class InvestorAdmin(admin.ModelAdmin):
    list_display = ('investor', 'company_name', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('is_active', 'is_deleted')
    search_fields = ['investor', 'company_name']

class IndustrySubcategoryAdmin(admin.ModelAdmin):
    # Add any configuration you want for IndustrySubcategory admin
    pass

class IndustryCategoryAdmin(admin.ModelAdmin):
    # Add any configuration you want for IndustryCategory admin
    pass

admin.site.register(Investor, InvestorAdmin)
admin.site.register(IndustrySubcategory, IndustrySubcategoryAdmin)
admin.site.register(IndustryCategory, IndustryCategoryAdmin)


