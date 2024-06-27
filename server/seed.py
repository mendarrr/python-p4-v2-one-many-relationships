#!/usr/bin/env python3
# server/seed.py

import datetime
from app import app
from models import db, Employee, Review, Onboarding

with app.app_context():

    # Delete all rows in tables
    Employee.query.delete()
    Review.query.delete()
    Onboarding.query.delete()

    # Add model instances to database
    uri = Employee(name="Uri Lee", hire_date=datetime.datetime(2022, 5, 17))
    tristan = Employee(name="Tristan Tal",
                       hire_date=datetime.datetime(2020, 1, 30))
    db.session.add_all([uri, tristan])
    db.session.commit()

    # 1..many relationship between Employee and Review
    uri_2023 = Review(year=2023,
                      summary="Great web developer!",
                      employee=uri)
    tristan_2021 = Review(year=2021,
                          summary="Good coding skills, often late to work",
                          employee=tristan)
    tristan_2022 = Review(year=2022,
                          summary="Strong coding skills, takes long lunches",
                          employee=tristan)
    tristan_2023 = Review(year=2023,
                          summary="Awesome coding skills, dedicated worker",
                          employee=tristan)
    db.session.add_all([uri_2023, tristan_2021, tristan_2022, tristan_2023])
    db.session.commit()

    # 1..1 relationship between Employee and Onboarding
    uri_onboarding = Onboarding(
        orientation=datetime.datetime(2023, 3, 27),
        employee=uri)
    tristan_onboarding = Onboarding(
        orientation=datetime.datetime(2020, 1, 20, 14, 30),
        forms_complete=True,
        employee=tristan)
    db.session.add_all([uri_onboarding, tristan_onboarding])
    db.session.commit()