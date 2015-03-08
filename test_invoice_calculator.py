import unittest

from invoice_calculator import divide_pay


class InvoiceCalculatorTests(unittest.TestCase):
    def testDivideFairly(self):
        # The is supposed to automatically calculate the pay split
        pay = divide_pay(360.0, {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0})
        # Here we manually check the values to ensure the automated check works
        self.assertEqual(pay, {"Alice": 90.0, "Bob": 90.0, "Carol": 180.0})

    def testZeroHourPerson(self):
        pay = divide_pay(360.0, {"Alice": 3.0, "Bob": 6.0, "Carol": 0.0})
        self.assertEqual(pay, {"Alice": 120.0, "Bob": 240.0, "Carol": 0.0})

    def testZeroHoursTotal(self):
        with self.assertRaises(ValueError):
            pay = divide_pay(360.0, {"Alice": 0.0, "Bob": 0.0, "Carol": 0.0})
            self.assertEqual(pay, {"Alice": 0.0, "Bob": 0.0, "Carol": 0.0})

    def testNoPeople(self):
        with self.assertRaises(ValueError):
            pay = divide_pay(360.0, {})
            self.assertEqual(pay, {})

if __name__ == '__main__':
    unittest.main()