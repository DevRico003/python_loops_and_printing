#!/bin/python3

def from_to_by(start, end, step):
    if step == 0:
        raise ValueError("Step cannot be zero")

    if step > 0 and end < start:
        raise ValueError("End should be greater than start for positive step")
    elif step < 0 and end > start:
        raise ValueError("End should be less than start for negative step")
    
    for i in range(start, end + (1 if step > 0 else -1), step):
        print(i)

def one_to_ten():
    from_to_by(1, 10, 1)

def evens_to_twenty():
    from_to_by(2, 20, 2)

def from_to(start, end):
    step = 1 if start <= end else -1
    from_to_by(start, end, step)

if __name__ == "__main__":
    print("Output of one_to_ten:")
    one_to_ten()

    print("\nOutput of evens_to_twenty:")
    evens_to_twenty()

    print("\nOutput of from_to with arguments 6, 11:")
    from_to(6, 11)

    print("\nOutput of from_to with arguments 11, 6:")
    from_to(11, 6)

    print("\nOutput of from_to_by with arguments 1, 10, 3:")
    from_to_by(1, 10, 3)

    print("\nOutput of from_to_by with arguments 10, 1, -3:")
    from_to_by(10, 1, -3)

    print("\nOutput of from_to_by with arguments 1, 10, -1:")
    try:
        from_to_by(1, 10, -1)
    except ValueError as e:
        print(e)

    print("\nOutput of from_to_by with arguments 10, 1, 1:")
    try:
        from_to_by(10, 1, 1)
    except ValueError as e:
        print(e)

    print("\nOutput of from_to_by with arguments 1, 10, 0:")
    try:
        from_to_by(1, 10, 0)
    except ValueError as e:
        print(e)
