from django.db import models


class Score(models.Model):
    class Category(models.TextChoices):
        RONDALLA = "rondalla", "Rondalla"
        BAILE = "baile", "Baile galego"
        GAITA = "gaita", "Gaita, pandeireta e percusión"
        OUTROS = "outros", "Outros"

    title = models.CharField("título", max_length=200)
    category = models.CharField(
        "categoría", max_length=20, choices=Category.choices, default=Category.OUTROS
    )
    file = models.FileField("ficheiro", upload_to="scores/%Y/")
    notes = models.CharField("notas", max_length=300, blank=True)
    uploaded_at = models.DateTimeField("data de subida", auto_now_add=True)

    class Meta:
        ordering = ["category", "title"]
        verbose_name = "partitura"
        verbose_name_plural = "partituras"

    def __str__(self):
        return self.title
