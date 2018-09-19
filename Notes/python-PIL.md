from PIL import Image

bmpFile = Image.open(r'bmp/FLAG_B24.BMP')
bmpFile.close()
`
['BITFIELDS', 'COMPRESSIONS', 'JPEG', 'PNG', 'RAW', 'RLE4', 'RLE8', '_Image__transformer', '__array_interface__', '__class__', '__copy__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bitmap', '_close_exclusive_fp_after_loading', '_copy', '_crop', '_dump', '_ensure_mutable', '_exclusive_fp', '_expand', '_min_frame', '_new', '_open', '_repr_png_', '_seek_check', 'alpha_composite', 'category', 'close', 'convert', 'copy', 'crop', 'decoderconfig', 'decodermaxblock', 'draft', 'effect_spread', 'filename', 'filter', 'format', 'format_description', 'fp', 'frombytes', 'fromstring', 'get_format_mimetype', 'getbands', 'getbbox', 'getchannel', 'getcolors', 'getdata', 'getextrema', 'getim', 'getpalette', 'getpixel', 'getprojection', 'height', 'histogram', 'im', 'info', 'load', 'load_end', 'load_prepare', 'mode', 'offset', 'palette', 'paste', 'point', 'putalpha', 'putdata', 'putpalette', 'putpixel', 'pyaccess', 'quantize', 'readonly', 'remap_palette', 'resize', 'rotate', 'save', 'seek', 'show', 'size', 'split', 'tell', 'thumbnail', 'tile', 'tobitmap', 'tobytes', 'toqimage', 'toqpixmap', 'tostring', 'transform', 'transpose', 'verify', 'width']
`
bmpFile.format, bmpFile.size, bmpFile.mode
bmpFile.width,bmpFile.height

bmpFile.show()

bmpFile.getpixel((x,y))

# 点集操作
out = bmpFile.point(lambda i:i//2)
out.show()

# 颜色模式转换
#“L”, “RGB” and “CMYK.”
out = bmpFile.convert("L")
out.show()

# resize
out = bmpFile.resize((500,500))
out.show()

# 图像旋转
out = bmpFile.rotate(45)
out.show()

# 分离与合并通道
r, g, b = bmpFile.split()
im = Image.merge("RGB", (b, g, r))


# 剪切粘贴和合并图像
Image类包含维护图像里区块的方法。为了从图像里抽取一个子矩形，使用crop()方法。

复制一个子矩形
box = (100, 100, 400, 400)
region = im.crop(box)
使用包含4个元素的元组来定义区块，相匹配的坐标是（左上右下）。PIL使用一个坐标系统，原点位于左上角。坐标系统使用像素来引用位置，所以上例中的区块大小是300x300像素。

现在这个区块可以以某种方式处理和粘贴了。

处理子矩形并粘贴
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)
当粘贴回的时候，区块大小必须精确匹配已给的区块大小。另外，这个区块不能扩展到外部图像。但是，原始图像的模式必须和区块的模式匹配。如果他们比匹配，区块会提前动转换为匹配的模式。