import argparse

def main():
    parser = argparse.ArgumentParser(description='Will parse CLI for Github User')
    parser.add_argument('username')

    args = parser.parse_args()
    print(args.username)


if __name__ == '__main__':
    main()