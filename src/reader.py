with open("samples/input/valid_basic_oru.hl7","r") as file:
    content = file.read()
    segments = content.split("\n")
    separated = []
    results = []
    for i in segments:
        if "|" in i:
            separated.append(i.split("|"))
    for k in separated:
        if k[0] == "MSH":
            message_type = k[8].split("^")
            msh_segment = {
                "Sending Application": k[2],
                "Sending Facility": k[3],
                "Receiving Application": k[4],
                "Receiving Facility" : k[5],
                "Message Date/Time" : k[6],
                "Message Type" : message_type[0],
                "Trigger Event" : message_type[1],
                "Message Control ID" : k[9],
                "Processing ID" : k[10],
                "HL7 Version" : k[11]
            }
            
    for x in separated:
        if x[0] == "PID":
            name = x[5].split("^")
            pid_segment = {
                "Patient ID": x[3],
                "Patient First Name": name[1],
                "Patient Last Name": name[0],
                "Date of Birth": x[7],
                "Sex": x[8]
                }
    for y in separated:
        if y[0] == "OBR":
            panel = y[4].split("^")
            obr_segment = {
                "Placer Order Number" : y[2],
                "Filler Order Number" : y[3],
                "Panel Code" : panel[0],
                "Panel Name" : panel[1],
                "Observation Date" : y[7]
            }
    for j in separated:
        if j[0] == "OBX":
            analyte = j[3].split("^")
            obx_segment = {
                "Data Type" : j[2],
                "Test Symbol" : analyte[0],
                "Test Name" : analyte[1],
                "Test Result" : j[5],
                "Test Unit" : j[6],
                "Test Reference Range": j[7],
                "Abnormal Flag" : j[8],
                "Result Status": j[11]
            }
            results.append(obx_segment)
  
laboratory_message = {
    "Message" : msh_segment,
    "Patient" : pid_segment,
    "Order" : obr_segment,
    "Results" : results
}
print(laboratory_message)