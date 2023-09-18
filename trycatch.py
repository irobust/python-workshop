def key_error():
    dict1 = dict(a=10, b=20)
    list1 = [1,2,3,4]
    try:
        print(dict1['a'])
        print(list1[4])
    except IndexError:
        print("List1 doesn't has this index")
    except KeyError:
        print("Dict1 doesn't have this key")
    except:
        print("Generic error message")
    finally:
        print('Keep running program!')

def value_error():
    try:
        a = int(input("Please input number: "))
    except ValueError:
        a = 0
        print('Invalid input, please input [0-9].')

def main():
    value_error()

if __name__ == "__main__":
    main()
