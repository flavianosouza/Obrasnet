from django.db import models
# from django_mysql.models import ListCharField

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        unique=True
    )
    desciption = models.CharField(
        max_length=255,
        null=True
    )
    sheetname = models.CharField(
        max_length=100,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Material(models.Model):
    title = models.CharField(
        max_length=255,
        db_index=True
    )
    image = models.TextField(
        null=True
    )
    # specification = ListCharField(
    #     base_field=models.CharField(max_length=200),
    #     size=100,
    #     max_length=(100 * 200),
    #     null=True
    # )
    specification = models.TextField(
        null=True
    )

    ref = models.CharField(
        max_length=30, 
        db_index=True,
        null=True
    )

    price = models.TextField(
        null=True
    )

    description = models.TextField(
        null=True
    )

    advantage = models.TextField(
        max_length=255,
        null=True
    )

    documentation = models.TextField(
        null=True
    )

    features = models.TextField(
        null=True
    )

    url = models.URLField()

    state = models.BooleanField(
        default = True
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        default = 1
    )

    created_at = models.DateTimeField(auto_now_add = True, null=True)

    def __str__(self):
        return self.title, self.image, self.description, self.url

class Design(models.Model):
    title = models.CharField(max_length=255)
    squere = models.FloatField()

    def __str__(self):
        return self.title
    