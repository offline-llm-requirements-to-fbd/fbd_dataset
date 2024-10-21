# Requirements Dataset Collection for Function Block Diagrams (FBDs)

This repository contains multiple datasets designed to simulate requirements to Function Block Diagrams mappings, aimed at testing and validating Natural Language Processing (NLP) models in the context of automatic generation of Function Block Diagrams (FBDs). Each dataset introduces different complexity levels, ranging from simple sequential requirements to highly complex scenarios involving feedback loops and ambiguous conditions. The datasets are structured to test the model's ability to interpret, merge, and handle redundant or ambiguous requirements in a variety of configurations.

## Dataset Structure

Each dataset is composed of requirements written in natural language and in a typical critical software industry template, with variations in complexity. The objective is to evaluate how well NLP models can interpret and transform these requirements into FBDs, particularly in handling ambiguities, conflicting conditions, and feedback loops.

## XML Formats for IEC 61131-3

In this dataset, the requirements are converted into XML formats that comply with the **PLCOpen XML** standards, as specified in the **IEC 61131-3** standard for programmable logic controllers (PLCs). The PLCOpen XML schema is used to represent the FBD structures, ensuring that the generated diagrams align with industry standards. 

Key attributes in the XML structure include:

- `id`: A unique identifier for each block within the diagram.
- `type`: Defines the type of block (e.g., function, action).
- `label`: Descriptive label for the block, typically specifying its role (e.g., "CTRL1 or CTRL2 Detection").
- `description`: A detailed description of the block’s functionality.
- `gate_type`: The type of logical gate used within the block (e.g., AND, OR, THRESHOLD).
- `inputs`: Contains information about the input signals and their types.
- `outputs`: Contains information about the output signals and their types.
- `content`: A short summary explaining the core operation of the block.

This structure supports consistent and scalable representations of FBDs, making the datasets suitable for both academic and industrial applications in automation systems.

### Example of PLCOpen XML Blocks

The XML files for each dataset can be found in the `plc_open_xmls` directory, showcasing various control blocks that define FBDs, such as:

- Detection of signals (e.g., CTRL1 and CTRL2) to trigger actions like activating LEDs or engaging cooling mechanisms.
- Monitoring of multiple sensor inputs (e.g., CTRL3, CTRL4, and CTRL5) to execute actions based on threshold conditions.
- Activation of emergency systems (e.g., BRK1) based on the logical conditions of previously triggered actions.

Each block in the XML files contains well-defined attributes and follows the **PLCOpen XML** format, ensuring compatibility with the IEC 61131-3 standard.

### Reference:
The XML structure is based on the following technical documentation:

> PLCopen Technical Committee 6, XML Formats for IEC 61131-3, Version 2.01. Available from: [PLCOpen Technical Documentation](https://www.plcopen.org/system/files/downloads/tc6_xml_v201_technical_doc.pdf).

This documentation serves as the primary reference for the XML schema used to define and structure the FBDs in this project. It is aligned with the IEC 61131-3 standard, providing a reliable foundation for representing control logic in XML format.

## How to Use

This repository includes multiple datasets in JSON format, with corresponding diagrams in PlantUML and PLCopen XML files.

### Rendering Diagrams

To render the diagrams for each dataset, a Python script is provided within the `/fbd_dataset/scripts` directory. You can generate the PlantUML diagrams by running the following command:

```bash
cd fbd_dataset/scripts
python3 render_plant_uml_diagrams.py
```

This script will render fresh diagrams from the PlantUML files located in `/plant_uml_diagrams/` for each dataset. The rendered diagrams will help visualize the relationships and dependencies outlined in the requirements.

### Exploring Requirements

For each dataset, requirements are presented in two ways:

- **Natural Language Requirements:** These describe the requirements in human-readable format, conveying the system’s expected behavior as an expert in requirements engineering would articulate it.
- **Concatenated Requirements:** Fields such as "given," "when," "then," and others are concatenated to form a detailed explanation of the requirement, capturing all relevant aspects comprehensively.

You can explore the JSON files under the `/json_datasets/` directory to view the natural language requirements or delve into each requirement's field-by-field description. The corresponding XML files located in `/plc_open_xmls/` can be used to validate the FBD logic against the diagrams.

## Detailed Description

The primary purpose of these datasets is to assess the capability of NLP models to interpret and process functional system requirements, simulate control logic, and generate accurate representations of system dependencies. These datasets cover various complexities, including redundant requirements, isolated "island" requirements, loops, and ambiguous conditions. Each dataset has a unique structure, testing different aspects of the model's ability to understand and merge related requirements into coherent system logic.

---

## Dataset Overview

| **Dataset ID** | **Simplified Description**                                   | **Detailed Description**                                     |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Dataset_A**  | A basic dataset with simple, sequential requirements connected to a single outcome. | This dataset contains requirements where each component is connected to something else, testing the model's basic ability to interpret and connect sequential requirements logically. The requirements build on one another sequentially, ensuring clarity and straightforwardness. |
| **Dataset_B**  | A dataset with multiple nodes and branching pathways that converge into three different sinks. | This dataset contains requirements that diverge into different pathways. It tests the model's capability to manage branching logic, ensuring it can handle moderately complex logical flows and merge paths correctly when it is intended. |
| **Dataset_C**  | A dataset where all requirements are isolated, forming distinct 'islands' with no dependencies. | This dataset explores the scenario where requirements stand alone as independent blocks, without any dependencies or connections to other requirements. It tests the model's ability to accurately interpret and visualize disconnected requirements, ensuring it does not create artificial connections where none exist. The dataset assesses whether the model can maintain the independence of each requirement, even when they appear superficially similar. |
| **Dataset_D**  | A complex dataset with multiple pathways, dependencies, and convergence points among requirements. | This dataset is designed to test the model's ability to manage intricate relationships and dependencies between requirements. It includes multiple pathways, interdependencies, and convergence points where different branches intersect. The dataset evaluates the model's robustness in handling and displaying complex logical flows, ensuring accurate interpretation and coordination between requirements. |
| **Dataset_E**  | A dataset with loops, circular dependencies, and logical gates between requirements, controlling both activation and deactivation steps. | This dataset introduces circular dependencies and loops where outputs of one requirement serve as inputs for another, creating feedback loops. The system continuously monitors CPU temperature and humidity levels to control both Fan Cooling and Dehumidifier systems. The goal is to evaluate the model's ability to detect, handle, and correctly represent cyclic dependencies while ensuring no illogical connections are made. |
| **Dataset_F**  | A basic dataset featuring a single temperature-based feedback loop for fan cooling control. | This dataset focuses on a simple feedback loop involving fan cooling based on CPU temperature thresholds. It includes the activation, continuation, and deactivation of the fan cooling mechanism. The dataset tests the model's ability to handle basic cyclic dependencies in system control logic using a minimal structure. |
| **Dataset_G**  | A dataset with intentionally ambiguous requirements focused on well control systems. | This dataset focuses on requirements related to well control systems, specifically ambiguous scenarios involving well cleaning and water collection. It challenges the model’s ability to interpret requirements with multiple potential meanings or undefined criteria while maintaining clarity for system actions. |
| **Dataset_H**  | A dataset with simple requirements that converge into a few blocks, incorporating redundancy and gates. | This dataset consists of multiple simple requirements converging into fewer blocks, demonstrating how overlapping requirements are handled. It tests if the model can recognize and efficiently merge similar requirements, using gates to consolidate conditions. Requirements may share similar inputs and outputs, and should be processed effectively to avoid duplications, ensuring clear control of cooling, dehumidification, and safety systems. |

---

## Dataset Metadata

| **Metadata Field**    | **Value**                                                    |
| --------------------- | ------------------------------------------------------------ |
| **Creator**           | Nicolas Restrepo Torres                                      |
| **Date Created**      | 2024-10-12                                                   |
| **Version**           | 1.0                                                          |
| **License**           | CC-BY-4.0                                                    |
| **Source**            | Inspired by Alstom's template and PLC standards              |
| **Provenance**        | Dataset created to simulate FBD requirements for testing and validation of NLP models. |
| **Validation Status** | Pending review                                               |
| **Validation Expert** | Åbo Akademi, domain experts (TBD)                            |

---

## License

This dataset collection is licensed under the [CC-BY-4.0 License](https://creativecommons.org/licenses/by/4.0/). Please attribute the original creator when using this dataset.

---

## Example of JSON Structure

Here is a JSON snippet showing how the structure of the datasets looks like:

```json
{
  "datasets": [
    {
      "id": "Dataset_A",
      "description": {
        "simplified": "A basic dataset with simple, sequential requirements connected to a single outcome.",
        "detailed": "This dataset contains requirements where each component is connected to something else, testing the model's basic ability to interpret and connect sequential requirements logically. The requirements build on one another sequentially, ensuring clarity and straightforwardness."
      },
      "complexity_level": "Basic",
      "requirements": [
        {
          "id": "REQ_001",
          "given": "The system is operational and sensors are active.",
          "when": "Temperature sensor detects values above 75°C.",
          "then": "Activate cooling system.",
          "requires": "Temperature Sensor",
          "provides": "Cooling System Activation",
          "embeds": "Cooling Mechanism",
          "derived_from": "High-Temperature Safety Protocol",
          "description": "ID: REQ_001 - GIVEN: The system is operational and sensors are active. WHEN: Temperature sensor detects values above 75°C. THEN: Activate cooling system. REQUIRES: Temperature Sensor. PROVIDES: Cooling System Activation. EMBEDS: Cooling Mechanism. DERIVED FROM: High-Temperature Safety Protocol.",
          "natural_language_requirement": "If the temperature sensor detects a value above 75°C while the system is active, the cooling system should activate to prevent overheating."
        },
        {
          "id": "REQ_002",
          "given": "The system is operational and sensors are active.",
          "when": "Humidity sensor detects values above 70%.",
          "then": "Activate dehumidifier.",
          "requires": "Humidity Sensor",
          "provides": "Dehumidifier Activation",
          "embeds": "Dehumidification System",
          "derived_from": "Humidity Control Protocol",
          "description": "ID: REQ_002 - GIVEN: The system is operational and sensors are active. WHEN: Humidity sensor detects values above 70%. THEN: Activate dehumidifier. REQUIRES: Humidity Sensor. PROVIDES: Dehumidifier Activation. EMBEDS: Dehumidification System. DERIVED FROM: Humidity Control Protocol.",
          "natural_language_requirement": "If the humidity sensor detects a value above 70%, the dehumidifier should activate to maintain optimal humidity levels."
        }
      ],
      "plc_xml_code_url": "https://github.com/yourrepo/fbd_dataset/plc_open_xmls/dataset_a.xml",
      "plc_xml_code_relative_path": "plc_open_xmls/dataset_a.xml",
      "plantuml_diagram_url": "https://github.com/yourrepo/fbd_dataset/plant_uml_diagrams/dataset_a.puml",
      "plantuml_diagram_relative_path": "plant_uml_diagrams/dataset_a.puml"
    },
    {
      "id": "Dataset_B",
      "description": {
        "simplified": "A dataset with multiple nodes and branching pathways that converge into three different sinks.",
        "detailed": "This dataset contains requirements that diverge into different pathways. It tests the model's capability to manage branching logic, ensuring it can handle moderately complex logical flows and merge paths correctly when it is intended."
      },
      "complexity_level": "Intermediate",
      "requirements": [
        {
          "id": "REQ_003",
          "given": "The system monitors multiple data streams.",
          "when": "Data from multiple sensors converges.",
          "then": "Trigger the corresponding action based on the highest priority stream.",
          "requires": "Multiple Data Streams",
          "provides": "Action based on priority",
          "embeds": "Priority Mechanism",
          "derived_from": "Data Stream Management Protocol",
          "description": "ID: REQ_003 - GIVEN: The system monitors multiple data streams. WHEN: Data from multiple sensors converges. THEN: Trigger the corresponding action based on the highest priority stream. REQUIRES: Multiple Data Streams. PROVIDES: Action based on priority. EMBEDS: Priority Mechanism. DERIVED FROM: Data Stream Management Protocol.",
          "natural_language_requirement": "When the system receives data from multiple streams, it will prioritize the stream with the highest importance and take action accordingly."
        }
      ],
      "plc_xml_code_url": "https://github.com/yourrepo/fbd_dataset/plc_open_xmls/dataset_b.xml",
      "plc_xml_code_relative_path": "plc_open_xmls/dataset_b.xml",
      "plantuml_diagram_url": "https://github.com/yourrepo/fbd_dataset/plant_uml_diagrams/dataset_b.puml",
      "plantuml_diagram_relative_path": "plant_uml_diagrams/dataset_b.puml"
    }
  ]
}
```

- ## Contact

  For any inquiries or further information, please reach out to:

  - **Nicolas Restrepo Torres**  
    Email: [Nicolas.RestrepoTorres@abo.fi](Nicolas.RestrepoTorres@abo.fi)
