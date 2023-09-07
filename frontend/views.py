from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from .models import GeneralSettings, Menu, Home, Service, Portfolio, PortoflioTitle, Blog, About, IntroSection, Skill,IntroSect, SkillTitle, ServiceTitle, BlogTitle, Footer
def index(request):
    # GeneralSettings tablosundan aktif ayarları çek
    settings = GeneralSettings.objects.filter(isActive=True).order_by('id')

    # Menüler tablosundan aktif menüleri çek
    active_menus = Menu.objects.filter(isActive=True)

    # Ana sayfa içeriklerini çek
    home_content = Home.objects.filter(menus__name='Home', isActive=True).first()

    intro_sections = IntroSection.objects.filter(menus__name='Home', isActive=True)

    intro_section = IntroSect.objects.filter(menus__name='Home', isActive=True).first()

    skill_contents = Skill.objects.filter(menus__name='About', isActive=True)

    skilTitle_contents = SkillTitle.objects.filter(menus__name='About', isActive=True).first()

    # Hizmet içeriklerini çek
    service_contents = Service.objects.filter(menus__name='Service', isActive=True)

    serviceTitle_contents = ServiceTitle.objects.filter(menus__name='Service', isActive=True).first()

    # Portfolyo içeriklerini çek
    portfolio_content = Portfolio.objects.filter(menus__name='Portfolio', isActive=True)

    portfolioTitle_contents = PortoflioTitle.objects.filter(menus__name='Portfolio', isActive=True).first()

    # Blog içeriklerini çek
    blog_contents = Blog.objects.filter(menus__name='Blog', isActive=True)

    blogTitle_contents = BlogTitle.objects.filter(menus__name='Blog', isActive=True).first()

    footer_contents = Footer.objects.filter(isActive=True).first()


    # Hakkında bilgilerini çek
    about_content = About.objects.filter(menus__name='About', isActive=True).last()


    

    return render(request, 'frontend/index.html', {
        'settings': settings,
        'menus': active_menus,
        'home_content': home_content,
        'intro_sections': intro_sections,
        'intros_section': intro_section,
        'skill_contents': skill_contents,
        'skilTitle_contents': skilTitle_contents,
        'service_contents': service_contents,
        'serviceTitle_contents': serviceTitle_contents,
        'portfolio_content': portfolio_content,
        'portfolioTitle_contents':portfolioTitle_contents,
        'blog_contents': blog_contents,
        'blogTitle_contents': blogTitle_contents,
        'footer_contents':footer_contents,
        'about_content': about_content,
    })





def redirect_to_section(request, section_id):
    if isinstance(section_id, int):
        if 1 <= section_id <= 5:
            if section_id == 1:
                # 1 yazıldığında ana sayfaya yönlendirme
                return redirect('/#site-header')
            elif section_id == 2:
                # 2 yazıldığında about sayfasına yönlendirme
                return redirect('/#about-section')  # Bu kısmı about sayfasına yönlendirme ile değiştir
            elif section_id == 3:
                # 3 yazıldığında portfolio sayfasına yönlendirme
                return redirect('/#portfolio-section')  # Bu kısmı portfolio sayfasına yönlendirme ile değiştir
            elif section_id == 4:
                # 4 yazıldığında service sayfasına yönlendirme
                return redirect('/#service-section')  # Bu kısmı service sayfasına yönlendirme ile değiştir
            elif section_id == 5:
                # 5 yazıldığında blog sayfasına yönlendirme
                return redirect('/#blog-section')  # Bu kısmı blog sayfasına yönlendirme ile değiştir
    return HttpResponseNotFound(render(request, 'frontend/404.html'))



def invalid_url_redirect(request, invalid_url):
    # Burada geçersiz URL'yi nasıl yönlendireceğinizi belirleyebilirsiniz.
    return render(request, 'frontend/404.html', status=404)