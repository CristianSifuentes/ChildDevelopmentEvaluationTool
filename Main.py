# Main.py
from Evaluation import CognitiveDevelopment, SocialDevelopment, EmotionalDevelopment, PhysicalDevelopment
from DevelopmentReport import DevelopmentReport
from DataHandler import DataHandler
from Decorators import validate_score, measure_time

@validate_score
@measure_time
def create_evaluation(area, score):
    if area == "cognitive":
        return CognitiveDevelopment("Cognitive", score)
    elif area == "social":
        return SocialDevelopment("Social", score)
    elif area == "emotional":
        return EmotionalDevelopment("Emotional", score)
    elif area == "physical":
        return PhysicalDevelopment("Physical", score)

def main():
    evaluations = []

    print("Welcome to the Child Development Evaluation Tool")
    areas = ["cognitive", "social", "emotional", "physical"]
    for area in areas:
        score = int(input(f"Enter the score for the {area} development area (0-100): "))
        evaluation = create_evaluation(area, score)
        evaluations.append(evaluation)

    report = DevelopmentReport(evaluations)
    
    with DataHandler("development_report.txt") as file:
        for result in report.generate_report():
            print(result)
            file.write(result + "\n")
        
        summary = report.summary()
        print(summary)
        file.write(summary + "\n")

if __name__ == "__main__":
    main()
