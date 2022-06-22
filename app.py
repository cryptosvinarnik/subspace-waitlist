from subspace import join_waitlist


with open(input("File with emails: ")) as file:
    emails = file.read().strip().split()

if __name__ == "__main__":
    r = join_waitlist(emails)

    print(
        "Quantity:", len(list(filter(lambda a: a == 200, list(r))))
    )
