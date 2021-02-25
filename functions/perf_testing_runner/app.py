import os
import requests
import boto3

session = boto3.Session()
firehoseClient = session.client('firehose')

def lambda_handler(event, context):
    uri = event['uri']
    website1 = os.environ['WEBSITE1']
    website2 = os.environ['WEBSITE2']
    deliveryStream = os.environ['DeliveryStreamName']

    #website1 = 'https://www.colypointobserver.com.au/'
    #website2 = 'http://nvi.com.au/'
    #Getting the first URL
    url = website1 + uri
    response = requests.get(url, timeout=6)

    timeElabsed1 = round(response.elapsed.total_seconds(),5)
    payload = {
            "domain":website1,
            "uri":uri,
            "elapsed": str(timeElabsed1),
        }

    full_payload1 = {**payload, **response.headers}
    
    print(full_payload1)

    url = website2 + uri
    response = requests.get(url, timeout=6)
    print(str(round(response.elapsed.total_seconds(),5)))

    timeElabsed2 = round(response.elapsed.total_seconds(),5)
    payload = {
            "domain":website2,
            "uri":uri,
            "elapsed": str(timeElabsed2),
        }

    full_payload2 = {**payload, **response.headers}

    print(full_payload2)

    print('Time elabsed from site1:'+str(timeElabsed1)+', time elabsed from site2:'+str(timeElabsed2))

    response = client.put_record_batch(
            DeliveryStreamName=deliveryStream,
            Records=[
                {
                    'Data': json.dumps(payload1).encode('utf-8')
                },
                {
                    'Data': json.dumps(payload2).encode('utf-8')
                }
            ]
        )
    return 'success'


