from prefect import flow


@flow
def hello(name: str = "chris"):
    print("=" * 100)
    print("HOW DO YOU LIKE THEM APPLES?")
    print("=" * 100)
