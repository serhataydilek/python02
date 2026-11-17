def input_temperature(temp_str: str) -> int:
    result = int(temp_str)
    if result > 0 and result < 40:
        return result
    else:
        if result < 0:
            raise ValueError(
                f"{result}°C is too cold for plants (min 0°C)")
        elif result > 40:
            raise ValueError(
                f"{result}°C is too hot for plants (min 40°C)")


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    for temp_str in ("100", "-50"):
        print(f"\nInput data is '{temp_str}'")

        try:
            temperature = input_temperature(temp_str)
            print(f"Temperature is now {temperature}°C")

        except ValueError as error:
            print(f"Caught input_temperature error: {error}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
