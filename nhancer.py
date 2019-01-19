import numpy as np
import tensorflow as tf
from model import resnet
import utils
import os
import sys

use_gpu = True
batch_sz = 32

img_h = 720
img_w = 1280
img_d = 3
img_sz = img_h * img_w * img_d

config = tf.ConfigProto(device_count={'GPU': 0}) if not use_gpu else None

x_ = tf.placeholder(tf.float32, [None, img_sz])
x_image = tf.reshape(x_, [-1, img_h, img_w, img_d])
enhanced = resnet(x_image)

def nhance(frames, pct=1.0):
    with tf.Session(config=config) as sess:
        saver = tf.train.Saver()
        saver.restore(sess, "models/iphone")

        imgs = np.float16(frames) / 255
        vlen = frames.shape[0]

        ret = np.empty(frames.shape, dtype=np.uint8)
        if pct < 1.0:
            ret_ba = np.copy(frames)
            lim_pt = int(img_w * (1.0 - pct))
        else:
            ret_ba = None

        ptr = 0
        while ptr < vlen:
            print('Ptr is: ', ptr)
            bsz = batch_sz if ptr + batch_sz <= vlen else (vlen - ptr) 
            batch = np.reshape(imgs[ptr : ptr + bsz], [bsz, img_sz])
            r_batch = sess.run(batch, feed_dict={x_: batch})
            r_batch = np.uint8(np.reshape(r_batch, [batch_sz, img_h, img_w, img_d]) * 255)
            ret[ptr : ptr + batch_sz, :, :, :] = r_batch
            if pct < 1.0:
                ret_ba[ptr : ptr + batch_sz, :, lim_pt:, :] = rbatch[:, :, lim_pt:, :]
            ptr += bsz

        return ret, ret_ba
