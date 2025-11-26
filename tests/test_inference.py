from inference_engine import infer


def test_infer_empty():
    assert infer([]) == []


def test_infer_flu_like():
    res = infer(['fever', 'cough', 'sore_throat'])
    assert any('Influenza' in (r['conclusion'] or '') or 'Common Cold' in (r['conclusion'] or '') for r in res)


def test_infer_with_bmi_requirement():
    metrics = {"bmi_category": "Obesity"}
    res = infer(['shortness_of_breath'], metrics=metrics)
    assert any(r['rule_id'] == 'r_obesity_resp' for r in res)
