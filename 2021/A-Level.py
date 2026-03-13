# coced by Zenet

def harshad_num():
    n = int(input("Enter the nth harshad number you want to see: "))
    harshads = []

    final_harshad = 0
    iter_ = 1

    while len(harshads) != n:

        if iter_ % sum([int(iter_) for iter_ in str(iter_)]) == 0:

            final_harshad = iter_
            harshads.append(iter_)
        iter_ += 1

    print(f"based on the {n}th harshad we get: {final_harshad}") if n != 1 else (
        print(f"based on the {n}st harshad we get: {final_harshad}"))

harshad_num()
