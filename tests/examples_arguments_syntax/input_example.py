"""
Interactive chart using the input element
============================
This is an example of a horizontal stacked bar chart using data which contains crop yields over different regions and different years in the 1930s.
"""
# category: interactive charts

import altair as alt
from vega_datasets import data

search_input = alt.selection_point(
    fields=['Name'],
    empty=False,  # Start with no points selected
    bind=alt.binding(
        input='text',  # Change this to any of the options at https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types
        placeholder="Car model",
        name='Search ',
    )
)
alt.Chart(data.cars.url).mark_point(size=60).encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    tooltip='Name:N',
    opacity=alt.condition(  # This condition would also need to be updated accordingly
        search_input,
        alt.value(1),
        alt.value(0.05)
    )
).add_params(
    search_input
)