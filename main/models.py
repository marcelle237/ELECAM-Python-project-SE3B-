from django.db import models

# Create your models here.
class ElectionStatistic(models.Model):
    election_year = models.IntegerField()
    candidate_name = models.CharField(max_length=100)
    party_name = models.CharField(max_length=100)
    votes_received = models.IntegerField()

    def __str__(self):
        return f"{self.candidate_name} ({self.party_name}) - {self.election_year}"

class Election(models.Model):
    year = models.IntegerField()
    voter_turnout = models.FloatField()
    total_registered = models.IntegerField()
    winner = models.CharField(max_length=255)

class PollingStation(models.Model):
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

class Quartier(models.Model):
    station=models.ForeignKey(PollingStation,related_name='quartiers', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
    