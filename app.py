import os
import datetime

from dotenv import load_dotenv
from openai import OpenAI
from elevenlabs import generate, stream, save
from elevenlabs.client import ElevenLabs

load_dotenv()
client = OpenAI()
eleven_client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))
# Add mpv to the path
os.environ["PATH"] += os.pathsep + os.getenv("MPV_PATH")


def stream_audio(text_stream, prompt: str):
    audio_stream = generate(
        # api_key="YOUR_API_KEY", (Defaults to os.getenv(ELEVEN_API_KEY))
        text=text_stream(prompt),
        voice="d3OVHCiszKMFso7dAHaE",
        model="eleven_turbo_v2",
        stream=True,
    )

    return audio_stream


def get_poem(
    prompt="Compose a poem that explains the concept of recursion in programming.",
):
    completion = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {
                "role": "system",
                "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return completion.choices[0].message.content


def stream_poem(
    prompt="Compose a poem that explains the concept of recursion in programming.",
):
    stream_text = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {
                "role": "system",
                "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
            },
            {"role": "user", "content": prompt},
        ],
        stream=True,
    )

    for chunk in stream_text:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
            yield chunk.choices[0].delta.content


if __name__ == "__main__":
    # stream_text = stream_poem()
    # for chunk in stream_text:
    #     if chunk.choices[0].delta.content is not None:
    #         print(chunk.choices[0].delta.content, end="")
    streaming = stream_audio(stream_poem, "Compose a poem that explains the concept of recursion in programming.")
    bytes = stream(streaming)

    # Save the poem to mp3 file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_recursion_poem.mp3"
    save(bytes, filename)
