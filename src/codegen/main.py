from .parse.parse import parse_spec
from .pysdk import pysdk


def main() -> None:
    spec_root = parse_spec()
    pysdk.generate(spec_root)


if __name__ == "__main__":
    main()
