import test_simulation
import test_lm73device
import test_xmlMeasurementService
import test_compositeThermometer_SWD11G2_3
import unittest

suite = unittest.TestSuite()
suite.addTest(test_simulation.suite)
suite.addTest(test_lm73device.suite)
suite.addTest(test_xmlMeasurementService.suite)
suite.addTest(CompositeSensor_SWD11G2_3Test.suite)


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)
    pass
