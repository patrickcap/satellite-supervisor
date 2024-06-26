import json
import pickle

import numpy as np
import numpy.typing as npt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier  # type: ignore[import-untyped]


class Model:

    def __init__(self) -> None:
        self._model = None  # type: RandomForestClassifier

    @classmethod
    def load_trained_model(cls, filename: str) -> 'Model':
        with open(filename, 'rb') as f:
            model = pickle.load(f)
        instance = cls()
        if not isinstance(model, RandomForestClassifier):
            raise AttributeError(
                f'The file {filename!r} does not contain a valid model. '
                f'Expected type {type(RandomForestClassifier)!r} but got {type(model)!r} '
            )
        instance._model = model
        return instance

    def predict(self, prepped_input: pd.DataFrame) -> int:
        return self._model.predict(prepped_input)