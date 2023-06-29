class Video:

    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx=0):
        cls.videos[video_indx].play()


v1 = Video()
v2 = Video()
v1.create("Python")
#v2.create("Python ООП")
v1.play()
#YouTube.add_video(v1)
#YouTube.add_video(v2)
#YouTube.play()
#YouTube.play(1)




