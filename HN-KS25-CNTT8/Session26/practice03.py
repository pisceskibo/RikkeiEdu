# TÍNH ĐA HÌNH
class MusicPlayer:
    def __init__(self):
        pass

    def play(self):
        print("Phát nhạc")

class PodcastApp:
    def __init__(self):
        pass

    def play(self):
        print("Phát tập mới")

class YoutubePlayer:
    def __init__(self):
        pass

    def play(self):
        print("Phát video")

# Hàm chung
def play_theo_nen_tang(platform):
    platform.play()

play_theo_nen_tang(MusicPlayer())
play_theo_nen_tang(PodcastApp())
play_theo_nen_tang(YoutubePlayer())