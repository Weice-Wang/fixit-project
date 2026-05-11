from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'pk': self.id})

class Item(models.Model):
    CATEGORY_OPTIONS = [
        ('mobile', 'Mobile'),
        ('electronics', 'Electronics'),
        ('gaming', 'Gaming'),
        ('tools_hardware', 'Tools & Hardware'),
        ('home_appliances', 'Home & Appliances'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_OPTIONS,
        default='other'
    )
    price = models.PositiveIntegerField()

    WARRANTY_OPTIONS = [
        (0, 'No Warranty'),
        (3, '3 Months'),
        (6, '6 Months'),
        (12, '1 Year'),
        (24, '2 Years'),
        (36, '3 Years'),
        (48, '4 Years'),
        (60, '5 Years'),
    ]
    warranty = models.PositiveIntegerField(
        choices=WARRANTY_OPTIONS,
        default=12
    )

    purchase_date = models.DateField()
    description = models.TextField(
        max_length=500
    )
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'item_id': self.id})
    

class Maintaining(models.Model):
    REPAIR_TYPE_OPTIONS = [
        ('repair', 'Repair'),
        ('replace', 'Replace Part'),
        ('service', 'Service'),
        ('upgrade', 'Upgrade'),
        ('cleaning', 'Cleaning'),
        ('inspection', 'Inspection'),
        ('other', 'Other'),
    ]

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='maintainings'
    )

    date = models.DateField('Maintaining date')

    repair_type = models.CharField(
        max_length=20,
        choices=REPAIR_TYPE_OPTIONS,
        default='repair'
    )


    description = models.TextField(
        blank=True
    )

    cost = models.PositiveIntegerField(
        default=0
    )

    service_provider = models.CharField(
        max_length=100,
        blank=True
    )

    is_completed = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f'{self.item.name} - {self.repair_type}'

    class Meta:
        ordering = ['-date']


