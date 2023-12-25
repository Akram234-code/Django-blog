from django.db import models
from django.urls import reverse

# class MyModelName(models.Model):
Create your models here.    
"""A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    # …


    # Metadata
    class Meta:
         ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
            return reverse('model-detail-view', args=[str(self.id)])

                def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name

         class CatalogConfig(AppConfig):

              default_auto_field = 'django.db.models.BigAutoField'
              class Meta:
    ordering = ['-my_field_name']

ordering = ['title', '-pubdate']
verbose_name = 'BetterName'
     def __str__(self):

            return self.my_field_name

def get_absolute_url(self):
    """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

   # Create a new record using the model's constructor.
   record = MyModelName(my_field_name="Instance #1")

# Save the object into the database.
record.save()

# Access model field values using Python attributes.
print(record.id) # should return 1 for the first record.
print(record.my_field_name) # should print 'Instance #1'

# Change record by modifying the fields, then calling save().
record.my_field_name = "New Instance Name"
record.save()





    o
      


 
    


        
        


