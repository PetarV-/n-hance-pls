import skvideo.io
import skvideo.datasets

def video_to_frames(input_loc):
    """
    Deconstructs video to frames

    :param input_loc: Video file
    :return: numpy array with dimensions (time, height, width, channels)
    """
    return skvideo.io.vread(input_loc)


def frames_to_video(array_of_frames, output_loc):
    """
    Reconstructs video from frames, assuming
    :param array_of_frames:
    :param output_loc:
    :return:
    """
    return skvideo.io.vwrite(output_loc, array_of_frames)


if __name__=='__main__':
    input_loc = './test_videos/IMG_0037.m4v'
    output_loc = './test_videos/reconstructed.mp4'
    array_of_frames = video_to_frames(input_loc)
    frames_to_video(array_of_frames, output_loc)

