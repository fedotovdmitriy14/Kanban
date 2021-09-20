from django.db import models


class Column(models.Model):
    name = models.CharField(max_length=50)

    DATE_CHOICES = [
        ('datetime', (
            ('true', 'required'),
            ('false', 'not required'),
        )
         ) ]
    INTEGER_CHOICES = [
        ('integer', (
            ('true', 'required'),
            ('false', 'not required'),
        )
         ) ]
    TEXT_CHOICES = [
        ('text', (
            ('true', 'required'),
            ('false', 'not required'),
        )
         ) ]
    TEXTAREA_CHOICES = [
        ('textarea', (
            ('true', 'required'),
            ('false', 'not required'),
        )
         )
    ]

    date_time_field = models.CharField(max_length=5, choices=DATE_CHOICES)
    integer_field = models.CharField(max_length=5, choices=INTEGER_CHOICES)
    text_field = models.CharField(max_length=5, choices=TEXT_CHOICES)
    textarea_field = models.CharField(max_length=5, choices=TEXTAREA_CHOICES)


class Card(models.Model):
    column_name = models.ForeignKey(Column, on_delete=models.CASCADE)
    # board_name = models.ForeignKey(Column, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    text = models.TextField()
    date = models.DateTimeField(null=True)
    integer = models.IntegerField(null=True)
    text_area = models.TextField(null=True)
    chars = models.CharField(max_length=52, null=True)



# class Card(models.Model):
#     name = models.CharField(null=True)
#     created = models.DateField(auto_created=True)
#     deadline = models.DateField(null=True)
#     text = models.TextField(null=True)
#     column = models.ForeignKey(Column, on_delete=models.CASCADE())
