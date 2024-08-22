import json

data= json.load(open("frames.json","r"))

nb_frames = len(data)
nb_frames_found  = len([d for d in data if d['target_video_url'] is not None])


completion = nb_frames_found/nb_frames

items = "<br/>".join(
    f'''<div class="item"> 
       {d['reference_frame_url'].split('/')[-1]} <img loading="lazy" src={d['reference_frame_url']}  /> { f"""<a href="{d['target_video_url']}">Target Found</a>""" if d['target_video_url'] is not None else "No Target Found"}
    </div>'''
    for d in data
)
html = rf"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mauvaise Pomme</title>
    <style>
    .item{{
        display: flex;
    }}
    </style>
</head>
<body>
    <div>Completion {completion:.02f}% ({nb_frames_found}/{nb_frames}) </div>
    {items}
</body>
</html>
"""


open("index.html","w").write(html)