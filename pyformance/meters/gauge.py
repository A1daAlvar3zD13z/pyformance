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

from typing import Callable, Union


class Gauge:
    """
    A base class for reading of a particular.

    For example, to instrument a queue depth:

    class QueueLengthGaguge(Gauge):
        def __init__(self, queue):
            super(QueueGaguge, self).__init__()
            self.queue = queue

        def get_value(self):
            return len(self.queue)

    """

    def get_value(self):
        "A subclass of Gauge should implement this method"
        raise NotImplementedError()


class CallbackGauge(Gauge):
    """
    A Gauge reading for a given callback
    """

    def __init__(self, callback) -> None:
        "constructor expects a callable"
        super(CallbackGauge, self).__init__()
        self.callback = callback

    def get_value(self):
        "returns the result of callback which is executed each time"
        return self.callback()


class SimpleGauge(Gauge):
    """
    A gauge which holds values with simple getter- and setter-interface
    """

    def __init__(self, value) -> None:
        "constructor accepts initial value"
        super(SimpleGauge, self).__init__()
        self._value = value

    def get_value(self):
        "getter returns current value"
        return self._value

    def set_value(self, value) -> None:
        "setter changes current value"
        # XXX: add locking?
        self._value = value


AnyGauge = Gauge[float | int]
