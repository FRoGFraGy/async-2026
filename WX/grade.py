import sys
def evaluate_grade(score):
    if score >= 80:
        return "Excellent"
    elif score >= 50 and score < 80:
        return "Good"
    else:
        return "Fail"

def main():
    test_score = int(input("Enter the test score (0-100): "))
    result = evaluate_grade(test_score)
    print(f"Score: {test_score} -> Grade: {result}")

if __name__ == "__main__":
    main()