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
        <div style="position: absolute; top: 0px; right: 80px; color: black; font-size: 14px; background-color: rgba(255, 255, 255, 0.7); padding:           5px; border-radius: 5px;">
            {caption_text}
        </div>
    </div>
    """
    return HTML(html_string)

def load_images(images):
    html_string = "<div style='display: flex; justify-content: space-between;'>"
    for name, position in images:
        caption_text = get_caption_text(name)
        html_string += f"""
        <div style="text-align: center; margin: 0 10px;">
            <img src="Images/{name}.png" style="width: 375px; height: 200px;">
            <div style="color: black; font-size: 14px; background-color: rgba(255, 255, 255, 0.7); padding: 5px; border-radius: 5px;">
                {caption_text}
            </div>
        </div>
        """
    html_string += "</div>"
    return HTML(html_string)

def wxy_table():
    html_table = """
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%;">
        <h3>Table of Signs</h3>
        <table border="1" style="border-collapse: collapse; text-align: center; width: 50%; font-size: 13px;">
            <tr>
                <th></th>
                <th>$\\omega$</th>
                <th>$x_l$</th>
                <th>$y_s(t)$</th>
                <th>$\\Delta \\phi$</th>        
            </tr>
            <tr>
                <th>$Fig.17$</th>
                <td>$1$</td>
                <td>$-1$</td>
                <td>$1$</td>
                <td>$1$</td>
            </tr>
            <tr>
                <th>$Fig.18$</th>
                <td>$-1$</td>
                <td>$-1$</td>
                <td>$1$</td>
                <td>$-1$</td>
            </tr>
            <tr>
                <th>$Fig.19$</th>
                <td>$1$</td>
                <td>$-1$</td>
                <td>$-1$</td>
                <td>$-1$</td>
            </tr>
            <tr>
                <th>$Fig.20$</th>
                <td>$-1$</td>
                <td>$1$</td>
                <td>$-1$</td>
                <td>$-1$</td>
            </tr>
        </table>
        Fig.21
    </div>
    """
    return display(HTML(html_table))

def intervals_table():
    html_table = r"""
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%;">
        <h3>Table of Intervals</h3>
        <table border="1" style="border-collapse: collapse; text-align: center; width: 70%; font-size: 13px;">
            <tr>
                <th>Interval</th>
                <th>$$(-\infty; x_{pr})$$</th>
                <th>$(x_{pr};x_{pmd})$</th>
                <th>$(x_{pmd};0)$</th>
                 
            </tr>
            <tr>
                <th>$S_{(|x_l| - |x_s(t_{[n; m-1]})|)}$</th>
                <td>1</td>
                <td>$-1$</td>
                <td>$-1;1$</td>
         
            </tr>
            <tr>
                <th>$\left\{ t_{[n; m]} \right\}$</th>
                <td>$\text{Monotonically } \nearrow$</td>
                <td>$\text{Monotonically } \searrow$</td>
                <td>$\text{Oscillating } \sim$</td>
              
            </tr>
     
         
        </table>
        Fig.49
    </div>
    """
    return display(HTML(html_table))