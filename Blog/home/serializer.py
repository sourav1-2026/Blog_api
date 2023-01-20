from rest_framework import serializers
from .models import BlogModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogModel
        exclude=['created_at','updated_at']
                                                                                  