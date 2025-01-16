"""
Tests for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_success(self):
        """Test creating a user with email success."""
        email = "test@example.com"
        password = "password123"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email is normalized."""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@examPLE.com", "Test2@example.com"],
            ["tesT3@EXAMple.COM", "tesT3@example.com"],
        ]
        for from_email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=from_email, password="sample123"
            )
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raise_error(self):
        """Test creating a user without email raises an error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "sample123")

    def test_create_superuser_success(self):
        """Test creating a superuser success."""
        user = get_user_model().objects.create_superuser(
            email="admin@example.com", password="password123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
