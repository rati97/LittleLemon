from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Menu.objects.create(title="Khinkali", price="1.50", inventory=99)
        Menu.objects.create(title="Churchkhela", price="5.40", inventory=55)

    def test_getall(self):
        khinkali = Menu.objects.get(title="Khinkali")
        churchkhela = Menu.objects.get(title="Churchkhela")
        khinkali_serializer = MenuSerializer(khinkali)
        churchkhela_serializer = MenuSerializer(churchkhela)
        khinkali_response = self.client.get(f"/restaurant/menu/{khinkali.id}")
        churchkhela_response = self.client.get(f"/restaurant/menu/{churchkhela.id}")
        self.assertEqual(khinkali_serializer.data, khinkali_response.json())
        self.assertEqual(churchkhela_serializer.data, churchkhela_response.json())
