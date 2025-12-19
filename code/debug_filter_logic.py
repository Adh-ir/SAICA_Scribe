from analysis.mapper import _post_process_mappings
import logging

# Mock Data
training_plan = [
    {"competency_code": "1a", "competency_name": "Personal Ethics", "_original_index": 0, "behavioral_indicators": "Desc 1a"},
    {"competency_code": "1b", "competency_name": "Business Ethics", "_original_index": 1, "behavioral_indicators": "Desc 1b"},
    {"competency_code": "2a", "competency_name": "Technical One", "_original_index": 2, "behavioral_indicators": "Desc 2a"},
]

# Mock Mappings from LLM
mappings = [
    {"competency_code": "1a", "name": "Personal Ethics", "confidence": 0.45, "reasoning": "Weak match target"}, # Low conf target
    {"competency_code": "1b", "name": "Business Ethics", "confidence": 0.95, "reasoning": "Strong match non-target"}, # High conf non-target
    {"competency_code": "2a", "name": "Technical One", "confidence": 0.85, "reasoning": "High conf non-target"} # High conf non-target
]

print("--- Test 1: Default Mode (No Target) ---")
# Expectation: 1a (45%) excluded. 1b (95%) and 2a (85%) included.
res1 = _post_process_mappings(
    mappings=[m.copy() for m in mappings], 
    training_plan=training_plan, 
    target_competency=None, 
    original_input="Some input"
)
print(f"Result Count: {len(res1)}")
for m in res1:
    print(f" - {m['competency_code']} ({m['confidence']}%)")

print("\n--- Test 2: Target Mode (Target='1a') ---")
# Expectation: ONLY 1a included (force include). 1b and 2a excluded (strict filter).
res2 = _post_process_mappings(
    mappings=[m.copy() for m in mappings], 
    training_plan=training_plan, 
    target_competency="1a", 
    original_input="COMPETENCY: 1a EVIDENCE: ..."
)
print(f"Result Count: {len(res2)}")
for m in res2:
    print(f" - {m['competency_code']} ({m['confidence']}%)")
