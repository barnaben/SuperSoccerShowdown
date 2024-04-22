import unittest


def suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.')

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
