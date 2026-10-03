# Arohak × Quanfluence: 112 use-case AV

| File | What it is |
|---|---|
| `scene_av.html` | **The video itself**: every scene drawn on an HTML canvas. `window.render(t)` draws the frame at time `t` seconds (158 s total). Edit text, timings or visuals here. |
| `render.js` | Opens the scene in headless Chromium (Playwright), captures every frame and encodes the MP4 with ffmpeg. |
| `merge_voice.py` | Cuts the ElevenLabs narration into paragraphs and places each one on its scene. |
| `logos/` | Arohak and Quanfluence logo files used in the video. |
| `voiceover_elevenlabs.mp3` | The ElevenLabs narration. |
| `arohak_quanfluence_112_AV.mp4` | Silent version (captions only), for looping at the stall. |
| `arohak_quanfluence_112_AV_voice.mp4` | Version with voice-over. |
| `SCRIPT.md`, `ELEVENLABS_VIDEO_SCRIPT.md`, `ELEVENLABS_PROMPTS.md`, `VOICEOVER.md` | Scripts, scene cards and narration text. |

## Rebuild

Requirements: Node.js with `playwright`, Python 3 with `imageio-ffmpeg`.

```bash
cd expo-video-qubo
# The logos are loaded as images, so serve the folder over http (file:// blocks frame capture)
python3 -m http.server 8765 --bind 127.0.0.1 &

# Preview stills at chosen seconds -> stills/
URL=http://127.0.0.1:8765/scene_av.html node render.js stills 2,12,38,70,118,140

# Full silent video (about 8 min)
FFMPEG=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())") \
URL=http://127.0.0.1:8765/scene_av.html OUT=arohak_quanfluence_112_AV.mp4 node render.js video 30

# Add the voice-over
python3 merge_voice.py
```

Scene start times (seconds), used by both `scene_av.html` and `merge_voice.py`:
0 Arohak logo · 4 partnership · 8 calls · 16 three decisions · 28 right hospital · 43 complexity · 63 step 1 · 78 step 2 · 93 step 3 · 108 step 4 · 123 step 5 · 128 result (16.9%) · 143 roadmap · 151 close.
