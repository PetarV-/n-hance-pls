import skvideo.io

def video_to_frames(input_loc):
    """
    Deconstructs video to frames

    :param input_loc: Video file
    :return: numpy array with dimensions (time, height, width, channels)
    """
    return skvideo.io.vread(input_loc)


def frames_to_video(array_of_frames, output_loc):
    """
    Reconstructs video from frames

    :param array_of_frames: numpy array with dimensions (time, height, width, channels)
    :param output_loc: path to video file to be saved
    """
    rate = "30"
    writer = skvideo.io.FFmpegWriter(output_loc, inputdict={
      '-r': rate,
    },
    outputdict={
      '-vcodec': 'libx264',
      '-pix_fmt': 'yuv420p',
      '-r': rate,
    })
    for i in range(len(array_of_frames)):
        writer.writeFrame(array_of_frames[i, :, :, :])
    writer.close()
    return


if __name__=='__main__':
    input_loc = './test_videos/IMG_0037.MOV'
    output_loc = './test_videos/reconstructed.mp4'
    array_of_frames = video_to_frames(input_loc)
    frames_to_video(array_of_frames, output_loc)

