import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_data(num_records):
    data = []
    for _ in range(num_records):
        
            costumer_id = fake.random_int(min=1000, max=9999)
            age = fake.random_int(min=18, max=80)
            gender = random.choice(['M', 'F'])
            location = random.choice(['SP','RJ','BA','DF','MG','RS','SC','PR','AM','PA'])
            purchase_amount = round(random.uniform(20.0, 10000.0), 2)
            product_category = random.choice(['Eletronicos', 'Livros', 'Saúde', 'Moda', 'Esportes', 'Beleza', 'Casa', 'Brinquedos', 'Games'])
            clicked_ad = random.choice(['Sim', 'Não'])
            browsing_history = [fake.url() for _ in range(random.randint(1, 10))]
            interested_score = round(random.uniform(0.5, 1.0), 2)
            churn_risk = random.choice(['Low', 'Medium', 'High'])

            data.append([costumer_id, age, gender, location, purchase_amount, product_category, clicked_ad, browsing_history, interested_score, churn_risk])
        
    return data

num_records = 10000
data = generate_data(num_records)

columns = [
    'Customer_ID',
    'Age',
    'Gender',
    'Location',
    'Purchase_Amount',
    'Product_Category',
    'Clicked_Ad', 
    'Browsing_History',
    'Interest_Score',
    'Churn_Risk'
]

df = pd.DataFrame(data, columns=columns)

df.to_csv('costumer_behavior.csv', index=False)

print('Arqivo gerado: costumer_behavior.csv')