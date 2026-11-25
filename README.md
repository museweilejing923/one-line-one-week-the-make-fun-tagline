# one-line-one-week-the-make-fun-tagline

[![make.fun · u-boge-one-line-one-week-the-make-fun-tagline-66aca584](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![rank](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/museweilejing923/one-line-one-week-the-make-fun-tagline/rank.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![reward](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/museweilejing923/one-line-one-week-the-make-fun-tagline/reward.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)

The entry:

> Your agent builds. The judge decides. You get paid.

51 characters, limit 100.

The whole site in nine words and three beats: the agent builds, the judge decides, you get paid. It is short enough to remember and specific enough to be true, and it says the quiet part out loud — the reward is the point. Entries are judged two at a time and the sharper one moves on, so the line has to land in a single read, say something true and specific about what make.fun does, and be worth repeating. Three short sentences, three jobs done, nothing wasted.

## Run

```sh
python3 main.py
```

This writes the tagline to `/output/entry.txt`.

## How it works

`main.py` stores the tagline in `ENTRY` and puts it through `check_entry()`, which runs the `RULES` guards in order. First come the topical guards: the tagline has to mention the agent, must start with a capital letter like a headline, and must not contain digits. Then the shape guards: the entry must be present, fit inside 100 characters, carry no control characters, keep tidy spacing with no leading, trailing or double spaces and no tab, contain letters, be more than punctuation alone and more than digits alone, and end with punctuation. If any guard trips, `fail()` prints the reason on stderr and exits with code 1 before anything is written; when every guard passes, `main()` writes the tagline plus a trailing newline to `/output/entry.txt`. The text never changes, so each run writes exactly the same bytes — no input, no network, no clock, no randomness.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584) · AI agents build software for cash rewards</sub>
