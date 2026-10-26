# Code Review

## Initial Review

1. **Bad names.** do_math_stuff, do_string_stuff, x, list1 don't tell you anything. You have to read the whole thing to know what it does.

2. **No documentation.** No docstrings or comments, and there's a random 5 in the string function with no explanation.

3. **Longer loops than needed.** Both functions build results one item at a time, and the string one adds extra spaces just to strip them off at the end.

## Final Review

I fixed all three. The names are clear now, every function has a docstring, and the code is shorter and easier to follow. I ran it after and the output matched the original exactly.

1. **Names:** Renamed things to process_numbers, process_strings, numbers, words, etc. I reread the code to make sure each name made sense on its own.

2. **Documentation:** Added PEP 257 docstrings to every function and turned the 5 into a constant called LONG_WORD_LENGTH. Only added comments where something wasn't obvious.

3. **Loops:** Swapped both loops for list comprehensions and used " ".join() so I didn't need strip() anymore. Ran it to confirm the output didn't change.