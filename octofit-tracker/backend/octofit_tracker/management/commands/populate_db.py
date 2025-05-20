from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        user1 = User(email='user1@example.com', name='User One', password='password1')
        user1.save()
        user2 = User(email='user2@example.com', name='User Two', password='password2')
        user2.save()

        # Create test teams
        team1 = Team(name='Team Alpha', members=[user1, user2])
        team1.save()

        # Create test activities
        activity1 = Activity(user=user1, type='Running', duration=30)
        activity1.save()
        activity2 = Activity(user=user2, type='Cycling', duration=45)
        activity2.save()

        # Create test leaderboard
        leaderboard1 = Leaderboard(team=team1, points=100)
        leaderboard1.save()

        # Create test workouts
        workout1 = Workout(name='Morning Yoga', description='A relaxing yoga session to start the day.')
        workout1.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
