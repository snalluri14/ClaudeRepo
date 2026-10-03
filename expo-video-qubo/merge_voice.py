"""Cut the ElevenLabs narration into its 14 paragraphs and place each one at the
start of its scene in the silent AV, producing arohak_quanfluence_112_AV_voice.mp4.

Paragraph boundaries were taken from the pauses in voiceover_elevenlabs.mp3
(ffmpeg silencedetect). If you record new audio, re-check these times.
"""
import subprocess
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
VIDEO, AUDIO, OUT, LENGTH = 'arohak_quanfluence_112_AV.mp4', 'voiceover_elevenlabs.mp3', 'arohak_quanfluence_112_AV_voice.mp4', 158

# (audio start s, audio end s, video cue s) — one row per narration paragraph
SEGMENTS = [
    (0.00, 1.38, 0.5),      # Arohak Technologies.
    (1.79, 3.72, 5.0),      # In partnership with Quanfluence.
    (4.23, 13.71, 8.6),     # Distress calls across the state
    (14.35, 21.35, 18.5),   # Three decisions
    (21.91, 31.99, 28.6),   # Right hospital
    (32.43, 42.04, 43.5),   # Complexity
    (42.51, 51.70, 63.5),   # Step 1
    (52.20, 64.92, 78.4),   # Step 2 (QUBO)
    (65.42, 73.91, 93.5),   # Step 3 (zones)
    (74.43, 86.60, 108.5),  # Step 4 (Ising machine)
    (87.08, 92.44, 123.3),  # Step 5 (decode)
    (92.79, 99.21, 132.0),  # 16.9% result — ends as the badge appears
    (99.66, 107.48, 143.3), # Roadmap
    (107.94, 113.08, 151.5),# Close
]

parts, labels, prev = [], [], 0.0
for i, (a, b, cue) in enumerate(SEGMENTS):
    a, b = max(0, a - 0.08), b + 0.08
    start = max(cue, prev + 0.3)   # never overlap the previous line
    prev = start + (b - a)
    d = int(start * 1000)
    parts.append(f"[0:a]atrim={a:.2f}:{b:.2f},asetpts=PTS-STARTPTS,afade=t=in:d=0.04,"
                 f"afade=t=out:st={b - a - 0.06:.2f}:d=0.06,adelay={d}|{d}[s{i}]")
    labels.append(f"[s{i}]")
graph = ";".join(parts) + ";" + "".join(labels) + \
    f"amix=inputs={len(SEGMENTS)}:normalize=0,apad,atrim=0:{LENGTH},loudnorm=I=-16:TP=-1.5:LRA=11[a]"

subprocess.run([FF, '-y', '-i', AUDIO, '-i', VIDEO, '-filter_complex', graph, '-map', '1:v', '-map', '[a]',
                '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-movflags', '+faststart', OUT], check=True)
print('wrote', OUT)
