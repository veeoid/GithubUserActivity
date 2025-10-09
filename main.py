import argparse
from api_endpoint import getUserData

def main():
    parser = argparse.ArgumentParser(description='Will parse CLI for Github User')
    parser.add_argument('username')

    args = parser.parse_args()
    userdata = getUserData(args.username)

    print(userdata)




if __name__ == '__main__':
    main()