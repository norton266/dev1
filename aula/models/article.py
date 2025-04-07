from django.db import models
from .reporter import Reporter
from .magazine import Magazine
from .base_model import BaseModel

class Article(BaseModel):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter,
                                 on_delete=models.RESTRICT)
    magazine = models.ManyToManyField(Magazine, null=True, blank=True,
                                      through="Publication",
                                      through_fields=("article", "magazine"))
    def __str__(self):
        return self.title