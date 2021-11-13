from typing import List
from fastapi import FastAPI, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from tools import is_anagram
from serializers import DeviceCreate, AnagramWords, Endpoint, DeviceGet
import models
from settings import redis_init
from db import SessionLocal


app = FastAPI()
db = SessionLocal()
redis = redis_init()


@app.get("/isanagram", status_code=status.HTTP_200_OK)
def anagram(words: AnagramWords):
    message = is_anagram(words.first_word, words.second_word)
    if message:
        redis.incr("counter")
    return {"message": message, "Counter": redis.get("counter")}


@app.post("/devices", response_model=DeviceGet, status_code=status.HTTP_201_CREATED)
def device_create(device: DeviceCreate):
    new_device = models.Device()
    db.add(new_device)
    db.commit()
    return new_device


@app.post("/devices-set/{endpoint_id}", status_code=status.HTTP_201_CREATED)
def def_create_10_devices(device: DeviceCreate, endpoint_id: int):
    devs_no_endpoint = [models.Device() for i in range(5)]
    db.add_all(devs_no_endpoint)
    devs_with_endpoint = []

    endpoint_list = [
        db.query(models.Endpoint).filter(models.Endpoint.id == endpoint_id).first()
        for i in range(5)
    ]
    for e in endpoint_list:
        new_device = models.Device()
        new_device.endpoints.append(e)
        session: Session = db
        session.add(new_device)
        session.flush()
        session.commit()
        db.commit()
        devs_with_endpoint.append(new_device)
    db.commit()
    return devs_no_endpoint + devs_with_endpoint


@app.post("/endpoints", response_model=Endpoint, status_code=status.HTTP_201_CREATED)
def endpoint_create(endpoint: Endpoint):
    new_endpoint = models.Endpoint(comment=endpoint.comment)
    db.add(new_endpoint)
    db.commit()
    return new_endpoint


@app.get("/devs-no-endpoint", status_code=status.HTTP_200_OK)
def get_devices_without_endpoint():
    devs_no_endpoint = (
        db.query(models.Device).filter(~models.Device.endpoints.any()).all()
    )
    grouped_devices_by_type = (
        db.query(models.Device.dev_type, func.count(models.Device.id))
        .filter(~models.Device.endpoints.any())
        .group_by(models.Device.dev_type)
        .all()
    )
    return dict(grouped_devices_by_type)


@app.get("/devices", response_model=List[DeviceGet], status_code=status.HTTP_200_OK)
def get_all_devices():
    devices = db.query(models.Device).all()
    return devices
