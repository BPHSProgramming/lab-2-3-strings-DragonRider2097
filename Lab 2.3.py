#Jordan Hosler-Watson, Period 8, 9/30/25
print("Task 1")
name = input("What is your first and last name(put a space inbetween)\n")
print(len(name))
space = name.find(" ")
first_name = name[0:space]
print(first_name.title())
last_name = name[(space + 1):]
print(last_name.title())

print("Task 2")
sw_phrase = "Once you start down the dark path, forever will it dominate your destiny."

enc_phrase = sw_phrase.upper().replace('A', '1').replace('A', '2').replace('A', '3').replace('A', '4').replace('A', '5')

print(enc_phrase)

print("Task 3")
phrase_length = (len(sw_phrase))
print(phrase_length)
phrase_one = sw_phrase[0:sw_phrase/3]
#phrase_two = sw_phrase[]
#phrase_three = sw_phrase[]
print()

print("Task 4")

print("Task 5")

print("Task 6")