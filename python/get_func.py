#!/usr/bin/env python3

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

if __name__=='__main__':
    res = get_speak_func(float(input("Введите число ")))
    print(res(input()))
