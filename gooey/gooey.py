# THIS IS THE EXECUTABLE MODULE FILE
	
def option(label, lstyle, text, tstyle):
	output_form = []
	output = ""
	data = {1:"()", 2:"[]", 3:"<>", 4:"{}", 5:"--", 6:"••"}
	#conditioning
	label = str(label)
	text = str(text)
	label_txt = []
	text_txt = []
	prelabel = ""
	pretext = ""
  #label
	if lstyle == 0:
		output_form.append(label)
	else:
		prelabel = data[int(lstyle)]
		label_txt.append(prelabel[0])
		label_txt.append(label)
		prelabel = data[int(lstyle)]
		label_txt.append(prelabel[1])
		" ".join(label_txt)
		output_form.append(label_txt)
  #text
	if tstyle == 0:
		output_form.append(text)
	else:
		pretext = data[int(tstyle)]
		text_txt.append(pretext[0])
		text_txt.append(text)
		text = data[int(tstyle)]
		text_txt.append(pretext[1])
		" ".join(text_txt)
		output_form.append(text_txt)
	" ".join(output_form)
	output = output_form
	return output
#commands