es = [
["l'interesse", 21250, 5, 6.5],
["il montante", 3800, 2, 9],
["il montante", 3800, 3, 7.25],
["il montante", 4356.57, 4, 6],
["il montante", 4500, 3, 3],
["il montante", 7600, 7, 5.75]
]

def console():
	for m_o_i, c, t, r in es:
		print(f"Calcola {m_o_i} semplice su un capitale di {c} € maturato in {t} anni al tasso annuo del {r} %")
		s = c*r*t/100
		if m_o_i == "l'interesse":
			print (s)
		else:
			print(c + s)

def input_word_press():
	for m_o_i, c, t, r in es:
		print(f"input(\"Calcola {m_o_i} semplice su un capitale di {c} € maturato in {t} anni al tasso annuo del {r} %", end= " / ")
		s = c*r*t/100
		if m_o_i == "l'interesse":
			print (str(s) + "\");")
		else:
			print(str(c + s) + "\");")

def gw3():
	print("[hoops name=\"gw3\"]<script>")
	for m_o_i, c, t, r in es:
		print(f"input(\"Calcola {m_o_i} semplice su un capitale di {c} € maturato in {t} anni al tasso annuo del {r} %", end= "\",")
		s = c*r*t/100
		if m_o_i == "l'interesse":
			print ("\"" + str(s) + "\",\".\")")
		else:
			print("\"" + str(c + s) + "\",\".\");")
	print("</script>")

def input_text2():
	print("[hoops name=\"input_text2\"]<script>")
	for m_o_i, c, t, r in es:
		print(f"input(\"Calcola {m_o_i} semplice su un capitale di {c} € maturato in {t} anni al tasso annuo del {r} %", end= "\",")
		s = c*r*t/100
		if m_o_i == "l'interesse":
			print ("\"" + str(s).replace(".",",") + "\")")
		else:
			print("\"" + str(c + s).replace(".",",") + "\");")
	print("</script>")
console()
input_text2()
