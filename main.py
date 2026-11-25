from pathlib import Path


def load_entry():
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    return entry_path.read_text(encoding="utf-8").rstrip("\n")


def main():
    print(load_entry())


if __name__ == "__main__":
    main()
