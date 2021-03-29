import factory
import os
import pytz
os.environ.setdefault('DJANGO_SETTINGS_MODULE','search_engine.settings')
import django
django.setup()
from factory.django import DjangoModelFactory
from core.models import User,Result,Keyword

class UserFactory(DjangoModelFactory):
    class Meta:
        model=User
    name=factory.Faker("first_name")

class KeywordFactory(DjangoModelFactory):
    class Meta:
        model=Keyword
    name=factory.Faker("sentence",nb_words=1,variable_nb_words=True)
class ResultFactory(DjangoModelFactory):
    class Meta:
        model=Result
    keyword=factory.SubFactory(KeywordFactory)
    user=factory.SubFactory(UserFactory)
    title=factory.Faker("sentence",nb_words=5,variable_nb_words=True)
    description=factory.Faker("sentence",nb_words=50,variable_nb_words=True)
    date=factory.Faker('date_time_this_year', tzinfo=pytz.utc)
