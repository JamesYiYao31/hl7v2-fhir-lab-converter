def read_hl7_file(path):
    with open(path,"r") as file:
        return file.read()

def split_message(text):
    segmented_fields = []
    segments = text.splitlines()
    for i in segments:
        if "|" in i:
            segmented_fields.append(i.split("|"))
    return segmented_fields

def find_segment(segments,name):
    for j in segments:
        if j[0] == name:
            return j
    return None

def extract_msh(segments):
    msh_fields = find_segment(segments,"MSH")
    if msh_fields is None:
        return None
    message_type = msh_fields[8].split("^")
    return {
        "Sending Application": msh_fields[2],
        "Sending Facility": msh_fields[3],
        "Receiving Application": msh_fields[4],
        "Receiving Facility" : msh_fields[5],
        "Message Date/Time" : msh_fields[6],
        "Message Type" : message_type[0],
        "Trigger Event" : message_type[1],
        "Message Control ID" : msh_fields[9],
        "Processing ID" : msh_fields[10],
        "HL7 Version" : msh_fields[11]
        }

def extract_pid(segments):
    pid_fields = find_segment(segments,"PID")
    if pid_fields is None:
        return None
    name = pid_fields[5].split("^")
    return {
        "Patient ID": pid_fields[3],
        "Patient First Name": name[1],
        "Patient Last Name": name[0],
        "Date of Birth": pid_fields[7],
        "Sex": pid_fields[8]
        }

def extract_obr(segments):
    obr_fields = find_segment(segments,"OBR")
    if obr_fields is None:
        return None
    panel = obr_fields[4].split("^")
    return {
        "Placer Order Number" : obr_fields[2],
        "Filler Order Number" : obr_fields[3],
        "Panel Code" : panel[0],
        "Panel Name" : panel[1],
        "Observation Date" : obr_fields[7]
        }
    
def extract_obx_results(segments):
    obx_results = []
    for i in segments:
        if i[0] == "OBX":
            analyte = i[3].split("^")
            obx_result = {
                "Data Type" : i[2],
                "Test Symbol" : analyte[0],
                "Test Name" : analyte[1],
                "Test Result" : i[5],
                "Test Unit" : i[6],
                "Test Reference Range": i[7],
                "Abnormal Flag" : i[8],
                "Result Status": i[11]
                }
            obx_results.append(obx_result)
    return obx_results

def parse_hl7_message(text):
    separated = split_message(text)    
    msh_segment = extract_msh(separated)
    pid_segment = extract_pid(separated)
    obr_segment = extract_obr(separated)
    results = extract_obx_results(separated)
    return {
        "Message" : msh_segment,
        "Patient" : pid_segment,
        "Order" : obr_segment,
        "Results" : results
        }
    
if __name__ == "__main__":
    content = read_hl7_file("samples/input/valid_basic_oru.hl7")
    laboratory_message = parse_hl7_message(content)
    print(laboratory_message)
    
