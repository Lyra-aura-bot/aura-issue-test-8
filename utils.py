import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("a", type=int, help="first operand")
    parser.add_argument("b", type=int, help="second operand")
    parser.add_argument(
        "-o", "--op",
        choices=["add", "sub", "mul", "div"],
        default="add",
        help="operation to perform"
    )
    return parser.parse_args()