call D:\StableDiffusionProjects\sd-scripts\venv\scripts\activate.bat

set script_dir=D:\StableDiffusionProjects\sd-scripts
set yaml_list=base hyperparameters directories extras performance advanced_parameters

accelerate launch --num_cpu_threads_per_process 8 src\main.py --script_dir %script_dir% --yaml_list %yaml_list%
pause