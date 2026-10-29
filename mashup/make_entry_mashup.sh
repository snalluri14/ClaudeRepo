#!/usr/bin/env bash
# Builds the grand-entry mashup from one song's audio:
#   part 1: 2:19 -> 3:00
#   part 2: 0:26 -> end
# joined with a short crossfade, fade-in at the start and fade-out at the end.
#
# Usage: ./make_entry_mashup.sh <input-audio-file> [output.mp3]
# Requires: ffmpeg
set -euo pipefail

IN="${1:?usage: $0 <input-audio-file> [output.mp3]}"
OUT="${2:-grand_entry_mashup.mp3}"
XFADE=1.5   # seconds of overlap between the two parts

TOTAL=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
PART2_LEN=$(awk -v t="$TOTAL" 'BEGIN { printf "%.3f", t - 26 }')
FINAL_LEN=$(awk -v a=41 -v b="$PART2_LEN" -v x="$XFADE" 'BEGIN { printf "%.3f", a + b - x }')
FADE_OUT_START=$(awk -v l="$FINAL_LEN" 'BEGIN { printf "%.3f", l - 3 }')

ffmpeg -y -i "$IN" -filter_complex "
  [0:a]atrim=start=139:end=180,asetpts=PTS-STARTPTS[p1];
  [0:a]atrim=start=26,asetpts=PTS-STARTPTS[p2];
  [p1][p2]acrossfade=d=${XFADE}:c1=tri:c2=tri,
  afade=t=in:st=0:d=1,afade=t=out:st=${FADE_OUT_START}:d=3,
  loudnorm=I=-14:TP=-1.0:LRA=11[out]" \
  -map "[out]" -ar 44100 -b:a 320k "$OUT"

echo "Created $OUT (${FINAL_LEN}s)"
