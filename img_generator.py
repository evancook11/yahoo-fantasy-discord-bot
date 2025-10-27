from selenium import webdriver
from selenium.webdriver.common.by import By
import tempfile
from models import Table

def create_html_table(table: Table) -> str:
    header_string = "".join([f"<th>{header}</th>" for header in table.header])
    value_strings = []
    for row in table.entries:
        row_string = "<tr>" + "".join([f"<td>{value}</td>" for value in row]) + "</tr>"
        value_strings.append(row_string)

    value_strings = "".join(value_strings)

    html_string = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}

            table {{
                padding: 12px;
            }}
        </style>
    </head
    <body>
        <table id='table'>
            <thead>
                <tr>{header_string}</tr>
            </thead>
            <tbody>
                {value_strings}
            </tbody>
        </table>
    </body>
    </html>
    """
    return html_string
def html_to_image(html: str) -> str:
    """Takes an html string and returns the path of the generated image"""
    
    with tempfile.NamedTemporaryFile(delete_on_close=False, suffix=".html", mode="w") as temp_html:
        temp_html.write(html)
        temp_html.close()
        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument('--headless')
        driver = webdriver.Chrome(driver_options)
        driver.get(f"file://{temp_html.name}")
        driver.implicitly_wait(1)
        table = driver.find_element(By.ID, 'table')
        
        temp_png = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        temp_png.close()

        table.screenshot(temp_png.name)
        driver.quit()
    return temp_png.name

