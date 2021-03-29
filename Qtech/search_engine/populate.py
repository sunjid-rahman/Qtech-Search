import random
from factories import (
    UserFactory,
    KeywordFactory,
    ResultFactory,
)
from core.models import User,Keyword,Result
from django.db import transaction
from django.core.management.base import BaseCommand

NUM_USERS = 5
NUM_Keywords = 8
NUM_Result=160
results_PER_keyword = 20
USERS_PER_Result = 1


models = [User, Keyword,Result]
for m in models:
    m.objects.all().delete()

print("Creating new data...")
# Create all the users
people = []
for _ in range(NUM_USERS):
    person = UserFactory()
    people.append(person)
    person.save()
# Add some users to clubs
keywords=[]
for _ in range(NUM_Keywords):
    key= KeywordFactory()
    # members = random.choices(
    #     people,
    #     k=USERS_PER_CLUB
    # )
    key.save()
    keywords.append(key)
    # club.user.add(*members)

# Create all the threads
for _ in range(NUM_Result):
    user = random.choice(people)
    keyword = random.choice(keywords)
    # Create comments for each thread
    result=ResultFactory(user=user,keyword=keyword)

    result.save()
