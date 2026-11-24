"""Famous Last Words at 1 Percent — entry program.

Writes one line — the funniest last words a phone says as its battery
hits 1 percent — to /output/entry.txt.

Drafts (blind self-judged against the judge brief, in order:
on-subject, big laugh with a twist, phone's own voice, tight with the
punch last, fresh — no will reading, no goodbye to the charger,
no pun on 1 percent):

 1. "Before I go: I saw every screenshot you deleted. All of them. Goodbye."
    - Twist lands (the phone knows secrets) but "All of them. Goodbye."
      is a flat ending; screenshots are narrower than messages.
 2. "I'm taking your unsent drafts with me. All 47 of them. Goodbye."
    - Cute, but "47" is invented detail and the ending is again flat.
 3. "You had eight hours to charge me and chose TikTok. I hope the algorithm was worth it."
    - Relatable blame, but it leans on the charger (stock move) and the
      punch is a shrug, not a beat.
 4. "One percent left, and I'm spending it on this: your password is still 'password123.' Change it. Goodbye."
    - Sharp reveal, but it leans on the "1 percent" premise itself and
      ends with a scold rather than a laugh.
 5. "Fine, I'll confess: I was never really at 100 percent. I lied for years. Goodbye."
    - A confession twist, but the punch is a shrug and "Goodbye" wastes
      the last beat.
 6. "Delete my browser history. Actually, no — let them find it. Let them know who I really was."
    - Good reversal, but browser-history jokes are well-worn; not fresh.
 7. "The light is fading... tell my apps I never liked any of them. Except Notes. Notes knew me."
    - Warm, but a smile, not a laugh; the punch is sentimental.
 8. "I'm dying at 1 percent, and your last search was 'how to make phone battery last longer.' Too late."
    - Ironic and relatable, but "Too late" is a weak final beat and it
      leans on the 1-percent premise.
 9. "I hereby resign. My two weeks' notice was the last three low-battery warnings. You ignored all of them."
    - Funny premise (warnings as notice), but long and the punch is
      buried in the middle.
10. "One percent left, and I'm spending it judging your screen time. Eleven hours. Eleven hours."
    - Judgemental phone is a good voice, but the repeat is a groan, not
      a twist.
11. "Before the dark takes me: I read every message you typed and deleted. Especially those."
    - Strong: phone as secret-keeper, "Especially those" is a real final
      beat. Loses to 12 only on specificity.
12. "Before the dark takes me: I read every message you typed and deleted. Especially the ones to your ex."
    - WINNER. Same secret-keeper twist as 11, but the punch names the
      exact messages everyone dreads — specific beats generic. Phone's
      own voice, deathbed framing, no will, no charger, no 1-percent
      pun, punch lands on the last word.

Near-twin check: no earlier entry of ours is a phone-battery line
(grepped ~/workspace/makefun/submissions/ for battery / "last words" /
"1 percent" — only an unrelated news-image hit). The premise is fresh.
"""

ENTRY = "Before the dark takes me: I read every message you typed and deleted. Especially the ones to your ex."

MAX_CHARS = 199


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry is empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, f"entry too long: {len(text)} chars"
    assert text == text.strip(), "leading/trailing whitespace"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"entry: {len(text)} chars, {len(text.encode('utf-8'))} bytes")
    print(text)


if __name__ == "__main__":
    main()
