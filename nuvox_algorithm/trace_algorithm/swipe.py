from dataclasses import dataclass
from typing import List


@dataclass
class TracePoint:
    """Data class for a single point within a Swipe trace."""
    x: float  # x∈(0, 1) is x coordinate relative to top-left of key pad.
    y: float  # y∈(0, 1) is y coordinate relative to top-left of key pad
    t: float  # t∈ℝ is the time (s) at which this point was recorded relative to start of swipe.
    key_id: str  # ID (1-9) of key that this point belongs to on the keyboard.

    def __post_init__(self):
        assert 0.0 <= self.x <= 1.0
        assert 0.0 <= self.y <= 1.0

    def __repr__(self):
        return f'TracePoint(x={self.x:.2f}, y={self.y:.2f}, t={self.t:.2f}, key_id={self.key_id})'


@dataclass
class Swipe:
    """Data class for a single Swipe."""
    id: int                         # ID of swipe in database.
    user_id: int                    # ID of user who generated swipe.
    device_type: str                # pc/mobile/tablet
    trace: List[TracePoint]         # List of TracePoint objects.
    target_text: str                # Word user intended to swipe.
    target_kis: str                 # Target key-id-sequence.
    trace_matches_text: bool        # Whether trace sufficiently matches text.

    def __repr__(self):
        return f'Swipe(target_text={self.target_text}, trace_matches_text={self.trace_matches_text})'
