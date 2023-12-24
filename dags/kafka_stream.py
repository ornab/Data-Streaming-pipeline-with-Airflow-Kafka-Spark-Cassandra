
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
# from kafka import KafkaProducer
# import json
# import requests
# import time  # Import the 'time' module

default_args = {

    'owner': 'ornab',
    'start_date': datetime(2023, 12, 23, 10, 00)

}

def get_data():
    import json
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    #print(json.dumps(res, indent=3))
    return res


def format_data(res):
    data = {}

    # Extracting and formatting name
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']

    # Extracting other details
    data['gender'] = res['gender']

    # Extracting and formatting address
    location = res['location']
    data['address'] = f"{location['street']['number']} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"

    # Adding email, phone, and cell
    data['email'] = res['email']
    data['phone'] = res['phone']
    data['cell'] = res['cell']

    # Extracting date of birth
    data['date_of_birth'] = res['dob']['date']

    # Extracting picture URLs
    data['picture_large'] = res['picture']['large']
    data['picture_medium'] = res['picture']['medium']
    data['picture_thumbnail'] = res['picture']['thumbnail']

    return data


def stream_data():
    import json
    from kafka import KafkaProducer
    import time

    res = get_data()
    res = format_data(res)

    #print(json.dumps(res, indent=3))

    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)

    producer.send('users_created', json.dumps(res).encode('utf-8'))



with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    streming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )


# Continuous Data Streaming

# def continuous_data_stream():
#     while True:
#         stream_data()
#         time.sleep(5)  # Adjust the time interval as needed
#
# if __name__ == "__main__":
#     continuous_data_stream()





