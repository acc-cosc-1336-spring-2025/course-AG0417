import decisions

print("What are the options")
options = input()
options = int(options)

print("What is the total")
total = input()
total = int(total)
result = decisions.get_options_ratio(options, total)

print(result)
