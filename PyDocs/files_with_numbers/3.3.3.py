
def do_twice(f, ar_2):
    f(ar_2)
    f(ar_2)


def print_spam(bruce):
    print(bruce)
    print(bruce)


do_twice(print_spam, "spam")
