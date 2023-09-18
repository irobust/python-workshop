def key_error():
    dict1 = dict(a=10, b=20)
    list1 = [1,2,3,4]
    try:
        print(dict1['c'])
        print(list1[4])
    except IndexError as e:
        print(f"Error:{e}")
    except KeyError as e:
        print(f"Dict Error: {e}")
    except Exception as e:
        print(f"Generic error message: {e}")
    finally:
        print('Keep running program!')

def value_error():
    try:
        a = int(input("Please input number: "))
    except ValueError:
        a = 0
        print('Invalid input, please input [0-9].')

def main():
    key_error()

if __name__ == "__main__":
    main()
