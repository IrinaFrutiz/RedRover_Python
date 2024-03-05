def which_family_are_bigger(family1, family2):
    if len(family1) == len(family2):
        return "Equal"
    else:
        return f"Family {1 if len(family1) > len(family2) else 2}"


print(which_family_are_bigger(input("First family members: ").split(), input("Second family members: ").split()))
