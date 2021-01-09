from typing import Dict, List

from nuvox_algorithm.trace_algorithm.swipe import TracePoint


class TraceAlgorithm:
    def __init__(self):
        # The init method can be used to load a machine learning model or simply
        # set some configurations for your trace algorithm. You do not have to
        # use it if you do not need it.
        pass

    def predict_intended_kis(self, trace: List[TracePoint]) -> Dict[str, float]:
        """This function should receive a swipe trace (a chronological
        list of TracePoint objects) and returns a dictionary mapping possible
        key-id-sequences (KIS) to the predicted probability that the user
        intended to swipe that sequence of keys.

        Notes
        --------
        - The values (predicted probabilities) in the returned
        dictionary must be sum to 1.0 as the dictionary must describe
        a probability distribution.

        Example
        --------
        - If a user attempts to swipe the word 'beg', their trace will
        presumably pass over keys 1 --> 2 --> 3.
        - In this case the true intended KIS would be '123' because
        the word 'beg' requires b from key 1, e from key 2 and g from key 3.
        - For this input trace, this function may, for example, return:
          {
            '123': 0.8,
            '13': 0.2
          }
          thereby assigning a probability of 0.8 that the user intended the KIS
          1->2->3 and 0.2 probability that the user only intended 1->3.
        """
        pass
