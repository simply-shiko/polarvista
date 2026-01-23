from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description =models.TextField(blank=True, null=True)
    image =models.ImageField(upload_to='destinations/', blank=True, null=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="places"
    )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    place_type = models.CharField(
        max_length=50,
        choices=[
            ("park", "National Park / Reserve"),
            ("beach", "Beach"),
            ("city", "City"),
            ("island", "Island"),
            ("cultural", "Cultural Site"),
            ("mountain", "Mountain"),
            ("lake", "Lake"),
        ]
    ) 
    image = models.ImageField(
        upload_to="places/" ,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class SafariPackage(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="packages"
    )
    places = models.ManyToManyField(Place,
    related_name="safari_packages",
    blank=True
    )
    title = models.CharField(max_length=200)
    overview =models.TextField(blank=True)
    duration_days = models.PositiveIntegerField(default=1)
    cover_image=models.ImageField(upload_to='safaris/', blank=True, null=True)
    destination=models.ForeignKey(Destination, on_delete=models.CASCADE,related_name='safari_packages')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title 

