import json
import pickle

import numpy as np
import numpy.typing as npt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor  # type: ignore[import-untyped]


class Model:

    def __init__(self) -> None:
        self._model = None  # type: RandomForestRegressor
