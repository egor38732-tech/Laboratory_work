# -*- coding: utf-8 -*-
'''Слой 2. Подготовка дат и месяца рейса.'''
import pandas as pd


def prepare_trips(raw):
    trips = raw.copy()
    trips["date"] = pd.to_datetime(trips["date"])
    trips["month"] = trips["date"].dt.to_period("M").astype(str)
    return trips
