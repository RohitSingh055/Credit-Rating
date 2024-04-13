import json
import sys
sys.path.append(r'C:\Users\ASUS\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages')
import requests


url = "http://127.0.0.1:8000/predict"


input_data_for_model = {
    'chk_acct': 0,
    'duration': 6,
    'history': 2,
    'purpose_of_credit': 6,
    'credit_amount': 1169,
    'balance': 4,
    'employment': 2,
    'install_rate': 4,
    'marital_status': 3,
    'real_estate': 3,
    'age': 67,
    'other_installment': 1,
    'num_credits': 2,
    'job': 1,
    'phone': 0,
    'foreign': 1
}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data = input_json)

print(response.text)