#Jordan Hosler-Watson, Period 8, 9/30/25
print("Task 1")
name = input("What is your first and last name(put a space inbetween)\n")
space = name.find(" ")
first_name = name[0:space]
print(first_name.title())
last_name = name[(space + 1):]
print(last_name.title())
format_fn =  first_name[0].lower() + first_name[1:].upper()
format_ln =  last_name[0].lower() + last_name[1:].upper()
print(format_fn,format_ln)

print("Task 2")
sw_phrase = "Once you start down the dark path, forever will it dominate your destiny."

enc_phrase = sw_phrase.upper().replace('A', '1').replace('A', '2').replace('A', '3').replace('A', '4').replace('A', '5')

print(enc_phrase)

print("Task 3")
phrase_length = (len(sw_phrase))
phrase_cut = phrase_length//3
phrase_one = sw_phrase[0:phrase_cut]
phrase_two = sw_phrase[phrase_cut: phrase_cut * 2]
phrase_three = sw_phrase[phrase_cut* 2:]
print(phrase_two,phrase_one,phrase_three)

print("Task 4")
digit = input("Please input a 5 digit code ")
digit_cut = (len(digit))//5
digit_sp1 = digit_cut
digit_sp2 = digit_cut+1
digit_sp3 = digit_cut+2
digit_sp4 = digit_cut+3
digit_sp5 = digit_cut+4
print(digit_sp1 + digit_sp2 + digit_sp3 + digit_sp4 + digit_sp5)

print("Task 5")
another_swphrase = "Why, you stuck-up half-witted scruffy-looking nerf herder"
print(another_swphrase[::2])
print(another_swphrase[::-2])

print("Task 6")

from datetime import date


today = date.today()

today = today.strftime("%Y,%B,%d")


print(f"The date today is {today}")
date_parts = today.split(',')
year = date_parts [0]
month = date_parts [1]
day = date_parts[2]
print(f"Currently it is the year {year}, and the day is {day}, of {month}")