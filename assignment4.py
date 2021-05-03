import unittest


def calculate_volume(length, width, height):
    volume = length * width * height
    return volume


def calc_list_avg(numList):
    count = 0
    sumList = 0
    for x in numList:
        count += 1
        sumList += x
    average = sumList / count
    return average


def gen_full_name():
    firstName = input("Enter a first name: \n")
    lastName = input("Enter a last name: \n")
    fullName = firstName + " " + lastName
    return firstName, lastName, fullName


class TestStringMethods(unittest.TestCase):

    def test_calc_vol(self):
        length = 5
        width = 5
        height = 5
        parameters = type(length), type(width), type(height)
        self.assertEqual(parameters, (int, int, int))  # Pass
        self.assertTrue(length > 0 and width > 0 and height > 0)  # Pass
        # self.assertEqual(calculate_volume(length, width, height), 15)  # Fail

    def test_list_avg(self):
        testList = [5, 6, 7, 1, 2, 3, 5, 9]
        # self.assertEqual(calc_list_avg(testList), 275)  # Fail
        self.assertTrue(len(testList) > 0)  # Pass
        self.assertIsNotNone(testList)  # Pass

    def test_full_name(self):
        names = gen_full_name()
        self.assertEqual(type(names), tuple)  # Pass
        # self.assertEqual(type(names[1]), int)  # Fail
        self.assertTrue(names[2] == names[0] + " " + names[1])  # Pass


if __name__ == '__main__':
    unittest.main()
