# HL7 v2 Laboratory Result to FHIR R4 Converter

A Python learning project that converts simplified HL7 v2 laboratory result messages into FHIR R4 resources.

## Project Overview

The purpose of this project is to build a Python program that converts a simplified HL7 v2 laboratory result message into FHIR R4 resources.

The project will explore two healthcare interoperability approaches: HL7 v2 messaging and HL7 FHIR.

## The Problem

Healthcare organizations often use multiple clinical, laboratory, and administrative systems that need to exchange patient information.

HL7 v2 remains widely used for sending laboratory results between systems, while FHIR provides a modern resource-based format commonly used by healthcare applications and APIs. This project explores how laboratory information can be transformed between these formats.

## Intended Users

This educational project may be useful for:

* Health informatics students
* Laboratory professionals learning interoperability
* Healthcare software developers
* Healthcare interface and integration analysts
* Technical support professionals working with clinical systems

## Version 1 Scope

Version 1 will support:

* One synthetic HL7 v2.5.1 `ORU^R01` message
* One fictional patient
* One laboratory order or panel
* Multiple numerical laboratory results
* FHIR R4 JSON output
* The `MSH`, `PID`, `OBR`, and `OBX` segments

## Input

The program will read a synthetic HL7 v2.5.1 laboratory result message stored in a text file.

Version 1 will not connect directly to laboratory instruments, laboratory information systems, electronic health records, or radiology systems.

## Output

The program will generate a FHIR R4 JSON Bundle containing:

* One `Patient` resource
* One or more `Observation` resources
* One `DiagnosticReport` resource

The `DiagnosticReport` will reference the laboratory `Observation` resources generated from the HL7 v2 message.

## Learning Objectives

The learning objectives of this project are to:

* Understand the basic structure of HL7 v2 messages
* Understand FHIR R4 resources and references
* Practise Python file handling
* Parse structured text using Python
* Work with dictionaries and JSON
* Validate healthcare data
* Write automated tests
* Learn Git and GitHub workflows
* Document technical decisions clearly

## Current Limitations

This project uses only synthetic and fictional patient data.

It supports a small and controlled subset of HL7 v2.5.1 and FHIR R4. It is an educational prototype and is not designed for production healthcare environments.

The program must not be used for clinical decision-making, patient care, or the processing of real patient information.

## Project Status

The project is currently in the planning and documentation stage.

I am developing it with minimal AI-assisted coding to strengthen my Python programming skills and improve my understanding of healthcare interoperability standards.
