from days_since import data
from generate_image import GenerateImage
from caption_creator import CaptionCreator
from tweet import tweetdata
from inatgrampost import InstagramPost
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=0, minute=5)
def timed_job():
    print('This runs every day 00:05')
    d = data()
    caption = d.get_string()

    gi = GenerateImage(caption)
    photo_path = gi.generate_image()

    cc = CaptionCreator()
    edited_caption = "Days Since India Won A Cricket World Cup: "
    edited_caption += caption
    add_on = cc.get_caption_add_on()
    edited_caption += add_on

    td = tweetdata(edited_caption)
    ip = InstagramPost(photo_path,edited_caption)

    td.tweet()
    ip.post()

sched.start()
