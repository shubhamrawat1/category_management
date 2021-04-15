from django.db import models


class Category(models.Model):

    cat_name = models.CharField(max_length=120, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    cat_image = models.ImageField(upload_to='cat_images', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.cat_name

    class Meta():
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

