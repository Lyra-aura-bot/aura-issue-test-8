from utils import parse_args
from operations import compute

def main():
    args = parse_args()
    result = compute(args.a, args.b, args.op)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()