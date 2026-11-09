def create_spider_plot(df, cols):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import streamlit as st
    # Load dataset


    # Select 18 columns

    # Take one row for plotting (example: first row)
    values = df.loc[0, cols].values.tolist()

    # Close the circle
    values += values[:1]

    # Create angles
    angles = np.linspace(0, 2 * np.pi, len(cols), endpoint=False).tolist()
    angles += angles[:1]

    # Create radar plot
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    ax.plot(angles, values, linewidth=2, color='blue')
    ax.fill(angles, values, color='skyblue', alpha=0.4)

    # Labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(cols, fontsize=9)

    # Title
    #plt.title("Spider Plot for Selected 18 Features", size=14, pad=20)

    st.pyplot(fig)