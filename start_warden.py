from interoperability.warden.warden import Warden

def main():
    try:
        Warden()
    except Exception as ex:
        print('Caught this error: ' + repr(ex))
        print('Error has occured on warden thread, instance is stopping....')

if __name__ == "__main__":
    main()