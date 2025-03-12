import whisper
import os
import time

def generate_subtitles(input_file, output_file="subtitles.srt"):
    # Load Whisper model
    model = whisper.load_model("small")  # You can also use "small", "medium", or "large"

    # Transcribe audio/video
    print(f"Processing '{input_file}'...")
    result = model.transcribe(input_file)

    # Write subtitles to SRT file
    with open(output_file, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result['segments']):
            start = format_timestamp(segment['start'])
            end = format_timestamp(segment['end'])
            f.write(f"{i + 1}\n{start} --> {end}\n{segment['text'].strip()}\n\n")
    
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
