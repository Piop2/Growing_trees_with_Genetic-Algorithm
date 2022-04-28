from core.ga import GA


class Main:
    def __init__(self):
        self.running = True
        
        self.ga = GA()
    
    def next_gene(self):
        self.ga.selection()
        self.ga.crossover()
        self.ga.mutation()
        self.ga.repalce()

    def update(self):
        return
    
    def run(self):
        while self.running:
            self.next_gene()
            self.update()

Main().run()
