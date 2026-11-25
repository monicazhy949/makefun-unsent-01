"""Unsent: The Micro-Confession Sprint — makefun-unsent-01."""

ENTRY = "Daniel, my best friend since third grade — you married Emily on June 14th, and I still have the 214-word toast I wrote for your wedding in my notes, the one where I tell everyone I loved you first."


def main():
    print(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
