import os
import random
import deap
from deap import base, creator, tools
def pad_file(file_path, z):
    with open(file_path, 'ab') as file:
        random_content = os.urandom(z)
        file.write(random_content)

def create_new_section(file_path, section_name, section_content):
    with open(file_path, 'ab') as file:
        section_header = section_name.ljust(8, b'\x00') 
        file.write(section_header + section_content)

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)

def optimize_content_with_genetic_algorithm(file_path, z, generations, population_size):
    def evaluate(individual):
        padding_size = int(''.join(map(str, individual), 2))
        pad_file(file_path, padding_size)
        return (padding_size,)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, z.bit_length())
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    population = toolbox.population(n=population_size)
    algorithms.eaMuPlusLambda(population, toolbox, mu=population_size, lambda_=population_size, cxpb=0.7, mutpb=0.2, ngen=generations, stats=None, halloffame=None)

def apply_padding_attack_to_benign_files(benign_files_directory, initial_padding_size):
    for file_name in os.listdir(benign_files_directory):
        file_path = os.path.join(benign_files_directory, file_name)
        pad_file(file_path, initial_padding_size)
        print(f"Applied padding to {file_name}")
benign_files_directory = r'C:\Users\vikas\PycharmProjects\BODMAS\evasion-attacks-against-ml-based-malware-detectors\data\benign_examples'
initial_padding_size = 512  

apply_padding_attack_to_benign_files(benign_files_directory, initial_padding_size)
print("Padding/append attacks applied to all benign files")


