from .models import Feedback
from rest_framework import serializers




class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    feedback_id=serializers.ReadOnlyField()
    class Meta:
        model=Feedback
        fields="__all__"
