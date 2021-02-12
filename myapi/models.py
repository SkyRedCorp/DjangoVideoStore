from django.db import models

class USER(models.Model):
    User_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)

    def __str__(self):
        return "%s %s" % (self.Name, self.Surname)

class MOVIE(models.Model):
    Movie_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()
    
    def __str__(self):
        return self.Name

class STORE(models.Model):
    Store_id = models.IntegerField(primary_key=True)
    Address = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)

    def __str__(self):
        return self.Address

class INVENTORY(models.Model):
    Item_id = models.IntegerField(primary_key=True)
    ID_movie = models.ForeignKey(MOVIE, on_delete = models.DO_NOTHING)
    ID_store = models.ForeignKey(STORE, on_delete = models.DO_NOTHING)
    Quantity = models.IntegerField()

    def __str__(self):
        return str(self.ID_movie)

class RENTAL(models.Model):
    ID_register = models.IntegerField(primary_key=True)
    ID_store = models.ForeignKey(STORE, on_delete = models.DO_NOTHING)
    ID_user  = models.ForeignKey(USER, on_delete = models.DO_NOTHING)
    ID_item = models.ForeignKey(INVENTORY, on_delete = models.DO_NOTHING)
    Checkout_date = models.DateField()
    Return_date = models.DateField()

    def __str__(self):
        return str(self.ID_register)
