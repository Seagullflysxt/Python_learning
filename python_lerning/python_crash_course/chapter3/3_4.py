#3_4&3_5
invite = ['Steve Jobs','Bill Gates','Tim cook']
print(f"Hello,{invite[0]},{invite[1].title()},{invite[2]},would you like to have dinner with me?")
print(f"Sorry,{invite[2]} is busy tonight,so he can't catch up our appointment.")
invite[2] = 'senggi'
print(f"Hello,{invite[0]},{invite[1]},{invite[2]},would you like to have dinner with me?")

#3_6
print("I found a bigger food table!")
invite.insert(0,'Buffet')
invite.insert(2,'Guido Van Rossum')
invite.append('James Goslin')
print(f"Hello,{invite[0]},{invite[1]},{invite[2]},{invite[3]},{invite[4]},{invite[-1]},would you like to have dinner with me?")

#3_7
print("I'm sorry,the new table can not arrive home on time,so I can only invite two guests.")
sorry_1 = invite.pop(0)
print(f"Sorry {sorry_1},I can't invite you this time")
sorry_2 = invite.pop(0)
print(f"Sorry {sorry_2},I can't invite you this time")
sorry_3 = invite.pop(0)
print(f"Sorry {sorry_3},I can't invite you this time")
sorry_4 = invite.pop(0)
print(f"Sorry {sorry_4},I can't invite you this time")
print(f"{invite[0]},{invite[1]},you are still in the watinglist")
del invite[0]
del invite[0]
print(invite)


