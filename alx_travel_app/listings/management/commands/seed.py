from django.core.management.base import BaseCommand
from django.db import transaction
from listings.models import Listing
import random

TITLES = [
    "Cozy Beachfront Cottage",
    "Urban Loft Downtown",
    "Mountain View Cabin",
    "Luxury City Apartment",
    "Countryside Farm Stay",
    "Modern Studio Near Station",
    "Lake House Retreat",
    "Historic Townhouse",
    "Eco-Friendly Bungalow",
    "Desert Oasis Villa",
]

LOCATIONS = [
    "Lagos, Nigeria",
    "Nairobi, Kenya",
    "Cairo, Egypt",
    "Accra, Ghana",
    "Cape Town, South Africa",
    "Marrakesh, Morocco",
    "Kampala, Uganda",
    "Johannesburg, South Africa",
    "Algiers, Algeria",
    "Zanzibar, Tanzania",
]

class Command(BaseCommand):
    help = "Seed the database with sample listings data."

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of listings to create (default: 10)'
        )

    @transaction.atomic
    def handle(self, *args, **options):
        count = options['count']
        created = 0

        self.stdout.write(self.style.NOTICE(f"Seeding {count} listings..."))

        for i in range(count):
            title = TITLES[i % len(TITLES)]
            location = LOCATIONS[i % len(LOCATIONS)]
            price = round(random.uniform(20, 300), 2)
            capacity = random.randint(1, 8)

            listing, was_created = Listing.objects.get_or_create(
                title=title,
                location=location,
                defaults={
                    'description': f"Sample description for {title} in {location}.",
                    'price_per_night': price,
                    'capacity': capacity,
                    'is_active': True,
                }
            )

            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Seeding complete. {created} new listings created."))