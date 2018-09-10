from PIL import Image

bmpFile = Image.open(r'bmp/FLAG_B24.BMP')
`
['BITFIELDS', 'COMPRESSIONS', 'JPEG', 'PNG', 'RAW', 'RLE4', 'RLE8', '_Image__transformer', '__array_interface__', '__class__', '__copy__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bitmap', '_close_exclusive_fp_after_loading', '_copy', '_crop', '_dump', '_ensure_mutable', '_exclusive_fp', '_expand', '_min_frame', '_new', '_open', '_repr_png_', '_seek_check', 'alpha_composite', 'category', 'close', 'convert', 'copy', 'crop', 'decoderconfig', 'decodermaxblock', 'draft', 'effect_spread', 'filename', 'filter', 'format', 'format_description', 'fp', 'frombytes', 'fromstring', 'get_format_mimetype', 'getbands', 'getbbox', 'getchannel', 'getcolors', 'getdata', 'getextrema', 'getim', 'getpalette', 'getpixel', 'getprojection', 'height', 'histogram', 'im', 'info', 'load', 'load_end', 'load_prepare', 'mode', 'offset', 'palette', 'paste', 'point', 'putalpha', 'putdata', 'putpalette', 'putpixel', 'pyaccess', 'quantize', 'readonly', 'remap_palette', 'resize', 'rotate', 'save', 'seek', 'show', 'size', 'split', 'tell', 'thumbnail', 'tile', 'tobitmap', 'tobytes', 'toqimage', 'toqpixmap', 'tostring', 'transform', 'transpose', 'verify', 'width']
`
bmpFile.format, bmpFile.size, bmpFile.mode
bmpFile.width,bmpFile.height

bmpFile.show()

bmpFile.getpixel((x,y))
