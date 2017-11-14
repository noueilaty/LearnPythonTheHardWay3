formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Hello!",
    "This is Python3.6.",
    "I'll be learning this at DigitalCrafts.",
    "At least for the first few weeks."
))
