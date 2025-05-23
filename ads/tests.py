from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Ad, ExchangeProposal
from django.urls import reverse

class AdTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username="user1", password="pass")
        self.user2 = User.objects.create_user(username="user2", password="pass")

        self.ad1 = Ad.objects.create(
            user=self.user1,
            title="Велосипед",
            description="Горный велосипед, почти новый.",
            category="Спорт",
            condition="used"
        )
        self.ad2 = Ad.objects.create(
            user=self.user2,
            title="Книга по Django",
            description="Отдам за любую другую книгу.",
            category="Книги",
            condition="new"
        )

    def test_ad_creation(self):
        self.assertEqual(Ad.objects.count(), 2)
        self.assertEqual(self.ad1.title, "Велосипед")

    def test_ad_edit_by_owner(self):
        self.client.login(username="user1", password="pass")
        response = self.client.post(
            reverse("ads:ad_edit", args=[self.ad1.pk]),
            {"title": "Обновлено", "description": "новое", "category": "Спорт", "condition": "used"}
        )
        self.ad1.refresh_from_db()
        self.assertEqual(self.ad1.title, "Обновлено")

    def test_ad_edit_by_not_owner_forbidden(self):
        self.client.login(username="user2", password="pass")
        response = self.client.post(
            reverse("ads:ad_edit", args=[self.ad1.pk]),
            {"title": "Хак!", "description": "ха", "category": "Спорт", "condition": "used"}
        )
        self.ad1.refresh_from_db()
        self.assertNotEqual(self.ad1.title, "Хак!")

    def test_ad_delete(self):
        self.client.login(username="user1", password="pass")
        response = self.client.get(reverse("ads:ad_delete", args=[self.ad1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Ad.objects.filter(pk=self.ad1.pk).exists())

    def test_search_filter(self):
        response = self.client.get(reverse("ads:ad_list") + "?q=Django")
        self.assertContains(response, "Книга по Django")
        self.assertNotContains(response, "Велосипед")

class ExchangeProposalTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username="user1", password="pass")
        self.user2 = User.objects.create_user(username="user2", password="pass")

        self.ad1 = Ad.objects.create(
            user=self.user1,
            title="Ноутбук",
            description="MacBook Air",
            category="Электроника",
            condition="used"
        )
        self.ad2 = Ad.objects.create(
            user=self.user2,
            title="Гитара",
            description="Акустическая",
            category="Музыка",
            condition="used"
        )

    def test_create_proposal(self):
        self.client.login(username="user1", password="pass")
        response = self.client.post(
            reverse("ads:proposal_create"),
            {
                "ad_sender": self.ad1.pk,
                "ad_receiver": self.ad2.pk,
                "comment": "Обменяю на гитару"
            }
        )
        self.assertEqual(ExchangeProposal.objects.count(), 1)
        proposal = ExchangeProposal.objects.first()
        self.assertEqual(proposal.status, "pending")
        self.assertEqual(proposal.comment, "Обменяю на гитару")
