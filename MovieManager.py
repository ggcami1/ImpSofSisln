from moviepy.editor import VideoFileClip,AudioFileClip
import speech_recognition as sr

class MovieManager:
    def get_audio(self,mp4_file,mp3_file):
        vc=VideoFileClip(mp4_file)
        ac=vc.audio
        ac.write_audiofile(mp3_file)
        ac.close()
        vc.close()
    
    def remove_audio(self,mp4_file,output_mp4):
        video=VideoFileClip(mp4_file)
        video_wa=video.without_audio()
        video_wa.write_videofile(output_mp4)
        video_wa.close()
        video.close()

    def get_wav_audio(self,mp4_file,wav_file):
        vc=VideoFileClip(mp4_file)
        ac=vc.audio
        ac.write_audiofile(wav_file,codec='pcm_s16le')
        ac.close()
        vc.close()

    def audio_to_text(self, audio_file):
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio=r.record(source)
        try:
            text=r.recognize_google(audio, language='es')
            return text
        except:
            return 'unknow'


mm=MovieManager()
#mm.get_audio('video.mp4','audio.mp3')
#mm.remove_audio('video.mp4','videowithoutaudio.mp4')
#mm.get_wav_audio('video.mp4', 'audio.wav')
speech = mm.audio_to_text('audio.wav')
print(speech)
