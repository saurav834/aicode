"""
Experiment 6: Expert System (Medical Diagnosis)
Aim: Implement a rule-based Expert System using a knowledge base and inference rules.
"""


def medical_expert_system():
    print("--- Basic Medical Diagnosis Expert System ---")
    print("Answer with 'yes' or 'no':\n")

    fever = input("Do you have a high fever? ").strip().lower() == 'yes'
    cough = input("Do you have a dry cough? ").strip().lower() == 'yes'
    sore_throat = input("Do you have a sore throat? ").strip().lower() == 'yes'
    headache = input("Do you have a severe headache? ").strip().lower() == 'yes'
    body_ache = input("Do you have body/muscle aches? ").strip().lower() == 'yes'

    print("\n--- Diagnosis Result ---")
    if fever and cough and body_ache:
        print("Possible Condition: Viral Flu (Influenza).")
        print("Advice: Rest, stay hydrated, and consult a physician if fever persists.")
    elif sore_throat and cough and not fever:
        print("Possible Condition: Common Cold / Throat Infection.")
        print("Advice: Warm saline gargles and steam inhalation.")
    elif fever and headache and not cough:
        print("Possible Condition: Viral Fever or Migraine with fever.")
        print("Advice: Monitor temperature and visit a doctor for a blood test if needed.")
    else:
        print("Symptoms are mild or inconclusive. Please consult a general physician for an accurate checkup.")


if __name__ == "__main__":
    medical_expert_system()
