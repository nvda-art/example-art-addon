"""
Sample Synthesizer Driver for NVDA Add-on.
This driver is a stub that outputs spoken text as a list of words, and writes output to a file.
"""

import synthDriverHandler

class SampleSynthDriver(synthDriverHandler.SynthDriver):
    DRIVER_NAME = "sampleSynth"
    friendlyName = "Sample Synthesizer Driver"

    @classmethod
    def check(cls):
        # Always available for testing.
        return True

    def speak(self, message):
        output = message.split()
        try:
            with open("synth_output.txt", "w", encoding="utf-8") as f:
                f.write(str(output))
        except Exception as e:
            print("Error writing synth output file:", e)
        return output
