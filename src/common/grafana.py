from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import List

import pytz
import requests

APIKEY = ''
URL = ''
AUTH = (
    '', APIKEY
)


@dataclass
class GrafanaMessage:
    name: str
    value: float
    time: int
    metric: str = None
    interval: int = 10
    unit: str = ''
    mtype: str = 'count'
    tags: List[str] = field(default_factory=lambda: [])

    def __post_init__(self):
        self.name = f'etl.{self.name}'
        self.metric = self.name


def send_metric_to_grafana(name, value) -> None:
    msg = GrafanaMessage(
        name,
        value,
        time=int(datetime.now(pytz.timezone('Europe/Moscow')).timestamp())
    )
    print(msg)
    requests.post(
        URL,
        json=list(map(asdict, [msg])),
        auth=AUTH,
    ).raise_for_status()
