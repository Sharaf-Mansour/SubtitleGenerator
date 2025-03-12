# Whisper Subtitle Generator

A simple Python script to automatically create subtitles (in `.srt` format) for video files using OpenAI's Whisper model. It runs locally on your computer and is easy to use.

## Features

- 🎬 **Auto Subtitles**: Creates subtitles for `.mp4` video files.
- 🚀 **Fast and Local**: Runs directly on your computer, no internet needed.
- 📝 **Easy Output**: Generates `.srt` subtitle files ready for any video player.
- 🔄 **Skips Existing**: If subtitles already exist, it skips reprocessing.

---

## Requirements

- Python 3.8 or higher
- [FFmpeg](https://ffmpeg.org/) (for processing video files)
- Python packages:
  - `openai-whisper`
  - `ffmpeg-python`

---

## Installation

1. **Download the Script** Clone this repository or download the script manually.

2. **Install Python Packages**

```bash
pip install openai-whisper ffmpeg-python
```

3. **Install FFmpeg**

- **Windows**: [Download FFmpeg](https://ffmpeg.org/download.html) and add it to your system PATH.
- **Linux**:

```bash
sudo apt update
sudo apt install ffmpeg
```

- **macOS**:

```bash
brew install ffmpeg
```

---

## How to Use

1. Place the script in the same folder as your `.mp4` video files.
2. Open a terminal in that folder and run the script:

```bash
python whisper_subtitle.py
```

3. The script will automatically create `.srt` subtitle files for each `.mp4` file.
4. If a subtitle file already exists, it will skip that video.

---

## Example Code

```python
import whisper
import os
import time

def generate_subtitles(input_file, output_file="subtitles.srt"):
    model = whisper.load_model("small")
    print(f"Processing '{input_file}'...")
    result = model.transcribe(input_file)

    with open(output_file, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result['segments']):
            start = format_timestamp(segment['start'])
            end = format_timestamp(segment['end'])
            f.write(f"{i + 1}
{start} --> {end}
{segment['text'].strip()}

")

    print(f"Subtitles saved to '{output_file}'!")

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

if __name__ == "__main__":
    current_folder = os.getcwd()
    total_start_time = time.time()

    for file_name in os.listdir(current_folder):
        if file_name.endswith(".mp4"):
            input_file = os.path.join(current_folder, file_name)
            output_file = f"{os.path.splitext(file_name)[0]}.srt"

            if os.path.exists(output_file):
                print(f"Skipping '{input_file}' as it is already subtitled.")
                continue

            start_time = time.time()
            generate_subtitles(input_file, output_file=output_file)
            end_time = time.time()
            print(f"File: {input_file} | Start Time: {time.strftime('%H:%M:%S', time.localtime(start_time))} | End Time: {time.strftime('%H:%M:%S', time.localtime(end_time))} | Duration: {end_time - start_time:.2f} seconds")

    total_end_time = time.time()
    print(f"Total processing time: {total_end_time - total_start_time:.2f} seconds")
```

---

## Customization

- **Change Whisper Model**: For better accuracy, change the model from `small` to `medium` or `large`.

```python
model = whisper.load_model("large")
```

- **Change Output File Name**:

```python
generate_subtitles("input.mp4", "custom_name.srt")
```

---

## Troubleshooting

- **FFmpeg Not Found**: Make sure FFmpeg is installed and added to your system's PATH.
- **Slow Processing**: Try using a smaller model like `tiny` or `base`.
- **CUDA Not Detected**: Ensure you have an NVIDIA GPU and CUDA is installed properly.

---

## License

This project is licensed under the MIT License.

---

## Contributions

Feel free to open pull requests or issues for improvements.

---

## Credits

- [OpenAI Whisper](https://github.com/openai/whisper)
- [FFmpeg](https://ffmpeg.org/)

---
