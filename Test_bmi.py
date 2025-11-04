import Lab2.bmi as bmi

def test_bmi_under_weight():
    input_height = 1.78
    input_weight = 40
    test_bmi = -1

    result = bmi.calculate_bmi(input_height,input_weight)
    assert (result == test_bmi)

def test_bmi_normal_weight():
    input_height = 1.78
    input_weight = 66
    test_bmi = 0

    result = bmi.calculate_bmi(input_height,input_weight)
    assert (result == test_bmi)


def test_bmi_over_weight():
    input_height = 1.78
    input_weight = 80
    test_bmi = 1

    result = bmi.calculate_bmi(input_height,input_weight)
    assert (result == test_bmi)
