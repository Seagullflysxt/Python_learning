#3_9
invite = ['Steve Jobs','Bill Gates','Tim cook']
print(f"Hello,{invite[0]},{invite[1].title()},{invite[2]},would you like to have dinner with me?")
print(f"Sorry,{invite[2]} is busy tonight,so he can't catch up our appointment.")
invite[2] = 'senggi'
print(f"Hello,{invite[0]},{invite[1]},{invite[2]},would you like to have dinner with me?")
print(f"I invite {len(invite)} guests.")
