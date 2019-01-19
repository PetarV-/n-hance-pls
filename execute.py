from get_frames import video_to_frames, frames_to_video
from nhancer import nhance

inp = 'test_videos/IMG_0037.m4v'
out_full = 'test_videos/recon_f.mp4'
out_part = 'test_videos/recon_p.mp4'

frames = video_to_frames(inp)
full, part = nhance(frames, pct=0.5)
frames_to_video(full, out_full)
frames_to_video(part, out_part)

