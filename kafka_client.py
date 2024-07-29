import requests
from dataclasses import asdict

class KafkaClient:
    def __init__(self, host: str) -> None:
        self.host = host
    
    def send(self, topic: str, message) -> None:
        url = self.host + '/api/kafkauniversal/write'
        response = requests.post(
            url=url,
            json={
                "businessKey": "aikerim",
                "channelId": "aikerim",
                "commitWhenRead": True,
                "guarantedWrite": True,
                "processName": "aikerim",
                "topic": topic,
                "message": message,
            }
        )
        print(response.json())
