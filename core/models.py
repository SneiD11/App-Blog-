from django.db import models

class Author(model.model):

    name = models.CharField(
        max lenght=30,
        help_text="name of the author"
        Null=False
        blank=false
        ) 
        
    last_name = models.CharField(
        max lenght=30,
        help_text="last name of the author"
        Null=False
        blank=false
        ) 

     nacionality = models.CharField(
        max lenght=30,
        ) 

    email=models.EmailField(
        null=false
        blank=false
        unique=True
    )

    created=models.DateTimeField(auto_now_add=true)
    update= models.DateTimeField(auto_now=true)


class EntryBlog (models.model): 
    author=models.ForeingKey(author, on_delete=models.CASCADA, related_name="entry blog")
    conten= models.textfield()

    
