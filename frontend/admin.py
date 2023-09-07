from django.contrib import admin
from django.utils.html import format_html
from .models import GeneralSettings, Menu, Home, About, Portfolio, PortoflioTitle, Blog, Service, IntroSection, Skill, IntroSect, SkillTitle, ServiceTitle, BlogTitle,Footer


@admin.register(GeneralSettings)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ('parameter', 'value', 'isActive',)
    list_filter = ('isActive',)
    

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'isActive',)
    list_filter = ('isActive',)
    ordering = ['id']



@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'value', 'menus', 'isActive',)
    list_filter = ('menus',)
    ordering = ['id']




@admin.register(IntroSection)
class IntroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'introIcon', 'menus', 'isActive',)
    list_filter = ('menus',)
    ordering = ['id']

@admin.register(IntroSect)
class IntroSectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'menus', 'isActive',)
    list_filter = ('menus',)
    ordering = ['id']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('menus', 'skillValue', 'skillName', 'isActive',)
    list_filter = ('menus',)
    ordering = ['id']


@admin.register(SkillTitle)
class SkillTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'value', 'menus',)
    list_filter = ('menus',)
    ordering = ['id']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',  'menus',)
    list_filter = ('menus',)
    ordering = ['id']




@admin.register(ServiceTitle)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'menus',)
    list_filter = ('menus',)
    ordering = ['id']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'value', 'menus', 'name', 'email', 'age', 'education', 'phone', 'freelance', 'isActive','image')
    list_filter = ('menus', 'age')
    ordering = ['id']


    def resim(self, obj):
        return format_html('<img src="/uploads/{}" width="auto" height="20px" />'.format(obj.image))
    resim.short_description = 'Image'


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'projectType', 'image', 'menus', 'producer', 'projectLink', 'language')
    list_filter = ('menus', 'projectType', 'language')
    ordering = ['id']


@admin.register(PortoflioTitle)
class PortoflioTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'menus',)
    list_filter = ('menus',)
    ordering = ['id']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'name', 'image', 'date', 'blogTitle', 'menus')
    list_filter = ('menus', 'date')
    ordering = ['id']



@admin.register(BlogTitle)
class BlogTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'menus', 'isActive')
    list_filter = ('menus',)
    ordering = ['id']





@admin.register(Footer)
class BlogTitleAdmin(admin.ModelAdmin):
    list_display = ('description', 'productInfo', 'isActive')
    list_filter = ('description',)
    ordering = ['id']






# # Register your models here.


# @admin.register(GeneralSettings)
# class GeneralSettingsAdmin(admin.ModelAdmin):
#     list_display = ('parameter', 'value', 'isActive',) # Admin kısmında listelenecek verilerin görünmesini sağlıyor.
#     list_display_links = ('parameter', 'value',) # Üstüne tıklanınca içeriğe gitmemize yardımcı olan fonksiyon.
#     list_editable = ('isActive',) # Üstüne yani içeriğe gitmeden üzerinde değişiklik yapılmasına olanak sağlıyor.
#     list_filter = ('parameter', 'value',) # Filtreleme Parametlereini yan tarafa açar.
#     search_fields = ('parameter',) # Arama Çubuğu Ekler üst kısıma
#     ordering = ['id']







# @admin.register(Menu)
# class MenuAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug', 'isActive',)
#     list_display_links = ('name', 'slug',)
#     prepopulated_fields = {'slug':('name',),}
#     list_filter = ('name', 'isActive',)
#     list_editable = ('isActive',)
#     search_fields = ('name',)
#     ordering = ['id']



# @admin.register(Content)
# class ContentAdmin(admin.ModelAdmin):
#     list_display = ('title', 'menus', 'resim', 'date', 'slug', 'isActive',)
#     list_display_links = ('title', 'menus', 'resim',)
#     readonly_fields = ('resim',)
#     prepopulated_fields = {'slug':('title',),}
#     list_filter = ('title', 'menus',)
#     list_editable = ('isActive',)
#     search_fields = ('title','menus',)

#     def resim(self, obj):
#         return format_html('<img src="/media/{}" width="auto" height="20px" />'.format(obj.image))
#     resim.short_description = 'Image'
