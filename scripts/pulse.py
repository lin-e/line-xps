import pulsectl
pulse = pulsectl.Pulse('pulsepy')

preferred_output = [
    "CalDigit Thunderbolt 3 Audio Analogue Stereo",
    "CalDigit USB-C HDMI Audio Analogue Stereo",
    "Built-in Audio Analogue Stereo"
]

preferred_input = [
    "RØDE VideoMic NTG Analogue Stereo",
    "CalDigit Thunderbolt 3 Audio Analogue Stereo",
    "Logitech StreamCam Analogue Stereo",
    "Built-in Audio Analogue Stereo"
]

outputs = {}
inputs = {}

for sink in pulse.sink_list():
    outputs[sink.description] = sink

for source in pulse.source_list():
    inputs[source.description] = source

print(pulse.sink_list())

for s in preferred_output:
    if s in outputs:
        pulse.sink_default_set(outputs[s])
        print("Sink set to '" + s + "'")
        break

for s in preferred_input:
    if s in inputs:
        pulse.source_default_set(inputs[s])
        print("Source set to '" + s + "'")
        break
