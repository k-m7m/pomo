import math
import sys
import time
from pomo.models import PomoParam


class PomoApp:
    def __init__(self):
        self.param = PomoParam.parse_arguments()

    def run(self):
        count = 0
        while True:
            self._countdown(self.param.work, "Work Time")
            count += 1
            if count % self.param.count != 0:
                self._countdown(self.param.short_break, "Short Break")
            else:
                self._countdown(self.param.long_break, "Long Break")

    @staticmethod
    def _countdown(duration: int, message: str) -> None:
        end_time = time.monotonic() + duration
        sec: int | None = None

        while True:
            remaining = max(0, math.ceil(end_time - time.monotonic()))

            if remaining != sec:
                sec = remaining
                minutes, seconds = divmod(sec, 60)
                PomoApp._overwrite(f"{message}: {minutes:02}:{seconds:02}")

            if remaining == 0:
                break

            time.sleep(0.1)

    @staticmethod
    def _overwrite(text: str):
        sys.stdout.write("\r\033[2K")
        sys.stdout.write(text)
        sys.stdout.flush()
