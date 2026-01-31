class Elem:
    def __init__(self, val):
        self.val = val
        self.name = f"{val}"

    # You only need to implement one of them
    # The others can be derived
    def __lt__(self, a):
        # evens < odds
        # put evens at the front
        return (self.val % 2) < (a.val % 2)

    def __repr__(self):
        return f"{self.val}"


def main():
    elems = []
    for i in range(10, -1, -1):
        elems.append(Elem(i))
    
    print(elems)

    elems.sort()
    print(elems)

main()