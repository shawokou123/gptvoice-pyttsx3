import os
import platform
import pyttsx3
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def is_chinese(voice):
    # Check if the voice supports Chinese based on the 'zh' in languages
    return any('zh' in lang.lower() for lang in voice.languages)

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the volume of the speech (0.0 to 1.0)
    engine.setProperty('volume', 0.9)

    # Set the speech rate (default is 200)，加快读取文字的速度
    engine.setProperty('rate', 210)

    # Set the voice to Mandarin (Chinese) if available
    voices = engine.getProperty('voices')
    chinese_voice = next((voice.id for voice in voices if is_chinese(voice)), None)
    if chinese_voice:
        engine.setProperty('voice', "com.apple.voice.compact.zh-CN.Tingting")
    else:
        print("未找到中文语音，将使用默认语音")

    # Convert and play the text
    engine.say(text)
    engine.runAndWait()

def main():
    # 从文本文件中读取要转换为语音的文本
    file_path = 'cui_huifu.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # print(f"读取到的文本内容:\n{text}")

    # 调用文本到语音转换函数
    text_to_speech(text)

if __name__ == '__main__':
    main()