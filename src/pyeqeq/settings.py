from importlib.resources import files

IONIZATION_DATA_PATH = str(files("pyeqeq").joinpath("data", "ionizationdata.dat"))
CHARGE_DATA_PATH = str(files("pyeqeq").joinpath("data", "chargecenters.dat"))
