from django.db import models


class Team(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Player(models.Model):

    name = models.CharField(max_length=20)
    current_team = models.ForeignKey(
        "Team", related_name="current_players",
        help_text="This demonstrate the wrapper adding a create button only"
    )
    future_team = models.ForeignKey(
        "Team", related_name="future_players",
        help_text="This demonstrate the wrapper adding both a create and an edit button"
    )
    previous_teams = models.ManyToManyField(
        "Team", related_name="ancient_players",
        help_text="This demonstrate the wrapper on a ManyToMany field"
    )

    def __str__(self):
        return self.name
