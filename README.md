# regexbased-chronoparser

A small Python date/time parser that reads a phrase like "today 2 hrs before 5:30pm" and prints the resulting time, date and weekday. It uses only the standard library (`re` and `datetime`).

**Status:** work in progress. This is a learning project, and it has known bugs (see below).

## What it understands

| Input pattern | Meaning |
|---|---|
| today <time> | the time today |
| N hr/hrs/hour/hours before <time> | the time minus N hours |
| N hr/hrs/hour/hours after <time> | the time plus N hours |
| after <time> | the time on the next day |
| before <time> | the time on the previous day |

Times are written as H:MM followed by am or pm (for example "5:30pm"). If neither am nor pm is present, pm is assumed.

## Known issues

- Crashes with `UnboundLocalError` if the input has no "today" or no H:MM time (for example "hello" or "after 5:30pm"), because `timegrp` is only set inside the first `if`.
- Only `:` is accepted as the time separator, so "12.00" is not recognised.
- No hour wraparound: 11:30 pm with "2 hrs after" prints 13 : 30 pm, and 1:30 am with "2 hrs before" prints -1 : 30 am.
- Minutes lose their zero padding in the "hrs before/after" branches (2:00 prints as 2 : 0).
- Matching is case-sensitive ("AM", "Today" and "HRS" are not recognised), and "5:30 AM" is treated as pm.
- No input validation: impossible times such as 25:99 and unexpected characters are not rejected.
- Only hours are supported as an offset (no minutes or days), and the offset must come directly before "before"/"after" and the time.
- The four near-identical regex checks in each branch should be collapsed into one.

## Ideas for later

- Support "tomorrow" / "yesterday", minutes and days as offsets, and 24-hour times.
- Return a `datetime` object instead of printing, so the parser can be tested and reused.
- Add a test file with input and expected-output pairs.

## Notes

Written as a first-year student project. I used Claude to help debug some of the regex errors while building it.
