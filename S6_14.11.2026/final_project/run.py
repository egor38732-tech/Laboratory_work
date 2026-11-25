# -*- coding: utf-8 -*-
'''Точка входа. Выполняет анализ от загрузки до отчёта.'''
import json
from datetime import datetime
from pathlib import Path

import config
from src.load import load_trips
from src.prepare import prepare_trips
from src.analyze import kpi_by_carrier


def df_to_markdown(df):
    header = "| " + " | ".join(str(c) for c in df.columns) + " |"
    sep = "| " + " | ".join("---" for c in df.columns) + " |"
    rows = ["| " + " | ".join(str(v) for v in row) + " |"
            for row in df.itertuples(index=False)]
    return chr(10).join([header, sep] + rows)


def main():
    started = datetime.now()
    for folder in (config.PROCESSED_DIR, config.REPORTS_DIR):
        Path(folder).mkdir(parents=True, exist_ok=True)

    print("[1/4] загрузка")
    raw = load_trips(config.RAW_DIR, config.TRIPS_PATTERN)

    print("[2/4] подготовка")
    trips = prepare_trips(raw)

    print("[3/4] расчёт показателей")
    by_carrier = kpi_by_carrier(trips)
    csv_path = Path(config.PROCESSED_DIR) / "kpi_by_carrier.csv"
    by_carrier.to_csv(csv_path, index=False, encoding="utf-8")

    print("[4/4] отчёт")
    report_path = Path(config.REPORTS_DIR) / "report.md"
    report = chr(10).join(["# Показатели по перевозчикам", "", df_to_markdown(by_carrier), ""])
    report_path.write_text(report, encoding="utf-8")

    manifest = {
        "запуск": started.isoformat(timespec="seconds"),
        "длительность, с": round((datetime.now() - started).total_seconds(), 2),
        "параметры": {"TRIPS_PATTERN": config.TRIPS_PATTERN},
        "итоговые метрики": {"рейсов": len(trips), "перевозчиков": len(by_carrier)},
    }
    manifest_path = Path(config.PROCESSED_DIR) / "run_manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"    {csv_path}")
    print(f"    {report_path}")
    print(f"    {manifest_path}")
    print("ГОТОВО")


if __name__ == "__main__":
    main()
