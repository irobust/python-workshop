def remainder_division(a, b):
    if(b == 0):
        raise ZeroDivisionError
    result = a // b
    remainder = a % b

    return (result, remainder)

def main():
    try:
        result, remainder = remainder_division(10, 0)
    except ZeroDivisionError as e:
        print(f'Divide by zero: {e}')
        result, remainder = remainder_division(10, 1)

        _, remainder = remainder_division(10, 1)
        print(remainder)
        
    except Exception as e:
        print(f'Error:{e}')
    finally:
        print(f"Result is {result} and remainder is {remainder}")

if __name__ == '__main__':
    main()