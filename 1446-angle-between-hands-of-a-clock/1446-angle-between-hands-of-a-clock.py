class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_ = minutes / 5
        hour_ = hour + ((1/12)*(minutes_))

        diff = abs(hour_ - minutes_)
        angle = (360*diff)/12                  # 12-->360
        return min(angle,360-angle)