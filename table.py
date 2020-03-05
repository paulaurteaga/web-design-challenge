import pandas as pd
csv=pd.read_csv("Resources/cities.csv")
pd=pd.DataFrame(csv)
html_table=pd.to_html("table.html")
