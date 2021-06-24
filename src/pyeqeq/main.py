# -*- coding: utf-8 -*-
import json
import pathlib
from typing import Union

import pyeqeq_eqeq

from .settings import CHARGE_DATA_PATH, IONIZATION_DATA_PATH


def run_on_cif(
    cif,
    output_type: str = "list",
    dielectric_screening: float = 1.2,
    h_electron_affinity: float = -2.0,
    charge_precision: int = 3,
    method: str = "ewald",
    num_cells_real: int = 2,
    num_cells_freq: int = 2,
    ewald_splitting: float = 50,
    ionization_data_path: Union[str, pathlib.Path] = IONIZATION_DATA_PATH,
    charge_data_path: Union[str, pathlib.Path] = CHARGE_DATA_PATH,
    outpath: Union[str, pathlib.Path] = None,
):
    output_type = output_type.lower()
    method = method.lower()
    result = pyeqeq_eqeq.run(
        cif,
        "json" if output_type == "list" else output_type,
        dielectric_screening,
        h_electron_affinity,
        charge_precision,
        method,
        num_cells_real,
        num_cells_freq,
        ewald_splitting,
        ionization_data_path,
        charge_data_path,
    )
    if outpath is not None:
        with open(outpath, "w") as handle:
            handle.write(result)

    if output_type == "list":
        return json.loads(result)
    return result