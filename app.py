import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.mock_data import generate_mock_songs

st.set_page_config(
    page_title="Song Success Predictor",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open('assets/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    st.markdown(
        """
        <div class="hero-section">
            <div style="position: relative; z-index: 1;">
                <p style="font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.15em; color: rgba(255,255,255,0.5); font-weight: 600; margin-bottom: 1rem;">AI-Powered Music Intelligence</p>
                <h1 class="hero-title">Song Success Predictor</h1>
                <p class="hero-subtitle">Predict your song's streaming and social media success with real-time crowd sentiment analysis and AI-powered insights</p>
                <div style="margin-top: 1.5rem; display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem;">
                    <span class="hero-badge">📊 Real-time Analytics</span>
                    <span class="hero-badge">🤖 AI Predictions</span>
                    <span class="hero-badge">🎭 Sentiment Analysis</span>
                    <span class="hero-badge">📈 Viral Tracking</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-header">🚀 Supported Platforms</div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    platforms = [
        {"name": "Spotify", "icon": "🎵", "color": "#1DB954", "desc": "Streaming Analytics", "shadow": "rgba(29, 185, 84, 0.15)"},
        {"name": "TikTok", "icon": "🎬", "color": "#FF0050", "desc": "Viral Potential", "shadow": "rgba(255, 0, 80, 0.15)"},
        {"name": "Apple Music", "icon": "🍎", "color": "#FA57C1", "desc": "Premium Market", "shadow": "rgba(250, 87, 193, 0.15)"},
        {"name": "YouTube", "icon": "📺", "color": "#FF0000", "desc": "Video Engagement", "shadow": "rgba(255, 0, 0, 0.15)"}
    ]

    for col, p in zip([col1, col2, col3, col4], platforms):
        with col:
            st.markdown(
                f"""
                <div class="platform-card" style="box-shadow: 0 8px 24px {p['shadow']};">
                    <div class="platform-icon">{p['icon']}</div>
                    <div class="platform-name" style="color: {p['color']};">{p['name']}</div>
                    <div class="platform-desc">{p['desc']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    mock_songs = generate_mock_songs()

    st.markdown('<div class="section-header">📈 Top Performing Songs</div>', unsafe_allow_html=True)

    top_songs = mock_songs.nlargest(3, 'viral_score')
    cols = st.columns(3)

    medals = ["🥇", "🥈", "🥉"]

    for idx, (_, song) in enumerate(top_songs.iterrows()):
        with cols[idx]:
            score = song['viral_score']
            spotify = song['spotify_potential']
            tiktok = song['tiktok_potential']
            st.markdown(
                f"""
                <div class="success-card" style="min-height: 220px;">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.2rem;">
                        <div>
                            <div style="font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.4); font-weight: 600; margin-bottom: 0.3rem;">{medals[idx]} Rank #{idx+1}</div>
                            <h3 style="color: var(--text-primary); margin: 0 0 0.3rem 0; font-size: 1.1rem; font-weight: 700;">{song['title']}</h3>
                            <p style="color: var(--text-muted); margin: 0; font-size: 0.85rem;">by {song['artist']}</p>
                        </div>
                        <div style="text-align: right;">
                            <div style="font-size: 1.6rem; font-weight: 800; background: linear-gradient(135deg, #1DB954, #1ed760); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{score:.0f}%</div>
                            <div style="font-size: 0.7rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em;">Viral Score</div>
                        </div>
                    </div>
                    <div style="margin-bottom: 1rem;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.4rem;">
                            <span style="color: var(--text-muted); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em;">Success Progress</span>
                            <span style="color: var(--text-secondary); font-size: 0.75rem; font-weight: 600;">{song['genre']}</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: {score}%;"></div>
                        </div>
                    </div>
                    <div style="display: flex; gap: 1rem; font-size: 0.8rem;">
                        <div style="flex: 1; padding: 0.5rem; background: rgba(29, 185, 84, 0.06); border-radius: 8px; text-align: center;">
                            <div style="color: #1DB954; font-weight: 700;">{spotify:.0f}%</div>
                            <div style="color: var(--text-muted); font-size: 0.7rem;">Spotify</div>
                        </div>
                        <div style="flex: 1; padding: 0.5rem; background: rgba(255, 0, 80, 0.06); border-radius: 8px; text-align: center;">
                            <div style="color: #FF0050; font-weight: 700;">{tiktok:.0f}%</div>
                            <div style="color: var(--text-muted); font-size: 0.7rem;">TikTok</div>
                        </div>
                        <div style="flex: 1; padding: 0.5rem; background: rgba(250, 87, 193, 0.06); border-radius: 8px; text-align: center;">
                            <div style="color: #FA57C1; font-weight: 700;">{song['apple_potential']:.0f}%</div>
                            <div style="color: var(--text-muted); font-size: 0.7rem;">Apple</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-header">📊 Platform Analytics</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    stats = [
        {"title": "Spotify Success", "value": f"{mock_songs['spotify_potential'].mean():.1f}%", "icon": "🎵", "color": "#1DB954", "change": "+12.3%"},
        {"title": "TikTok Viral", "value": f"{mock_songs['tiktok_potential'].mean():.1f}%", "icon": "🎬", "color": "#FF0050", "change": "+8.7%"},
        {"title": "Viral Score", "value": f"{mock_songs['viral_score'].mean():.1f}%", "icon": "🚀", "color": "#1DA1F2", "change": "+15.2%"},
        {"title": "Songs Analyzed", "value": f"{len(mock_songs)}", "icon": "📊", "color": "#FA57C1", "change": "+23 new"}
    ]

    for col, stat in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(
                f"""
                <div class="stat-card" style="--card-accent: {stat['color']};">
                    <span class="stat-icon">{stat['icon']}</span>
                    <div class="stat-value" style="color: {stat['color']};">{stat['value']}</div>
                    <div class="stat-label">{stat['title']}</div>
                    <div class="stat-change">{stat['change']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-header">🎸 Genre Performance</div>', unsafe_allow_html=True)

    genre_trends = mock_songs.groupby('genre').agg({
        'viral_score': 'mean',
        'spotify_potential': 'mean',
        'tiktok_potential': 'mean'
    }).reset_index()
    genre_trends = genre_trends.sort_values('viral_score', ascending=True)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=genre_trends['genre'],
        x=genre_trends['viral_score'],
        orientation='h',
        name='Viral Score',
        marker=dict(
            color=genre_trends['viral_score'],
            colorscale=[[0, '#1a1a2e'], [0.5, '#1DB954'], [1, '#1ed760']],
            line=dict(color='rgba(255,255,255,0.05)', width=1),
            cornerradius=6
        ),
        text=[f'{v:.1f}%' for v in genre_trends['viral_score']],
        textposition='outside',
        textfont=dict(color='rgba(255,255,255,0.7)', size=12, family='Inter')
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='rgba(255,255,255,0.7)', size=12, family='Inter'),
        title=None,
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.04)',
            title=None,
            zeroline=False
        ),
        yaxis=dict(
            title=None,
            tickfont=dict(size=13, color='rgba(255,255,255,0.8)')
        ),
        margin=dict(l=10, r=40, t=10, b=10),
        height=320,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        fig_scatter = go.Figure()
        fig_scatter.add_trace(go.Scatter(
            x=mock_songs['energy'],
            y=mock_songs['viral_score'],
            mode='markers',
            marker=dict(
                size=mock_songs['danceability'] * 20 + 4,
                color=mock_songs['viral_score'],
                colorscale=[[0, '#1a1a2e'], [0.3, '#1DA1F2'], [0.6, '#1DB954'], [1, '#1ed760']],
                line=dict(width=1, color='rgba(255,255,255,0.1)'),
                opacity=0.8
            ),
            text=[f"{row['title']}<br>Viral: {row['viral_score']:.0f}%" for _, row in mock_songs.iterrows()],
            hoverinfo='text'
        ))

        fig_scatter.update_layout(
            title=dict(text='Energy vs Viral Score', font=dict(size=14, color='rgba(255,255,255,0.8)', family='Inter'), x=0),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='rgba(255,255,255,0.6)', family='Inter'),
            xaxis=dict(title='Energy', showgrid=True, gridcolor='rgba(255,255,255,0.04)', zeroline=False),
            yaxis=dict(title='Viral Score', showgrid=True, gridcolor='rgba(255,255,255,0.04)', zeroline=False),
            margin=dict(l=10, r=10, t=40, b=10),
            height=340
        )

        st.plotly_chart(fig_scatter, use_container_width=True)

    with col2:
        genre_radar = mock_songs.groupby('genre').agg({
            'energy': 'mean',
            'danceability': 'mean',
            'valence': 'mean',
            'viral_score': lambda x: x.mean() / 100
        }).reset_index()

        fig_radar = go.Figure()
        colors = ['#1DB954', '#FF0050', '#1DA1F2', '#FA57C1', '#FFD700', '#FF6B9D']

        for i, (_, row) in enumerate(genre_radar.iterrows()):
            fig_radar.add_trace(go.Scatterpolar(
                r=[row['energy'], row['danceability'], row['valence'], row['viral_score']],
                theta=['Energy', 'Danceability', 'Valence', 'Viral'],
                fill='toself',
                name=row['genre'],
                line=dict(color=colors[i % len(colors)], width=2),
                fillcolor=f'rgba({int(colors[i % len(colors)][1:3], 16)}, {int(colors[i % len(colors)][3:5], 16)}, {int(colors[i % len(colors)][5:7], 16)}, 0.08)'
            ))

        fig_radar.update_layout(
            title=dict(text='Genre Feature Profiles', font=dict(size=14, color='rgba(255,255,255,0.8)', family='Inter'), x=0),
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 1], showticklabels=False, gridcolor='rgba(255,255,255,0.06)'),
                angularaxis=dict(gridcolor='rgba(255,255,255,0.06)', tickfont=dict(color='rgba(255,255,255,0.6)'))
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='rgba(255,255,255,0.6)', family='Inter'),
            legend=dict(font=dict(size=11), bgcolor='rgba(0,0,0,0)'),
            margin=dict(l=40, r=40, t=40, b=40),
            height=340
        )

        st.plotly_chart(fig_radar, use_container_width=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="cta-section">
            <div style="position: relative; z-index: 1;">
                <h2 style="color: var(--text-primary); margin-bottom: 0.5rem; font-size: 1.8rem; font-weight: 800; letter-spacing: -0.02em;">Ready to Analyze Your Song?</h2>
                <p style="color: var(--text-secondary); font-size: 1rem; margin-bottom: 2rem; max-width: 500px; margin-left: auto; margin-right: auto;">Get detailed AI-powered insights about your song's potential across all major platforms</p>
                <div style="display: flex; justify-content: center; gap: 0.8rem; flex-wrap: wrap;">
                    <span class="cta-btn" style="background: linear-gradient(135deg, #1DB954, #1ed760);">🎵 Upload Song</span>
                    <span class="cta-btn" style="background: linear-gradient(135deg, #1DA1F2, #4FC3F7);">📊 Analyze Features</span>
                    <span class="cta-btn" style="background: linear-gradient(135deg, #FF6B9D, #FF8E98);">📈 View Trends</span>
                    <span class="cta-btn" style="background: linear-gradient(135deg, #9C27B0, #E040FB);">🎭 Sentiment</span>
                    <span class="cta-btn" style="background: linear-gradient(135deg, #667eea, #764ba2);">🚀 Dashboard</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
