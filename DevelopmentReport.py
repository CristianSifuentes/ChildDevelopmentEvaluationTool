class DevelopmentReport:

    def __init__(self, evaluations):
        self.evaluations = evaluations
        
        
    def generate_report(self):
        for evaluation in self.evaluations:
            yield evaluation.evaluate()

    def summary(self):
        total = sum(e.score for e in self.evaluations)
        average = total / len(self.evaluations)
        return f"Development Summary: Average Score of {average:.2f}/100"
       
