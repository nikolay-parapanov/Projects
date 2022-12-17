from django.core.exceptions import ValidationError
from django.test import TestCase
from django.test import Client

from tri.authh.forms import SignUpForm
from tri.authh.models import AppUser
from tri.common.validators import validate_only_letters
from tri.marketplace.models import MarketItems


class MyTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def testOnlyLetersValidator(self):
        validate_only_letters("Nikolay")

        with self.assertRaises(ValidationError) as context:
            validate_only_letters("Nikolay1")

        assert context.exception.message == 'Only letters are allowed'

        with self.assertRaises(ValidationError) as context:
            validate_only_letters("1Nikolay")

        assert context.exception.message == 'Only letters are allowed'


    def testModelsCreation(self):
        user = AppUser(first_name = "Petar", last_name="Ivanov")
        assert user.full_name == "Petar Ivanov"
        assert not user.full_name == "PetarIvanov"

        with self.assertRaises(ValidationError) as exception_context:
            user.full_clean()
            user.save()

        user.username = "petarivanov"
        user.password = "aptor123123"
        user.email = "petar@microsoft.com"
        user.gender = "male"

        user.full_clean()
        user.save()

        item = MarketItems()
        with self.assertRaises(ValidationError) as exception_context:
            item.full_clean()
            item.save()

        item.name = "Shoes"
        item.price = 101
        item.user_id = user.id
        item.full_clean()
        item.save()

        assert len(AppUser.objects.all()) == 1
        assert len(MarketItems.objects.all()) == 1


    def testSignUpForm(self):
        data = {
            'username': 'username',
        }

        form = SignUpForm(data)
        assert not form.is_valid()

        data = {
            'username': "user1024",
            "password1": "nikiniki123",
            "password2": "nikiniki123",
            "first_name": "Niki",
            "last_name": "Parapanov",
            "age": "12",
            "gender": "male",
            "email": "niki@gmail.com"
        }

        form = SignUpForm(data)
        assert form.is_valid()

    def testApp(self):
        response = self.test_client.get("/marketpla1ce/")
        assert response.status_code == 404

        response = self.test_client.get("/marketplace/")
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'marketplace/marketplace-list.html')
        assert 'In order to use the functionality' in response.content.decode()






