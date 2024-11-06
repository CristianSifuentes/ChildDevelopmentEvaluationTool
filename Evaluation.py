class DevelopmentArea:
    def __init__(self, name, score):
        self.name = name
        self.score = score # Evaluation score on a scale, e.g., 0-100

    def evaluate(self):
        raise NotImplementedError("You must implement the evaluate method in the subclass.")

    
    def __str__(self):
         return f"{self.name}: {self.score}/100"

class CognitiveDevelopment(DevelopmentArea):
    
    def evaluate(self):
        # Evaluation based on cognitive questions or tests
        return f"Social Evaluation: {self.score}/100"

class SocialDevelopment(DevelopmentArea):
    pass


class EmotionalDevelopment(DevelopmentArea):
    pass

class PhysicalDevelopment(DevelopmentArea):
    pass