import output

bullshit_words = {"agile", "modular", "blockchain", "crypto", "bitcoin", "tesla", "ai", "influencer"}
good_words = {"coke", "mate", "hackathon", "hackspace", "hacker", "python", "marta"}
bad_words = {"beer", "wine", "party", "marketing", "ads", "advertisment", "sun", "birds", "daylight", "javascript", "php"}

state_machine = [
	[[0,0,0], [1,0,0], [1,1,0], [1,1,1]],
	[[0,1,0], [1,1,0], [2,1,0], [2,1,1]],
	[[1,1,0], [2,1,1], [2,2,1], [3,2,1]],
] # 1st val -> led; 2nd val -> arm, 3rd val -> puke

state = [0,0] # Current position in the state_machine matrix

bullshit_cnt = 0 
bad_cnt = 0
good_cnt = 0

bullshit_step = 1
bad_step = 1
good_step = 1

arm_mod = 0
led_mod = 0

keyword_dict = dict()
for w in bullshit_words:
	keyword_dict[w] = "bullshit"
for w in good_words:
	keyword_dict[w] = "good"
for w in bad_words:
	keyword_dict[w] = "bad"

def keyword_found(kw):
	global bullshit_cnt, good_cnt, bad_cnt
	if kw in bullshit_words:
		bullshit_cnt += 1 
		if bullshit_cnt == bullshit_step:
			bullshit_cnt = 0
			if state[0] < 2:
				state[0]+=1
			#else output.scream_bullshit()
	if kw in good_words:
		good_cnt += 1
		if good_cnt == good_step:
			good_cnt = 0
			if state[1] > 0:
				state[1]-=1
			#else output.scream_bullshit()
	if kw in bad_words:
		bad_cnt +=1 
		if bad_cnt == bad_step:
			bad_cnt = 0
			if state[1] < 2:
				state[1]+=1	
			#else output.scream_bullshit()
	process_state()
	
def process_state():
	print("Settings state...")
	output.set_led(state_machine[state[0]][state[1]][0]+led_mod)
	output.set_arm(state_machine[state[0]][state[1]][1]+arm_mod)
	output.set_puke(state_machine[state[0]][state[1]][2])
	print("")

def trigger_time():
	global state
	if state[0] > 0: 
		state[0] -= 1
	print("State[0] = " + str(state[0]))
	process_state()
  
def light_turned_on():
	arm_mod = 1	
	process_state()

def light_turned_off():
	arm_mod = 0
	process_state()

def sound_loud():
	led_mod = 1
	process_state()

def sound_quiet():
	led_mod = 0
	process_state()

def process_sound(volume):
	pass
