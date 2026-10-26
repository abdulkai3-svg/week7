# Design Decisions

I renamed everything because the original names made me read every line just to figure out what was happening. Now you can tell what each function does from its name. I also made the 5 into a constant so it's clear what it's for and easy to change later.

I used list comprehensions since the loops were just building a list with an if/else, and a comprehension does that in one line. For the strings I used join() instead of adding spaces and stripping them, because that's the normal way to do it in Python and it's less messy.

These changes make it easier for someone else to update the code without having to figure out the whole thing first. 