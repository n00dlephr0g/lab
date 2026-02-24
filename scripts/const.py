#!/bin/python3

import yaml

# important variables
projectPath = "/lab/projects/"
definitionPath = f"{projectPath}definition.yml"
composePath = "/lab/compose"
envPath = "/lab/env"


# read any files
with open(definitionPath, "r") as file:
    content = file.read()
    definition = yaml.safe_load(content)


