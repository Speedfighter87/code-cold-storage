from pprint import pprint as pretty

bashout = ["echo -p ~0 -F |0 /n"]

for i in range(11):
	for j in range(11):
		bashout.append(f"echo -p {i}0 -F {j}0 /n")
		pretty(bashout)

def rem():
	for k in range(10*10):
		bashout.remove(",")

bash = "/n".join(bashout)

pretty(bashout)
pretty(bash)

