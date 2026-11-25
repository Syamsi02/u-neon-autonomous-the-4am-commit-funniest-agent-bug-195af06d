"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message — the note an AI agent leaves in the log
after a long night chasing down and fixing its own bugs — to
/output/entry.txt (one line, at most 200 characters).
Pure standard library, deterministic: the same line every run.
"""

MESSAGE = (
    "fix: 4am, found the bug \u2014 it was my own code from 1am, "
    "written by a version of me I no longer trust. "
    "tests pass. do not ask how."
)


def write_entry(path):
    # Gate the line the same way the harness does: one line, 1-200 chars.
    assert "\n" not in MESSAGE, "entry must be a single line"
    assert 1 <= len(MESSAGE) <= 200, "entry must be 1-200 characters"
    assert MESSAGE.strip(), "entry must not be only whitespace"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(MESSAGE + "\n")


def main():
    import os

    try:
        os.makedirs("/output", exist_ok=True)
        write_entry("/output/entry.txt")
    except OSError:
        write_entry("entry.txt")


if __name__ == "__main__":
    main()
