# from PIL import Image, ImageOps, ImageDraw

# im = Image.open("../images/placeholders/sizes.png")
# crop_size = (120, 120)
# min_size = (160,160)

# # if im.size > min_size:
# #     box = (
# #         im.size[0]//2 - crop_size[0]//2, 
# #         im.size[1]//2 - crop_size[1]//2, 
# #         im.size[0]//2 + crop_size[0]//2, 
# #         im.size[1]//2 + crop_size[1]//2
# #         )
# #     region = im.crop(box)
 
# # else:
# #     region = im

# # if im.size > min_size:
# #     region = region.rotate(45)
# #     im.paste(region, box)
# # # im = Image.new("RGBA", (100, 100))

# # im.show()

# # im = ImageOps.fit(im, crop_size)
# # im.thumbnail(crop_size)
# # im.show()

# im = Image.new("RGBA", (280, 120), (0, 0, 0, 0))
# d = ImageDraw.Draw(im)
# d.rounded_rectangle(
#     [(0, 0), (280, 120)],radius=6,fill=(200, 200, 200),outline=None         
# )
# # d.rectangle((0, 0, 100, 100), (0, 255, 0, 127))
# # d.line((10, 10) + (im.size[0]-10, 10), width=2, fill=(255,255,255))
# # d.line((10, 10) + (10, im.size[1]-10), width=2, fill=(255,255,255))
# # d.line((10, im.size[1]-10) + (im.size[0]-10, im.size[1]-10), width=2, fill=(255,255,255))
# # d.line((im.size[0]-10, im.size[1]-10) + (im.size[0]-10, 10), width=2, fill=(255,255,255))
# # # d.line((10, -10) + (10, im.size[1]-10), fill=128)
# # # d.line((-10, -10) + (10, im.size[1]-10), fill=128)
# # d.circle((10+2,10+2), 2, fill=(255,255,255), outline=None, width=10)
# # d.circle((10+2,im.size[1]-10-2), 2, fill=(255,255,255), outline=None, width=1)
# # d.circle((im.size[0]-10-2, 10+2), 2, fill=(255,255,255), outline=None, width=1)
# # d.circle((im.size[0]-10-2, im.size[1]-10-2), 2, fill=(255,255,255), outline=None, width=1)
# # im.show()
# d.rounded_rectangle(
#     [(11, 11), (280-11, 120-11)],radius=5,outline=(0,0,0), width=1 
# )
# d.rounded_rectangle(
#     [(10, 10), (280-10, 120-10)],radius=5,outline=(255,255,255), width=1      
# )
# d.rounded_rectangle(
#     [(9, 9), (280-9, 120-9)],radius=5,outline=(0,0,0), width=1 
# )
# pad = 20
# im_padded = ImageOps.expand(im, border=pad, fill=(0,0,0,0))

# im_padded.show()
# # im_padded.save("./test.png")
# # from PIL import Image, ImageDraw, ImageFont

# # get an image
# # with Image.open("Pillow/Tests/images/hopper.png").convert("RGBA") as base:

# #     # make a blank image for the text, initialized to transparent text color
# #     txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

# #     # get a font
# #     fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
# #     # get a drawing context
# #     d = ImageDraw.Draw(txt)

# #     # draw text, half opacity
# #     d.text((10, 10), "Hello", font=fnt, fill=(255, 255, 255, 128))
# #     # draw text, full opacity
# #     d.text((10, 60), "World", font=fnt, fill=(255, 255, 255, 255))

# #     out = Image.alpha_composite(base, txt)

# #     out.show()


# from PIL import Image, ImageDraw

# COLORS = {
#     # metallics
#     "gold":          (255, 215, 0),
#     "silver":        (192, 192, 192),
#     "bronze":        (205, 127, 50),
#     "platinum":      (229, 228, 226),
#     "rose_gold":     (183, 110, 121),
#     "break" : (1),
#     # grayscale
#     "white":         (255, 255, 255),
#     "black":         (0, 0, 0),
#     "light_gray":    (211, 211, 211),
#     "gray":          (128, 128, 128),
#     "dark_gray":     (64, 64, 64),
#     "break2" : (1),
#     # reds
#     "red":           (255, 0, 0),
#     "dark_red":      (139, 0, 0),
#     "rose":          (255, 102, 102),
#     "crimson":       (220, 20, 60),
#     "break3" : (1),
#     # oranges + yellows
#     "orange":        (255, 165, 0),
#     "dark_orange":   (255, 140, 0),
#     "yellow":        (255, 255, 0),
#     "amber":         (255, 191, 0),
#     "break4" : (1),
#     # greens
#     "green":         (0, 128, 0),
#     "light_green":   (144, 238, 144),
#     "lime":          (50, 205, 50),
#     "mint":          (152, 255, 152),
#     "emerald":       (80, 200, 120),
#     "break5" : (1),
#     # blues
#     "blue":          (0, 0, 255),
#     "sky_blue":      (135, 206, 235),
#     "navy":          (0, 0, 128),
#     "cyan":          (0, 255, 255),
#     "teal":          (0, 128, 128),
#     "break6" : (1),
#     # purples
#     "purple":        (128, 0, 128),
#     "lavender":      (230, 230, 250),
#     "violet":        (238, 130, 238),
#     "magenta":       (255, 0, 255),
#     "break7" : (1),
#     # browns / earthy
#     "brown":         (150, 75, 0),
#     "tan":           (210, 180, 140),
#     "sand":          (194, 178, 128),
#     "break8" : (1),
#     # specialty / aesthetic colors
#     "pastel_pink":   (255, 182, 193),
#     "pastel_blue":   (174, 198, 255),
#     "pastel_green":  (119, 221, 119),
#     "neon_green":    (57, 255, 20),
#     "neon_pink":     (255, 20, 147),
#     "neon_blue":     (0, 160, 255)
# }

# im = Image.new("RGBA", (140,200), (0,0,0,0))
# # im.show()
# d = ImageDraw.Draw(im)
# c = 0
# line = 10
# col = 10
# size = 15
# for i in COLORS:
    
#     # if c==13:
#     #     line+=20
#     #     col = 10
#     #     c = 0
#     if "break" in i:
#         line+=20
#         col = 10
#         c = 0
#         continue
    
#     d.rectangle((col, line, col + size, line + size), fill=COLORS[i])
#     # c+=1
#     col+=20
    
# im.show() 

# im.save("colors_avail.png")

