# -*- coding: utf-8 -*-
'''Слой 3. Расчёт показателей по перевозчикам.'''


def kpi_by_carrier(trips):
    return (trips.groupby("carrier")
            .agg(trips_count=("trip_id", "count"),
                 revenue=("cost_rub", "sum"),
                 avg_weight=("weight_t", "mean"),
                 avg_delay=("delay_h", "mean"),
                 max_cost=("cost_rub", "max"),
                 delayed_share=("delay_h", lambda s: (s > 0).mean()))
            .round(2)
            .sort_values("revenue", ascending=False)
            .reset_index())
