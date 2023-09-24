from google.cloud import speech
import google.auth
import os
import torchaudio
import openai
import warnings
import sounddevice as sd
import soundfile as sf
credentials, project_id = google.auth.default()
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials/stt-hackaton-a5ec03ebab27.json'



def capture_audio_to_file(output_file, duration=5):
    sample_rate = 48000  # Standard audio sample rate (in Hz)

    # Record audio
    print(f"Recording audio for {duration} seconds... Press Ctrl+C to stop.")
    audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=2)
    sd.wait()  # Wait for the recording to finish

    # Save the recorded audio as an OGG file
    sf.write(output_file, audio_data, sample_rate)

    print(f"Audio saved as {output_file}")

PROGRAM_PATH = {
        "google": "C:/Program Files/Google/Chrome/Application/chrome.exe",
        "telegram": "C:/Users/edige/AppData/Roaming/Telegram Desktop/Telegram.exe",
        'калькулятор' : '“C:/Windows/system32/calc.exe',
    }
def open_program( program_name):
    if program_name.lower() in PROGRAM_PATH:
        program_path = PROGRAM_PATH[program_name]
        try:
            os.startfile(program_path)
            print(f'Started {program_path}')
        except FileNotFoundError:
            print(f'Error: The program "{program_name}" was not found.')
        except Exception as e:
            print(f'An error occurred: {str(e)}')
            return
    
    
    print(f'Program "{program_name}" not found in the list.')


def get_program_path_by_gpt(program_name):
    openai.api_key = "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"
    messages = [
        {"role": "system", "content": "You are a helpful assistant that provides program paths."},
        {"role": "user", "content": f"Find the default path to {program_name} on Windows. Use one \\"},
    ]

    # Join the messages to create a single string
    prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])

    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        max_tokens=50,  # Replace with your actual API key
    )

    # Extract and print the response
    assistant_response = response.choices[0].text.strip()
    print(f'AI: {assistant_response}' )
    return assistant_response



def transcribe_wav_audio(audio_file_path):
    client = speech.SpeechClient()

    with open(audio_file_path, 'rb') as audio_file:
        content = audio_file.read()
    try:
        metadata = torchaudio.info(audio_file_path).sample_rate
    except:
        pass
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.OGG_OPUS,
        sample_rate_hertz=48000,
        language_code="ru-ru",
    )

    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        alternative = result.alternatives[0]
        print(u"User: {}".format(alternative.transcript))
        prompt = f'{alternative.transcript}'
    return prompt

def main():
    output_file = capture_audio_to_file('input/output.ogg', duration=5)
    output_file = transcribe_wav_audio(output_file)
    # program_path = get_program_path_by_gpt()
    open_program(output_file)

    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    main()
