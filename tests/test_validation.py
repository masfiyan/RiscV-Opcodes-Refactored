
import unittest
import subprocess

class TestValidationScript(unittest.TestCase):
    def test_validation_script(self):
        result = subprocess.run(['python3', 'tools/validate_opcodes.py'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Validation script failed")
        self.assertIn("Validation completed successfully.", result.stdout, "Validation script output did not match expected")

if __name__ == '__main__':
    unittest.main()
