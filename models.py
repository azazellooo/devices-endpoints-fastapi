import binascii
import os

from sqlalchemy import String, Integer, Column, Text, ForeignKey
import random

from sqlalchemy.orm import relationship

from db import Base

DEV_TYPES = ["emeter", "zigbee", "lora", "gsm"]


class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, unique=True)
    dev_id = Column(String(200), default=lambda: binascii.hexlify(os.urandom(6)).decode())
    dev_type = Column(String(120), default=lambda: random.choice(DEV_TYPES))
    endpoints = relationship('Endpoint', back_populates='device')


class Endpoint(Base):
    __tablename__ = 'endpoints'
    id = Column(Integer, primary_key=True, unique=True)
    device_id = Column(Integer, ForeignKey('devices.id'), nullable=True)
    comment = Column(Text)
    device = relationship('Device', back_populates='endpoints')


