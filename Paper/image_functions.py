from IPython.display import Image, HTML
import matplotlib.pyplot as plt

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

def k_relative_num_table(number, figure):
    html_table = f"""
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%;">
        <h3>Sign of $k$ relative to {number}</h3>
        <table border="1" style="border-collapse: collapse; text-align: center; width: 70%; font-size: 13px;">
            <tr>
                <th></th>
                <th>$k<{number}$</th>
                <th>$k={number}$</th>
                <th>$k>{number}$</th>
                 
            </tr>
            <tr>
                <th>$\\frac{{k-{number}}}{{|E_{{(k-{number})}}|}}$</th>
                <td>-1</td>
                <td>$0$</td>
                <td>$1$</td>         
            </tr>
        </table>
        Fig.{figure}
    </div>
    """
    return display(HTML(html_table))

def k_relative_to_ordinate_axis_table():
    html_table = r"""
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%;">
        <h3>$k$ relative to ordinate axis</h3>
        <table border="1" style="border-collapse: collapse; text-align: center; width: 85%; font-size: 13px;">
            <tr>
                <th>$K$</th>
                <th>$0 \leq k < 1$</th>
                <th>$ k = 1 $</th>
                <th>$1 < k < 3$</th>
                <th>$k=3$</th>
                <th>$ 3 < k $</th>
                 
            </tr>
  
                <th>$\lfloor \frac{1+\frac{(k-1)(k-3)}{E_{((k-1)(k-3))}}}{2} \rfloor$</th>
                <th>$1$</th>
                <th>$0$</th>
                <th>$0$</th>
                <th>$0$</th>
                <th>$1$</th>                
            </tr>


        </table>
        Fig.77
    </div>
    """
    return display(HTML(html_table))

def kl_match_table():
    html_table = r"""
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%;">
        <h3>$kl$ match</h3>
        <table border="1" style="border-collapse: collapse; text-align: center; width: 85%; font-size: 13px;">
            <tr>
                <th></th>
                <th>$0 \leq k < 1$</th>
                <th>$ k = 1 $</th>
                <th>$1 < k < 3$</th>
                <th>$k=3$</th>
                <th>$ 3 < k $</th>
                 
            </tr>
                <th>$x_l<0$</th>
                <th>$0$</th>
                <th>$0$</th>
                <th>$1$</th>
                <th>$0$</th>
                <th>$0$</th>
                
            </tr>
            </tr>
                <th>$x_l=0$</th>
                <th>$0$</th>
                <th>$0$</th>
                <th>$0$</th>
                <th>$0$</th>
                <th>$0$</th>
                
            </tr>
            </tr>
                <th>$x_l>0$</th>
                <th>$1$</th>
                <th>$0$</th>
                <th>$0$</th>
                <th>$0$</th>
                <th>$1$</th>
                
            </tr>


        </table>
        Fig.78
    </div>
    """
    return display(HTML(html_table))

def expression_a_table():
    html_table = r"""
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%;">
        <h3>$Expression A$</h3>
        <table border="1" style="border-collapse: collapse; text-align: center; width: 85%; font-size: 13px;">
            <tr>
                <th></th>
                <th>$\omega < 0 $</th>
                <th>$ \omega = 0 $</th>
                <th>$\omega > 0 $</th>

                 
            </tr>
                <th>$x_l<0$</th>
                <th>$0$</th>
                <th>$1$</th>
                <th>$1$</th>

                
            </tr>
            </tr>
                <th>$x_l=0$</th>
                <th>$1$</th>
                <th>$0$</th>
                <th>$1$</th>

                
            </tr>
            </tr>
                <th>$x_l>0$</th>
                <th>$1$</th>
                <th>$1$</th>
                <th>$0$</th>

                
            </tr>


        </table>
        Fig.89
    </div>
    """
    return display(HTML(html_table))

def expression_b_table():
    html_table = r"""
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%;">
        <h3>$Expression B$</h3>
        <table border="1" style="border-collapse: collapse; text-align: center; width: 85%; font-size: 13px;">
            <tr>
                <th></th>
                <th>$\omega < 0 $</th>
                <th>$ \omega = 0 $</th>
                <th>$\omega > 0 $</th>

                 
            </tr>
                <th>$x_l<0$</th>
                <th>$1$</th>
                <th>$1$</th>
                <th>$0$</th>

                
            </tr>
            </tr>
                <th>$x_l=0$</th>
                <th>$1$</th>
                <th>$0$</th>
                <th>$1$</th>

                
            </tr>
            </tr>
                <th>$x_l>0$</th>
                <th>$0$</th>
                <th>$1$</th>
                <th>$1$</th>

                
            </tr>


        </table>
        Fig.90
    </div>
    """
    return display(HTML(html_table))

def XMD_table():
    html_table = r"""
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%;">
        <h3>X Maximum Distance</h3>
        <table border="1" style="border-collapse: collapse; text-align: center; width: 80%; font-size: 13px;">
            <tr>
                <th></th>
                <th>$|y_s(t_{[1; 0]})| > |x_l|$</th>
                <th>$|y_s(t_{[1; 0]})| \le |x_l|$</th>

                 
            </tr>
            <tr>
                <th>$\lfloor 
\frac{1+\frac{|y_s(t_{[1; 0]})| - |x_l|}{ E_{\left( |y_s(t_{[1; 0]})| - |x_l| \right)}}}
{2}
\rfloor$</th>
                <td>$1$</td>
                <td>$0$</td>

         
            </tr>

        </table>
        Fig.122
    </div>
    """
    return display(HTML(html_table))

def rotational_coeff_table():
    html_table = """
    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%;">
        <h3>Rotational Coefficient Table</h3>
        <table border="1" style="border-collapse: collapse; text-align: center; width: 50%; font-size: 13px;">
            <tr>
                <th></th>
                <th>$b$</th>
                <th>$x_l$</th>
                <th>$-bx_l$</th>
       
            </tr>
            <tr>
                <th>$Fig.173$</th>
                <td>$1$</td>
                <td>$1$</td>
                <td>$-1$</td>
      
            </tr>
            <tr>
                <th>$Fig.174$</th>
                <td>$1$</td>
                <td>$-1$</td>
                <td>$1$</td>
                <td>$1$</td>
       
            </tr>
            <tr>
                <th>$Fig.175$</th>
                <td>$1$</td>
                <td>$-1$</td>
                <td>$1$</td>
         
            </tr>
            <tr>
                <th>$Fig.176$</th>
                <td>$-1$</td>
                <td>$-1$</td>
                <td>$-1$</td>
          
            </tr>
        </table>
        Fig.177
    </div>
    """
    return display(HTML(html_table))

def show_number_line(a, b=None, c=None, d=None):

    fig, ax = plt.subplots(figsize=(8, 1))  
    ax.axhline(0, color='black', linewidth=1)  


    positions = list(range(-5, 6))  
    

    labels = []  
    
    for i in range(len(positions)):
        if positions[i] == a:
            if b is None:
                labels.append(1)
            else:
                labels.append(b)
            

            
        elif c is not None and positions[i] == c:
            labels.append(d)
            
        else:
            labels.append(positions[i])


    ax.set_xticks(positions)
    ax.set_xticklabels(labels)

    ax.set_yticks([])  
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.show()
    
def E(x):
    return x ** (1 - 0 ** abs(x))

def sign_func(x,a,b=None):
    if b is None:
        return (x-a)/abs(E(x-a))
    prod = (x-a)*(x-b)
    return prod/abs(E(prod))

def show_sign_func_number_line(a, b=None):

    fig, ax = plt.subplots(figsize=(8, 1))  
    ax.axhline(0, color='black', linewidth=1)  


    positions = list(range(-5, 6))  
    

    labels = []  
    
    for i in range(len(positions)):
        n = positions[i]
        if b is None:        
            labels.append(int(abs(n) * sign_func(n,a)))
        else:
            labels.append(int(abs(n) * sign_func(n,a,b)))

    ax.set_xticks(positions)
    ax.set_xticklabels(labels)

    ax.set_yticks([])  
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.show()
