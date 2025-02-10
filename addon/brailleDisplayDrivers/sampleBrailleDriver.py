"""
Sample Braille Display Driver for NVDA Add-on.
This driver is a stub that outputs braille content as a list, and writes output to a file.
"""

import braille

class SampleBrailleDisplayDriver(braille.BrailleDisplayDriver):
    driverID = "sampleBraille"
    friendlyName = "Sample Braille Display Driver"

    @classmethod
    def check(cls):
        # Always available for testing.
        return True

    def display(self, text):
        output = list(text)
        try:
            with open("braille_output.txt", "w", encoding="utf-8") as f:
                f.write(str(output))
        except Exception as e:
            print("Error writing braille output file:", e)
        return output
