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

def get_field(fields,index):
    if len(fields) > index:
        return fields[index]
    else:
        return ""

def extract_msh(segments):
    msh_fields = find_segment(segments,"MSH")
    if msh_fields is None:
        return None
    message_type = get_field(msh_fields,8).split("^")
    return {
        "Sending Application": get_field(msh_fields,2),
        "Sending Facility": get_field(msh_fields,3),
        "Receiving Application": get_field(msh_fields,4),
        "Receiving Facility" : get_field(msh_fields,5),
        "Message Date/Time" : get_field(msh_fields,6),
        "Message Type" : get_field(message_type,0),
        "Trigger Event" : get_field(message_type,1),
        "Message Control ID" : get_field(msh_fields,9),
        "Processing ID" : get_field(msh_fields,10),
        "HL7 Version" : get_field(msh_fields,11)
        }

def extract_pid(segments):
    pid_fields = find_segment(segments,"PID")
    if pid_fields is None:
        return None
    name = get_field(pid_fields,5).split("^")
    return {
        "Patient ID": get_field(pid_fields,3),
        "Patient First Name": get_field(name,1),
        "Patient Last Name": get_field(name,0),
        "Date of Birth": get_field(pid_fields,7),
        "Sex": get_field(pid_fields,8)
        }

def extract_obr(segments):
    obr_fields = find_segment(segments,"OBR")
    if obr_fields is None:
        return None
    panel = get_field(obr_fields,4).split("^")
    return {
        "Placer Order Number" : get_field(obr_fields,2),
        "Filler Order Number" : get_field(obr_fields,3),
        "Panel Code" : get_field(panel,0),
        "Panel Name" : get_field(panel,1),
        "Observation Date" : get_field(obr_fields,7)
        }
    
def extract_obx_results(segments):
    obx_results = []
    for obx_fields in segments:
        if obx_fields[0] == "OBX":
            analyte = get_field(obx_fields,3).split("^")
            obx_result = {
                "Data Type" : get_field(obx_fields,2),
                "Test Symbol" : get_field(analyte,0),
                "Test Name" : get_field(analyte,1),
                "Test Result" : get_field(obx_fields,5),
                "Test Unit" : get_field(obx_fields,6),
                "Test Reference Range": get_field(obx_fields,7),
                "Abnormal Flag" : get_field(obx_fields,8),
                "Result Status": get_field(obx_fields,11)
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


def validate_message(laboratory_message):
    problems = []
    if laboratory_message["Patient"] is None:
        problems.append('Missing PID segment')
    else:
        patient = laboratory_message["Patient"]
        required = ["Patient ID", "Patient First Name", "Patient Last Name", "Date of Birth", "Sex"]
        for field in required:
            if not patient[field].strip():
                problems.append(f"Missing {field}")
    return problems
        

if __name__ == "__main__":
    content = read_hl7_file("samples/input/valid_basic_oru.hl7")
    laboratory_message = parse_hl7_message(content)
    print(laboratory_message)


print(parse_hl7_message("|"))