with open("samples/input/valid_basic_oru.hl7","r") as file:
    content = file.read()
    segments = content.split("\n")
    separated = []
    segment_names = []
    for i in segments:
        if "|" in i:
            separated.append(i.split("|"))
    for j in separated:
        segment_names.append(j[0])
    for x in separated:
        if x[0] == "PID":
            print(x)
