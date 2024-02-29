from PIL import Image, ImageDraw
im = Image.new("RGB",(500,300),(219,193,27))
draw=ImageDraw.Draw(im)
im.show()