from pydub import AudioSegment


def __main__():
    #files = ['01_%02d_Ustrashenie.mp3' % x for x in range(1, 16)]
    files = ['02_%02d_Kleschi.mp3' % x for x in range(1, 15)]
    joined = sum(AudioSegment.from_mp3(x) for x in files)
    joined.export('part2.mp3', format='mp3')


if __name__ == '__main__':
    __main__()
