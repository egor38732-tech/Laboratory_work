# -*- coding: utf-8 -*-
'''Слой 1. Загрузка рейсов за апрель и май.'''
from pathlib import Path

import pandas as pd


def load_trips(raw_dir, pattern):
    files = sorted(Path(raw_dir).glob(pattern))
    if not files:
        raise FileNotFoundError(f"В {raw_dir} нет файлов по шаблону {pattern}")

    frames = []
    for path in files:
        frame = pd.read_csv(path)
        frames.append(frame)
        print(f"    {path.name}: {len(frame)} строк")

    return pd.concat(frames, ignore_index=True)
