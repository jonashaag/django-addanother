from django.db import models


class Team(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Player(models.Model):

    name = models.CharField(max_length=20)
    current_team = models.ForeignKey(
        "Team", related_name="current_players",
        on_delete=models.CASCADE,
        help_text='This demonstrates the wrapper adding an "add" button only'
    )
    future_team = models.ForeignKey(
        "Team", related_name="future_players",
        on_delete=models.CASCADE,
        help_text='This demonstrates the wrapper adding both an "add" and an "edit" button'
    )
    previous_teams = models.ManyToManyField(
        "Team", related_name="ancient_players",
        help_text="This demonstrates the wrapper on a ManyToMany field"
    )

    def __str__(self):
        return self.name
