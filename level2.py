def get_index(haystack, needle):
    if needle in haystack:
        return(haystack.index(needle))
    else:
        return(-1)

if __name__ == '__main__':
    haystack = "play"
    needle = "la"
    index = get_index(haystack, needle)
    print(index)
