from django.db import models

# Create your models here. Tablolarımızı oluşturmamıza yarayan kısım dosyasısıdır.

class GeneralSettings(models.Model):
    parameter = models.CharField(max_length=100)
    value = models.TextField()
    isActive = models.BooleanField(default=True)
    image = models.ImageField(upload_to='uploads',blank=True)


    def __str__(self):
        return self.parameter+" - "+self.value
    




class Menu(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, db_index=True)
    isActive = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    

class Home(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class IntroSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    introIcon = models.CharField(max_length=255, null=True)
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)



    def __str__(self):
        return self.title


class IntroSect(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)



    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    serviceIcon = models.CharField(max_length=255, null=True)
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ServiceTitle(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    value = models.TextField()
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()
    education = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    freelance = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads',blank=True)
    img = models.ImageField(upload_to='uploads',blank=True)
    cv = models.FileField(upload_to='cv',blank=True)
    isActive = models.BooleanField(default=True)
    


    def __str__(self):
        return self.title
    

class Skill(models.Model):
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    skillValue = models.SmallIntegerField()
    skillName = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)


    def __str__(self):
        return self.skillName


class SkillTitle(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    description = models.TextField()
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)


    def __str__(self):
        return self.title




class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    image = models.ImageField(null=True ,upload_to='uploads', blank=True)
    projectTitle = models.CharField(max_length=255)
    description = models.TextField()
    projectType = models.CharField(max_length=255)
    producer = models.TextField(max_length=255)
    projectLink = models.TextField()
    language = models.CharField(max_length=255)
    portfolioModal = models.CharField(max_length=255, null=True)
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE) 
    isActive = models.BooleanField(default=True)


    def __str__(self):
        return self.title



class PortoflioTitle(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.title




class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    name = models.CharField(null=True ,max_length=255)
    blogTitle = models.CharField(max_length=255, null=True)
    image = models.ImageField(null=True ,upload_to='uploads', blank=True)
    date = models.DateField(null=True ,auto_now_add=True)
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    blogId = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
    


class BlogTitle(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True ,upload_to='uploads', blank=True)
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Footer(models.Model):
    description = models.TextField()
    productInfo = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.description
