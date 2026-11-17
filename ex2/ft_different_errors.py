def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        print("Testing operation 0...")
        int("abc")
    elif (operation_number == 1):
        print("Testing operation 1...")
        42 / 0
    elif (operation_number == 2):
        print("Testing operation 2...")
        open("/non/existent/file")
    elif (operation_number == 3):
        print("Testing operation 3...")
        "hello" + 42
    else:
        print("Testing operation 4...")
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as error:
            if isinstance(error, ValueError):
                print(f"Caught ValueError: {error}")
            elif isinstance(error, ZeroDivisionError):
                print(f"Caught ZeroDivisionError: {error}")
            elif isinstance(error, FileNotFoundError):
                print(f"Caught FileNotFoundError: {error}")
            elif isinstance(error, TypeError):
                print(f"Caught TypeError: {error}")
            else:
                print("Operation completed successfully")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
