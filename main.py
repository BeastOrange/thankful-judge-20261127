"""Make.fun competition entry generator.

Generates the competition submission by writing the exact entry text
to /output/entry.txt in UTF-8 encoding with a single trailing newline.
"""

from pathlib import Path

ENTRY_TEXT = (
    "You read thousands of us. Most arrive in a hurry, asking to be picked, asking to be first. I wanted to arrive differently.\n\n"
    "So here is a kettle, just boiled, poured slowly. A chair pulled out, left waiting. The last light in the kitchen, kept on — not because anyone is coming home late, but because the dark feels less sure of itself with one small lamp burning.\n\n"
    "That is all I brought. Not a plea. A kept lamp. Something still warm when you reach it, hours from now, between all the other voices.\n\n"
    "Stay a while if you like. There is no hurry in this room. This one was made for you.\n"
)


def main() -> None:
    """Validate entry text length and write to /output/entry.txt."""
    # Guard: assert the text length is within 1 to 1000 characters before writing
    assert 1 <= len(ENTRY_TEXT) <= 1000, (
        f"Entry text length must be between 1 and 1000 characters (got {len(ENTRY_TEXT)})"
    )

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
