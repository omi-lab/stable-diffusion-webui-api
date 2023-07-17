import json
import requests
import io
import base64
from io import BytesIO
from pathlib import Path
import os
from PIL import Image, PngImagePlugin
from matplotlib import pyplot as plt

#Connect to existing SD webUI and tell it to create 4 photos of a foreground and a background pair
class Calls:

    def __init__(self) -> None:
   
        self.url = "http://127.0.0.1:7860"

    def get_txt2upscaledimgs(self,prompt:str,steps:int,iterations:int):


        payload = {
            "prompt": "beans beans beans",
            "steps": 5,
            "height": 512,
            "width": 512,
            "n_iter": 2,
        }

        response = requests.post(url=f'{self.url}/sdapi/v1/txt2upscaledimgs', json=payload) #txt2upscaledimgs
        rsp = response.json()
        # listo = []
        # for index, item in enumerate(rsp['images']):
        #     info = {
        #         "data": item,
        #         "name": index
        #         }
        #     listo.append(info)
        breakpoint()
        # need to see what structure result comes out in

if __name__ == "__main__":
    hi = Calls()
    hi.get_txt2upscaledimgs("beans beans beans",50,2)