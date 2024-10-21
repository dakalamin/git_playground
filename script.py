import random

def main() -> None:
    rb = random.randbytes(16)
    print(''.join(f'{b:02x}' for b in rb))

if __name__ == '__main__':
    main()
