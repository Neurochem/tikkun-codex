import math
import wave
import struct

# ===== PlasmaNode Harmonic Drone =====
# Deep, resonant, meditative, ritualistic

SAMPLE_RATE = 44100      # samples per second
DURATION    = 60         # seconds
VOLUME      = 0.4        # 0.0–1.0

# Base frequency and harmonics (in Hz)
BASE_FREQ   = 70.0       # fundamental
HARMONIC_2  = BASE_FREQ * 2.0   # octave
HARMONIC_3  = BASE_FREQ * 2.5   # fifth above octave

# Slow modulation (LFOs)
AMP_LFO_FREQ   = 0.05    # amplitude breathing (Hz)
FREQ_LFO_FREQ  = 0.03    # subtle pitch drift (Hz)
FREQ_LFO_DEPTH = 0.4     # semitone-ish drift

OUTPUT_FILE = "plasma_drone.wav"

def main():
    num_samples = int(SAMPLE_RATE * DURATION)

    with wave.open(OUTPUT_FILE, "w") as wav_file:
        wav_file.setnchannels(2)          # stereo
        wav_file.setsampwidth(2)          # 16-bit
        wav_file.setframerate(SAMPLE_RATE)

        for n in range(num_samples):
            t = n / SAMPLE_RATE

            # Slow amplitude breathing (0.7–1.0)
            amp_lfo = 0.85 + 0.15 * math.sin(2 * math.pi * AMP_LFO_FREQ * t)

            # Slow pitch drift in semitone space
            freq_lfo = math.sin(2 * math.pi * FREQ_LFO_FREQ * t) * FREQ_LFO_DEPTH
            freq_factor = 2 ** (freq_lfo / 12.0)

            f1 = BASE_FREQ   * freq_factor
            f2 = HARMONIC_2  * freq_factor
            f3 = HARMONIC_3  * freq_factor

            s1 = math.sin(2 * math.pi * f1 * t)
            s2 = math.sin(2 * math.pi * f2 * t)
            s3 = math.sin(2 * math.pi * f3 * t)

            # Blend harmonics
            sample = (0.6 * s1 + 0.3 * s2 + 0.2 * s3) * amp_lfo

            # Apply master volume and clamp
            sample *= VOLUME
            sample = max(-1.0, min(1.0, sample))

            int_sample = int(sample * 32767)
            data = struct.pack("<hh", int_sample, int_sample)  # stereo (L,R same)
            wav_file.writeframesraw(data)

    print(f"Done. Wrote {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
