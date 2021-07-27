from django.db import models
from django import models


# Create your models here.
class Destination:
    id : int
    name : str
    img : str
    price : int
    desc : str
    offer : bool
