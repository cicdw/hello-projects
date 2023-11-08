from prefect import flow, get_run_logger
import pandas as pd


@flow(name="Hello World")
def hello_world():
    logger = get_run_logger()

    data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

    # load data into a DataFrame object:
    df = pd.DataFrame(data)
    logger.info(df)
