from django.test import TestCase

from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from .models import Memory


class MemoryTest(TestCase):

    client_class = Memory
    demo_user = User.objects.get(pk=1)

    def MemoryCreationTest(self):
        print("Starting memory creation tests")
        test_1 = Memory.objects.create(
            name="Test 1",
            comment="a"*500,
            location=Point(100,10),
            author=self.demo_user,
        )
        User.objects.get()
        Memory.objects.create(
            name="Test 2",
            comment="a"*500,
            location=Point(100,10),
            author=self.demo_user,
        )

    
    def MemoryListTest(self):
        demo_user_memories = self.demo_user.memory_set.all()
