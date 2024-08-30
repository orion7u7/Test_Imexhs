from django.db import models
from django.core.validators import MinValueValidator
import numpy as np

# Create your models here.


# DeviceData model
class DeviceData(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    deviceName = models.CharField(max_length=100)
    avgBefore = models.FloatField(null=True, blank=True)
    avgAfter = models.FloatField(null=True, blank=True)
    dataSize = models.IntegerField(null=True, blank=True)
    data = models.JSONField()

    def __str__(self):
        return f"{self.deviceName} - {self.id}"

    # Calculate the average of the data before and after normalization
    def calculate_avg(self):
        data2 = [list(map(int, row.split())) for row in self.data]
        all_values = np.array(data2).flatten()

        self.avgBefore = np.mean(all_values)

        max_value = np.max(all_values)
        normalized_values = all_values / max_value

        self.avgAfter = np.mean(normalized_values)

        self.dataSize = all_values.size
    # Save the data
    def save(self, *args, **kwargs):
        self.calculate_avg()
        super().save(*args, **kwargs)