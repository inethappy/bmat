import csv
import random

from faker import Faker

fake = Faker()
with open('test_file.csv', 'w', newline='') as fd:
    writer = csv.writer(fd)
    deps = [fake.city() for x in range(10)]
    for i in range(100):
        fake_data = [random.choice(deps), fake.date(), random.randint(1, 200)]
        random.shuffle(fake_data)
        writer.writerow(tuple(fake_data))
