# HL7 v2 Message Guide

## Message Type

This project will use an HL7 v2.5.1 ORU^R01 message.

ORU messages are commonly used to communicate observation results such as laboratory results.

## Segments

### MSH
Message Header. Contains information about the message itself, such as the message type, message ID, and HL7 version.

### PID
Patient Identification. Contains patient demographic information such as patient ID, name, date of birth, and sex.

### OBR
Observation Request. Contains information about the laboratory order or test panel.

### OBX
Observation Result. Contains an individual laboratory result such as the test name, result value, unit, reference range, and result status.
