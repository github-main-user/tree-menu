from django.core.exceptions import ValidationError
from django.db import models
from django.urls import NoReverseMatch, reverse


class Menu(models.Model):
    name = models.SlugField(unique=True, help_text="Menu Name")

    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name="items",
        help_text="Menu which containt the item",
    )
    title = models.CharField(max_length=255, help_text="Title of the item")
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children",
        help_text="Parent of this item",
    )

    url = models.CharField(max_length=255, help_text="URL (can be named or absolute)")
    named_url = models.BooleanField(
        default=False, help_text="Is selected URL named or not"
    )

    def get_absolute_url(self):
        if self.named_url:
            try:
                return reverse(self.url)
            except NoReverseMatch:
                return "#"
        return self.url

    def clean(self):
        if self.parent:
            if self.parent == self:
                raise ValidationError("Element can't be parent of him self")

            ancestor = self.parent
            while ancestor:
                if ancestor == self:
                    raise ValidationError("Circular dependency in the menu")
                ancestor = ancestor.parent

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["id"]
