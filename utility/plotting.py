from typing import List

import plotly.graph_objects as go
from chromatopy.core import Measurement


def plot_measurements(measurements: List[Measurement]):
    # Create a 2D plot using Plotly
    fig = go.Figure()

    for meas in measurements:
        chromatogram = meas.chromatograms[
            0
        ]  # Assuming each measurement has at least one chromatogram
        x = chromatogram.times
        z = chromatogram.signals

        # Adding each chromatogram as a 2D line plot to the figure
        fig.add_trace(
            go.Scatter(
                x=x,
                y=z,
                mode="lines",  # Line plot
                name=f"{meas.id} ({chromatogram.wavelength} nm)",
                opacity=1,  # Set full opacity for all traces
            )
        )

    # Update plot layout
    fig.update_layout(
        title="Chromatogram Plot",
        xaxis_title="Time (min)",
        yaxis_title="Absorbance",
        margin=dict(l=0, r=0, b=0, t=30),  # Adjust margins to fit layout
        plot_bgcolor="white",  # Set background to white for better visibility
    )

    # Show the plot
    fig.show()
