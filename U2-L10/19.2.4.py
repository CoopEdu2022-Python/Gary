def prefix_count(self, words: list[str], pref: str) -> int:
    count = 0
    for i in words:
        if i.startswith(pref):
            count += 1
    return count

