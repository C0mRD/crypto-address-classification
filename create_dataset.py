import random
import string
import csv

def generate_tron_address():
    prefix = 'T'
    body = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=33))
    return prefix + body

def generate_monero_address():
    prefix = random.choice('48')
    body = ''.join(random.choices(string.ascii_lowercase + string.digits, k=94))
    return prefix + body

tron_addresses = []
monero_addresses = []

for _ in range(100000):
    tron_addresses.append([generate_tron_address(), 'Tron'])
for _ in range(100000):
    monero_addresses.append([generate_monero_address(), 'Monero'])

with open('dataset/raw_data/Tron_addresses.csv', 'w', newline='') as csvfile1:
    writer1 = csv.writer(csvfile1)
    writer1.writerow(['address', 'type'])
    writer1.writerows(tron_addresses)

with open('dataset/raw_data/Monero_addresses.csv', 'w', newline='') as csvfile2:
    writer2 = csv.writer(csvfile2)
    writer2.writerow(['address', 'type'])
    writer2.writerows(monero_addresses)