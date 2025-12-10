"""
Copyright 2014 Omer Gertel
Copyright 2025 Inmanta

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from .counter import Counter
from .gauge import CallbackGauge, Gauge, SimpleGauge
from .histogram import Histogram
from .meter import Meter
from .timer import Timer
from .base_metric import BaseMetric

__all__ = ["Counter", "CallbackGauge", "Gauge", "SimpleGauge", "Histogram", "Meter", "Timer", "BaseMetric"]

any_meter = Histogram | Meter | Gauge | Timer | Counter | BaseMetric
