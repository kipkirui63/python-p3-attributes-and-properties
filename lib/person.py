#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    pass
    def __init__(self, name=" ", job=" "):
        self.name = name
        self.job = job

        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")

        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")

        self.name = name.title()
