from typing import List

import plotly.graph_objects as go
from chromatopy.core import Measurement


def plot_measurments(measurements: List[Measurement]):
    # Example setup for calibration_meas; you should replace this with your actual data access code.
    # Assume calibration_meas is a list where each item has a 'chromatograms' list,
    # and each chromatogram has 'times' and 'signals'.

    # Create a 3D plot using Plotly
    fig = go.Figure()

    y_offset = 0  # Starting point for y-axis to separate chromatograms
    for meas in measurements:
        chromatogram = meas.chromatograms[
            0
        ]  # Assuming each measurement has at least one chromatogram
        x = chromatogram.times
        y = [y_offset] * len(x)  # All y values are the same for one chromatogram
        z = chromatogram.signals

        # Adding each chromatogram as a 3D scatter plot to the figure
        fig.add_trace(
            go.Scatter3d(x=x, y=y, z=z, mode="lines", name=f"Chromatogram {y_offset+1}")
        )

        # Increment y_offset for the next chromatogram
        y_offset += 1  # Adjust this value as needed to separate chromatograms

    # Update plot layout
    fig.update_layout(
        title="3D Chromatogram Plot",
        scene=dict(
            xaxis_title="Time",
            yaxis_title="Injection Number",
            zaxis_title=f"A.U. {measurements[0].chromatograms[0].wavelength} nm",
        ),
        margin=dict(l=0, r=0, b=0, t=30),  # Adjust margins to fit layout
    )

    # Show the plot
    fig.show()
