from IPython.display import Image, HTML

def get_caption_text(image_filename):
    image_number = image_filename.split('fig')[1]
    caption_text = image_filename[0].upper() + image_filename[1:3] + f'.{image_number}'
    
    return caption_text

def load_image(name=None):
    caption_text = get_caption_text(name)
    html_string = f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 300px;">
        <img src="Images/{name}.png" style="width: 562px; height: 300px;">
        <div style="position: absolute; top: 0px; right: 200px; color: black; font-size: 14px; background-color: rgba(255, 255, 255, 0.7); padding:           5px; border-radius: 5px;">
            {caption_text}
        </div>
    </div>
    """
    return HTML(html_string)