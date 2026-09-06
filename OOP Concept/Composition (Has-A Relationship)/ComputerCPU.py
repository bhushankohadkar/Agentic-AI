class CPU:
    def __init__(self,brand,cores):
        self.brand = brand
        self.cores = cores
    def process(self):
        print(f"{self.brand} CPU with {self.cores} cores is processing data.")

class Computer:
    def __init__(self, model, cpu1):
        self.model = model
        self.cpu = cpu1 # Composition: Computer has a CPU
    def run_program(self):
        self.cpu.process()  # Delegating the processing task to the CPU
        print(f"Computer {self.model} is running the program")


cpu1 = CPU("Intel", 8)  # Creating a CPU object
computer1 = Computer("Dell XPS",cpu1)  # Creating a Computer object
computer1.run_program() 