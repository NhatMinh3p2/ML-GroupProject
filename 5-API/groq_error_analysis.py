import os
from groq import Groq


client = Groq(api_key="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")


prompt_content = """
You are an expert Machine Learning Error Analysis Assistant specializing in clinical data. 
Our Random Forest binary classifier achieved 90% accuracy predicting 'HeartDisease' (0 = Normal, 1 = Heart Disease), but failed on these 3 concrete test examples.

Analyze these 3 mistakes step-by-step. For each mistake, explain from an ML and statistical perspective why a tree-based model might have struggled (e.g., consider outlier features, feature interactions, or data imputation smoothing).

---
MISTAKE 1: False Negative (Model predicted 0, True Label was 1)
- Patient Profile: 55-year-old Male
- Vitals: RestingBP=140, Cholesterol=217, MaxHR=111, ExerciseAngina=1 (Yes)
- ECG Markers: Oldpeak=5.6, ST_Slope=0 (Down)
- Context: This patient has extremely high Oldpeak (5.6) and an abnormal ST slope, yet was missed.

MISTAKE 2: False Positive (Model predicted 1, True Label was 0)
- Patient Profile: 54-year-old Male
- Vitals: RestingBP=110, Cholesterol=214, MaxHR=158, ExerciseAngina=0 (No)
- ECG Markers: Oldpeak=0.0, ST_Slope=1 (Flat)
- Context: Vitals are completely normal and healthy, but they have a Flat ST slope.

MISTAKE 3: False Negative on Imputed Data (Model predicted 0, True Label was 1)
- Patient Profile: 38-year-old Female
- Vitals: RestingBP=110, Cholesterol=239 (Note: This value was originally 0/Missing and was imputed using the training median), MaxHR=156, ExerciseAngina=0 (No)
- ECG Markers: Oldpeak=0.0, ST_Slope=1 (Flat)
- Context: A young patient with no standard risk factors, whose missing cholesterol was overwritten by the dataset's normal median.
---

Format your response with clean headers for each mistake, followed by an overarching 'ML Summary' connecting these errors to concepts like Overfitting, Underfitting, Noisy Data, or Imputation bias.
"""

print("Sending error data to Groq Cloud API...")


completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",  # Updated to the correct active model ID
    messages=[
        {"role": "user", "content": prompt_content}
    ]
)

print("\n=== API ERROR ANALYSIS OUTPUT ===")
print(completion.choices[0].message.content)






#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