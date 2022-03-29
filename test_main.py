import main
import pytest

# @pytest.fixture
# def input():
#     a=25
#     return a
# def test_divby5(input):
#     # a=10
#     # result1=main.divby5(a)
#     result1 = main.divby5(input)
#     assert result1==True
#
#
# def test2_divby5(input):
#     #a = 11
#     # result1 = main.divby5(a)
#     result1 = main.divby5(input)
#     assert result1 == False
#
# def test_divby7(input):
#     # a = 14
#     # result1 = main.divby7(a)
#     result1 = main.divby7(input)
#     assert result1 == True
#
# def test_divby7_1(input):
#     # a = 11
#     # result1 = main.divby7(a)
#     result1 = main.divby7(input)
#     assert result1 == False
#
# def test_divby9(input):
#     # a = 18
#     # result1 = main.divby9(a)
#     result1 = main.divby9(input)
#     assert result1 == True
#
# def test2_divby9_1(input):
#     # a = 11
#     # result1 = main.divby9(a)
#     result1 = main.divby9(input)
#     assert result1 == False
#
# def test_divby11(input):
#     # a = 22
#     # result1 = main.divby11(a)
#     result1 = main.divby11(input)
#     assert result1 == True
#
# def test2_divby11_1(input):
#     # a = 14
#     # result1 = main.divby11(a)
#     result1 = main.divby11(input)
#     assert result1 == False


import main
import pytest


@pytest.mark.parametrize("num,output", [(5, True), (2, False), (10, True), (7, False)])
# def input():
#     a = 25
#     return a

def test_divby5(num, output):
    result = main.divby5(num)
    assert result == output


#
#
# def test_fcheckDivisibleby5(input):
#     result = Divisible.checkDivisibleby5(input)
#     assert False == result
#
@pytest.mark.parametrize("num,output", [(7, True), (2, False), (14, True), (33, False)])
def test_divby7(num, output):
    result = main.divby7(num)
    assert result == output


#
# def test_fcheckDivisibleby7(input):
#     result = Divisible.checkDivisibleby7(input)
#     assert False == result
#
@pytest.mark.parametrize("num,output", [(9, True), (2, False), (18, True), (33, False)])
def test_divby9(num, output):
    result = main.divby9(num)
    assert result == output


#
# def test_fcheckDivisibleby9(input):
#     result = Divisible.checkDivisibleby9(input)
#     assert False == result
#
@pytest.mark.parametrize("num,output", [(11, True), (2, False), (22, True), (34, False)])
def test_divby11(num, output):
    result = main.divby11(num)
    assert result == output
#
# def test_fcheckDivisibleby11(input):
#     result = Divisible.checkDivisibleby11(input)
#     assert False == result




