from django.db import models


class NomanPage(models.Model):
    """
    Model representing a Noman page.
    """

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["lang", "name"], name="unique_lang_name")
        ]

    lang = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}({self.lang})"


class Seealso(models.Model):
    """
    Model representing a "See Also" reference.
    """

    page = models.ForeignKey(
        NomanPage, on_delete=models.CASCADE, related_name="seealso"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.page.name} -> {self.reference}"


class Alias(models.Model):
    """
    Model representing an alias for a Noman page.
    """

    page = models.ForeignKey(
        NomanPage, on_delete=models.CASCADE, related_name="aliases"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.page.name} -> {self.alias}"
