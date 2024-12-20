#!/bin/bash

# Activate the virtual environment
source /path/to/your/virtual/environment/bin/activate

# Set script directory and YAML list variables
script_dir="/path/to/your/StableDiffusionProjects/sd-scripts"
yaml_list=("base" "hyperparameters" "directories" "extras" "performance", "advanced_parameters")

# Launch the accelerate script with specified parameters
accelerate launch --num_cpu_threads_per_process 8 src/main.py --script_dir "$script_dir" --yaml_list "${yaml_list[@]}"

# Pause the script (if needed, usually not required in bash)
read -p "Press [Enter] key to continue..."
