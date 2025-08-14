import streamlit as st
import plotly.graph_objects as go


def show_energy_network_graph():
    # 🔗 Connexions entre transformateurs et bâtiments
    edges = [
        ("Transformer_1", "Dining"),
        ("Transformer_2", "Academic"),
        ("Transformer_2", "Library"),
        ("Transformer_2", "Facilities"),
        ("Transformer_2", "Lecture"),
        ("Transformer_2", "OLD Boys_main"),
        ("Transformer_2", "OLD Girls_main"),
        ("Transformer_3", "Boys_main"),
        ("Transformer_3", "Girls_main"),
    ]

    # 📌 Positions manuelles (x, y) pour le placement du graphe
    positions = {
        "Transformer_1": (0, 2),
        "Dining": (1, 2.2),

        "Transformer_2": (0, 0),
        "Academic": (1, 1),
        "Library": (1.2, 0.5),
        "Facilities": (1.4, 0),
        "Lecture": (1.6, -0.5),
        "OLD Boys_main": (1, -1),
        "OLD Girls_main": (1.3, -1.5),

        "Transformer_3": (0, -3),
        "Boys_main": (2, -2.8),
        "Girls_main": (2.3, -3.2),
    }

    # 🔹 Création des lignes (edges)
    edge_x, edge_y = [], []
    for src, dst in edges:
        x0, y0 = positions[src]
        x1, y1 = positions[dst]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='gray'),
        hoverinfo='none',
        mode='lines'
    )

    # 📈 Création des noeuds
    nodes = list(positions.keys())
    node_x = [positions[n][0] for n in nodes]
    node_y = [positions[n][1] for n in nodes]
    node_text = nodes

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=node_text,
        textposition="bottom center",
        hoverinfo='text',
        marker=dict(
            showscale=False,
            color=['yellow' if 'Transformer' in n else 'lightblue' for n in nodes],
            size=30,
            line_width=2
        )
    )

    # 📊 Construction de la figure
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title=dict(
                            text="",
                            font=dict(size=1),
                            x=0.5
                        ),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, visible=False),
                        yaxis=dict(showgrid=False, zeroline=False, visible=False)
                    ))

    st.plotly_chart(fig, use_container_width=True)
