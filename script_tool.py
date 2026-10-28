#!/usr/bin/env python3
"""VideoScript-Tool — topic/script to video plan (text output only, no rendering)."""
import argparse
def main():
    p = argparse.ArgumentParser(); p.add_argument("--topic", required=True); p.add_argument("--notes", default="")
    a = p.parse_args()
    print(f"# Video plan: {a.topic}\n")
    print(f"Notes: {a.notes or 'none'}\n")
    print("## Narration script")
    print(f"Hello, and welcome. Today we talk about {a.topic}, in simple words, with a clear example you can use today.\n")
    print("## Captions")
    print(f"- {a.topic}\n- Simple explanation\n- One practical example\n- Call to action: try it and share your result\n")
    print("## Scenes")
    print("1. Hook (0:00) — state the problem in one line.\n2. Explanation (0:20) — explain the idea simply.\n3. Example (1:00) — show one real example.\n4. Close (1:40) — recap + call to action.\n")
    print("## Background-music cues")
    print("- Intro: light, upbeat, low volume under narration.\n- Example: music dips, narration clear.\n- Close: music rises slightly, then fades out.")
if __name__ == "__main__": main()
