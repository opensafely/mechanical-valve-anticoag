from ebmdatalab import charts
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

def add_percentiles(df, period_column=None, column=None, show_outer_percentiles=True):
    """For each period in `period_column`, compute percentiles across that
    range.
    Adds `percentile` column.
    """
    deciles = np.arange(0.1, 1, 0.1)
    bottom_percentiles = np.arange(0.01, 0.1, 0.01)
    top_percentiles = np.arange(0.91, 1, 0.01)
    if show_outer_percentiles:
        quantiles = np.concatenate((deciles, bottom_percentiles, top_percentiles))
    else:
        quantiles = deciles
    df = df.groupby(period_column)[column].quantile(quantiles).reset_index()
    df = df.rename(index=str, columns={"level_1": "percentile"})
    # create integer range of percentiles
    df["percentile"] = df["percentile"].apply(lambda x: int(x * 100))
    return df


def deciles_chart(
    df,
    period_column=None,
    column=None,
    title="",
    ylabel="", interactive=True
):
    """period_column must be dates / datetimes
    """

    df = add_percentiles(
        df,
        period_column=period_column,
        column=column,
        show_outer_percentiles=False,
    )

    if interactive:
        fig = go.Figure()

        

        for percentile in np.unique(df['percentile']):
            df_subset = df[df['percentile'] == percentile]
            if percentile == 50:
                fig.add_trace(go.Scatter(x=df_subset[period_column], y=df_subset[column], line={
                            "color": "blue", "dash": "solid", "width": 1.2}, name="median"))
            else:
                fig.add_trace(go.Scatter(x=df_subset[period_column], y=df_subset[column], line={
                            "color": "blue", "dash": "dash", "width": 1}, name=f"decile {int(percentile/10)}"))

        # Set title
        fig.update_layout(
            title_text=title,
            hovermode='x',
            title_x=0.5,


        )

        fig.update_yaxes(title=ylabel)
        fig.update_xaxes(title="Date")

        # Add range slider
        fig.update_layout(
            xaxis=go.layout.XAxis(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                            label="1m",
                            step="month",
                            stepmode="backward"),
                        dict(count=6,
                            label="6m",
                            step="month",
                            stepmode="backward"),

                        dict(count=1,
                            label="1y",
                            step="year",
                            stepmode="backward"),
                        dict(step="all")
                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                type="date"
            )
        )

        fig.show()
    else:

       charts.deciles_chart(
        df,
        period_column=period_column,
        column=column,
        title=title,
        ylabel=ylabel,
        show_outer_percentiles=False,
        show_legend=True,
    ) 