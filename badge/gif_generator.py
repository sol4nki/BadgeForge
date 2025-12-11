from PIL import Image, ImageDraw


banner_size = (280, 120)
tmp_size = (600,120)
banner = Image.new("RGBA",banner_size, (0, 0, 0, 0))
d = ImageDraw.Draw(banner)
d.rounded_rectangle(
    [(0, 0), banner_size],
    radius=banner_size[1]//20,
    fill="silver",
    outline=None         
)

im1 = Image.new("RGBA",tmp_size, (0, 0, 0, 0))
dtmp = ImageDraw.Draw(im1)

dtmp.rectangle((0,0, 400, 50), fill=(250, 250, 250, 50))
im1 = im1.rotate(45, expand=True)
banner.paste(im1,(0,0), im1)
banner.show()