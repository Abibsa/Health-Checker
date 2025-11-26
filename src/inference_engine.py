import json
import os

DATA_RULES_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "rules.json")


def load_rules():
    with open(DATA_RULES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def infer(symptoms, metrics=None):
    """
    symptoms: list or set of symptom keys
    metrics: optional dict (e.g., {"bmi_category": "Obesity"})
    returns: list of matched rules with detailed metadata sorted by priority, match percentage, and score
    """
    if isinstance(symptoms, list):
        symptoms = set(symptoms)
    else:
        symptoms = set(symptoms)

    metrics = metrics or {}
    rules = load_rules()
    matches = []

    for r in rules:
        conds = set(r.get("conditions", []))
        bmi_requirement = r.get("bmi_category")
        
        # Calculate partial match
        matched_conditions = conds.intersection(symptoms)
        unmatched_conditions = conds - symptoms
        total_conditions = len(conds)
        matched_count = len(matched_conditions)
        
        # Calculate match percentage
        match_percentage = (matched_count / total_conditions * 100) if total_conditions > 0 else 0
        
        # Check BMI requirement
        bmi_match = True
        bmi_status = "Tidak diperlukan"
        if bmi_requirement:
            user_bmi = metrics.get("bmi_category")
            bmi_match = user_bmi == bmi_requirement
            bmi_status = f"Diperlukan: {bmi_requirement}" + (f" (Sesuai: {user_bmi})" if user_bmi else " (Tidak tersedia)")
        
        # Include rules with at least 60% match or full match
        # Prioritize full matches, but also show partial matches
        min_match_threshold = 0.6  # 60% minimum match (increased from 50%)
        
        # Skip rules with BMI requirement that doesn't match (unless it's emergency)
        if bmi_requirement and not bmi_match and r.get("priority", 1) != 0:
            continue  # Skip non-emergency rules with BMI mismatch
        
        if match_percentage >= (min_match_threshold * 100):
            # Calculate confidence score (combination of match percentage and priority)
            # Base score is match percentage (0-100)
            confidence_score = match_percentage
            
            # Bonus for full match (High confidence)
            if matched_count == total_conditions:
                confidence_score += 50  # Increased bonus for full match
            
            # Priority weighting (integrated into score instead of separate sort key)
            # Priority 0 (Emergency) gets massive bonus to always be top
            if r.get("priority", 1) == 0:
                confidence_score += 1000
            # Priority 1 (High) gets small bonus
            elif r.get("priority", 1) == 1:
                confidence_score += 20
            # Priority 2 (Medium) gets smaller bonus
            elif r.get("priority", 1) == 2:
                confidence_score += 10
            
            # Reduce confidence if BMI doesn't match but is required
            if bmi_requirement and not bmi_match:
                confidence_score -= 20
            
            # Special handling for COVID rules: penalize if missing characteristic symptoms
            if 'covid' in r.get("id", "").lower():
                has_characteristic_symptom = any(sym in matched_conditions for sym in ['loss_of_smell', 'loss_of_taste'])
                if not has_characteristic_symptom and match_percentage < 100:
                    confidence_score -= 40  # Heavy penalty for COVID without characteristic symptoms
            
            # Determine match type
            match_type = "Cocok Sempurna" if matched_count == total_conditions else "Cocok Sebagian"
            
            matches.append(
                {
                    "rule_id": r.get("id"),
                    "conclusion": r.get("conclusion"),
                    "advice": r.get("advice", ""),
                    "priority": r.get("priority", 1),
                    "score": matched_count,
                    "total_conditions": total_conditions,
                    "matched_conditions": list(matched_conditions),
                    "unmatched_conditions": list(unmatched_conditions),
                    "match_percentage": round(match_percentage, 1),
                    "confidence_score": round(confidence_score, 1),
                    "match_type": match_type,
                    "bmi_requirement": bmi_requirement,
                    "bmi_match": bmi_match,
                    "bmi_status": bmi_status,
                }
            )

    # Sort by confidence_score (descending)
    # This allows a perfect match of Priority 2 to beat a partial match of Priority 1
    matches.sort(key=lambda x: -x["confidence_score"])
    
    # Limit to top 5 most relevant results to avoid overwhelming the user
    matches = matches[:5]
    
    # If no matches found, return top partial matches anyway (at least 30% match)
    if not matches:
        for r in rules:
            conds = set(r.get("conditions", []))
            matched_conditions = conds.intersection(symptoms)
            unmatched_conditions = conds - symptoms
            total_conditions = len(conds)
            matched_count = len(matched_conditions)
            match_percentage = (matched_count / total_conditions * 100) if total_conditions > 0 else 0
            
            # Skip rules with BMI requirement that doesn't match (unless it's emergency)
            bmi_requirement = r.get("bmi_category")
            bmi_match = True
            bmi_status = "Tidak diperlukan"
            if bmi_requirement:
                user_bmi = metrics.get("bmi_category")
                bmi_match = user_bmi == bmi_requirement
                bmi_status = f"Diperlukan: {bmi_requirement}" + (f" (Sesuai: {user_bmi})" if user_bmi else " (Tidak tersedia)")
            
            # Skip non-emergency rules with BMI mismatch in fallback too
            if bmi_requirement and not bmi_match and r.get("priority", 1) != 0:
                continue
            
            if match_percentage >= 40:  # Increased threshold for fallback (from 30% to 40%)
                # Calculate confidence score (same logic as main matches)
                confidence_score = match_percentage
                
                if matched_count == total_conditions:
                    confidence_score += 50  # Increased bonus for full match
                
                # Priority weighting
                if r.get("priority", 1) == 0:
                    confidence_score += 1000
                elif r.get("priority", 1) == 1:
                    confidence_score += 20
                elif r.get("priority", 1) == 2:
                    confidence_score += 10
                
                # Reduce confidence if BMI doesn't match but is required
                if bmi_requirement and not bmi_match:
                    confidence_score -= 20  # Increased penalty for BMI mismatch
                
                # Special handling for COVID rules in fallback too
                if 'covid' in r.get("id", "").lower():
                    has_characteristic_symptom = any(sym in matched_conditions for sym in ['loss_of_smell', 'loss_of_taste'])
                    if not has_characteristic_symptom and match_percentage < 100:
                        confidence_score -= 40
                
                # Determine match type
                if matched_count == total_conditions:
                    match_type = "Cocok Sempurna"
                else:
                    match_type = "Cocok Sebagian (Rendah)"
                
                matches.append(
                    {
                        "rule_id": r.get("id"),
                        "conclusion": r.get("conclusion"),
                        "advice": r.get("advice", ""),
                        "priority": r.get("priority", 1),
                        "score": matched_count,
                        "total_conditions": total_conditions,
                        "matched_conditions": list(matched_conditions),
                        "unmatched_conditions": list(unmatched_conditions),
                        "match_percentage": round(match_percentage, 1),
                        "confidence_score": round(confidence_score, 1),
                        "match_type": match_type,
                        "bmi_requirement": bmi_requirement,
                        "bmi_match": bmi_match,
                        "bmi_status": bmi_status,
                    }
                )
        
        # Sort again by confidence_score
        matches.sort(key=lambda x: -x["confidence_score"])
        # Limit to top 5 matches
        matches = matches[:5]
    
    return matches
