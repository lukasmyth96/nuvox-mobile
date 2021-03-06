from typing import List, Dict

from django.core.exceptions import ValidationError

from nuvox_algorithm.utils.string_funcs import all_char_subsequences
from nuvox_algorithm.core import nuvox_keyboard

from games.models import Game


def validate_game_has_not_expired(game: Game):
    if game.has_expired:
        raise ValidationError('game has expired')


def validate_trace(trace: List[Dict[str, float]]):
    """Validate that trace is List[Dict[str, float]] where
    each trace point is a dict with keys 'x', 'y' and 't' that
    all map to float values."""
    if not trace:
        raise ValidationError('Field "trace" cannot be empty')

    if not isinstance(trace, list):
        raise ValidationError('Field "trace" must be a list')

    for trace_point in trace:
        validate_trace_point(trace_point)


def validate_trace_point(trace_point: Dict[str, float]):
    if not isinstance(trace_point, dict):
        raise ValidationError('Each trace point must be a dict')

    if not set(trace_point.keys()) == {'x', 'y', 't'}:
        raise ValidationError(f'Each trace point have keys x, y, t but found'
                              f'point with keys: {trace_point}')

    if not all([type(val) in (int, float) for val in trace_point.values()]):
        raise ValidationError(f'Each trace point must contain floats or integers.')


def trace_matches_target_text(trace: List[Dict[str, float]],
                              target_text: str) -> bool:
    """Returns True if trace is valid and matches target text else False."""
    try:
        validate_trace(trace)
    except ValidationError:
        return False

    trace_kis = nuvox_keyboard.trace_to_kis(trace)
    target_text_kis = nuvox_keyboard.text_to_kis(target_text, skip_invalid_chars=True)
    return (trace_kis[0] == target_text_kis[0]) and \
           (trace_kis[-1] == target_text_kis[-1]) and \
           (target_text_kis in all_char_subsequences(trace_kis))
