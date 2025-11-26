from health_metrics import calculate_bmi, bmi_category


def test_bmi_metric_rounding():
    bmi_raw, bmi_display = calculate_bmi(70, 175, units='metric')
    assert round(bmi_raw, 2) == 22.86
    assert bmi_display == 22.86
    assert bmi_category(bmi_raw) == "Normal"


def test_bmi_imperial_conversion():
    # 154.324 lb ≈ 70 kg, 68.8976 in ≈ 175 cm
    bmi_raw, bmi_display = calculate_bmi(154.324, 68.8976, units='imperial')
    assert bmi_display == 22.86


def test_invalid_values():
    try:
        calculate_bmi(0, 170)
    except ValueError as err:
        assert "greater than zero" in str(err)
    else:
        raise AssertionError("calculate_bmi should raise ValueError for zero weight")
