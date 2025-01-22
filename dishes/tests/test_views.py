from django.test import TestCase, Client
from django.urls import reverse
from dishes.models import Cook, DishType


class CookListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = Cook.objects.create_user(
            username="testuser",
            password="password123",
            first_name="Test",
            last_name="User",
            years_of_experience=5
        )
        for i in range(10):
            Cook.objects.create(
                username=f"cook_{i}",
                first_name=f"Cook {i}",
                last_name=f"LastName {i}",
                years_of_experience=i
            )

    def setUp(self):
        self.client = Client()
        self.client.login(username="testuser", password="password123")

    def test_cook_list_view_status_code(self):
        response = self.client.get(reverse("dishes:cook-list"))
        self.assertEqual(response.status_code, 200)

    def test_cook_list_view_template_used(self):
        response = self.client.get(reverse("dishes:cook-list"))
        self.assertTemplateUsed(response, "dishes/cook_list.html")


class DishTypeDetailViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.dish_type = DishType.objects.create(name="Main Course")
        cls.user = Cook.objects.create_user(
            username="testuser",
            password="password123",
            first_name="Test",
            last_name="User",
            years_of_experience=5
        )

    def setUp(self):
        self.client = Client()
        self.client.login(username="testuser", password="password123")

    def test_dish_type_detail_view_status_code(self):
        response = self.client.get(reverse("dishes:dish-type-detail", args=[self.dish_type.id]))
        self.assertEqual(response.status_code, 200)

    def test_dish_type_detail_view_template_used(self):
        response = self.client.get(reverse("dishes:dish-type-detail", args=[self.dish_type.id]))
        self.assertTemplateUsed(response, "dishes/dish_type_detail.html")

    def test_dish_type_detail_context(self):
        response = self.client.get(reverse("dishes:dish-type-detail", args=[self.dish_type.id]))
        self.assertIn("dishtype", response.context)
        self.assertEqual(response.context["dishtype"].name, "Main Course")
