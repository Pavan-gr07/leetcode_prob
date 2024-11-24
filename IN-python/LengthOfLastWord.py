def lenWord(str):
    words = str.strip().split()
    

    return len(words[-1]) if words else 0


lenWord("  Hello world   ")
