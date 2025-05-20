from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField(max_length=100)
    members = UserSerializer(many=True)

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField()
    user = UserSerializer()
    type = serializers.CharField(max_length=50)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField()
    team = TeamSerializer()
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()