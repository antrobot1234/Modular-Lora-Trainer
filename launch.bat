call D:\StableDiffusionProjects\sd-scripts\venv\scripts\activate.bat

set yaml_list=base hyperparameters directories extras performance advanced_parameters

accelerate launch --num_cpu_threads_per_process 8 src\main.py --yaml_list %yaml_list%
pause