class GardenError(Exception):
    def __init__(self, error_message: str = "Unknown garden error"):
        super().__init__(error_message)


class PlantError(GardenError):
    def __init__(self, error_message: str = "Unknown plant error"):
        super().__init__(error_message)


class WaterError(GardenError):
    def __init__(self, error_message: str = "Unknown water error"):
        super().__init__(error_message)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print()
    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught WaterError: {error}")
        print()
    try:
        print("Testing catching all garden errors...")
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
