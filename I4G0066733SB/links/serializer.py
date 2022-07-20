from rest_framework import serializers
from .models import Link
from django.contrib.auth.models import User

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"