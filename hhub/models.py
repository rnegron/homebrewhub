from django.contrib.postgres.fields import ArrayField
from django.db import models


class Entry(models.Model):
    class Platforms(models.TextChoices):
        GAME_BOY = "GB", "Game Boy"
        GAME_BOY_COLOR = "GBC", "Game Boy Color"
        GAME_BOY_ADVANCE = "GBA", "Game Boy Advance"

    class TypeTags(models.TextChoices):
        GAME = "game", "Game"
        HOMEBREW = "homebrew", "Homebrew"
        DEMO = "demo", "Demo"
        HACKROM = "hackrom", "Hack ROM"
        MUSIC = "music", "Music"

    slug = models.TextField(
        primary_key=True,
        editable=False,
        help_text="Slug that uniquely identifies this entry",
    )
    platform = models.TextField(
        choices=Platforms.choices, help_text="The platform this entry was developed for"
    )
    developer = models.TextField(
        null=True, help_text="The developer of this entry, if any"
    )
    title = models.TextField(help_text="What this entry is called")
    typetag = models.TextField(
        null=True,
        choices=TypeTags.choices,
        default=TypeTags.GAME,
        help_text="What kind of entry this is",
    )
    tags = ArrayField(
        models.TextField(), null=True, help_text="Additional descriptors for this entry"
    )
    basepath = models.TextField(
        help_text="The base path for this entry in the local filesystem"
    )
    devtoolinfo = models.JSONField(
        null=True,
        help_text="Information on how this entry was developed, "
        "if any (using gbstoolsid)",
    )

    class Meta:
        verbose_name = "entry"
        verbose_name_plural = "entries"
        ordering = ["slug"]
        indexes = [
            models.Index(fields=["title"], name="title_idx"),
            models.Index(fields=["platform"], name="platform_idx"),
            models.Index(fields=["typetag"], name="typetag_idx"),
        ]

    def __str__(self):
        return f"{self.title} ({self.platform})"
