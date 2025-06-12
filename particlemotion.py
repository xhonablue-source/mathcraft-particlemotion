import streamlit as st
import time
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="MathCraft: Particle Collisions & Base Ten Physics", layout="centered")

# Header
st.markdown("""
<div style='text-align: center; padding: 1rem;'>
    <h1 style='font-size: 3em; color: #f97316;'>🔬 MathCraft: Particle Collisions & Base Ten Physics</h1>
    <p style='font-size: 1.5em; font-weight: bold;'>by Xavier Honablue, M.Ed.</p>
    <p style='color: gray; font-size: 0.9em;'>All rights reserved. | Powered by lessons on motion, powers of 10, and scientific reasoning</p>
</div>
""", unsafe_allow_html=True)

# Intro physics concept
st.subheader("🎯 Concept Introduction: Opposing Motion & Forces")
st.markdown("""
Imagine two particles launched from opposite sides of a collider tube. One from the left, one from the right. They're both accelerating *toward each other*. Just like two trains in opposite motion.

This models **Newton’s Laws** and conservation of momentum. Scientists calculate when/where they meet using similar math to relative speed in train problems.
""")

# Choose direction
scenario = st.radio("Choose your particle motion setup:", ["Opposite Directions", "Same Direction"])

# Inputs
particleA_speed = st.slider("Particle A Speed (m/s)", 1, 1000000, 100000)
particleB_speed = st.slider("Particle B Speed (m/s)", 1, 1000000, 200000)
initial_distance = st.slider("Initial Distance Between (meters)", 100, 10000000, 1000000)

# Scientific notation helper
st.markdown("""
### 🧪 Scientific Notation Refresher
Scientific notation expresses very large or very small numbers using powers of 10. Examples:
- 1,000 = $1 \times 10^3$
- 300,000 m/s = $3 \times 10^5$ m/s

Try expressing your speed values in scientific notation!
""")

# Relative speed math
if scenario == "Opposite Directions":
    relative_speed = particleA_speed + particleB_speed
    meeting_time = initial_distance / relative_speed
    st.success(f"⏱️ Particles will collide after {meeting_time:.2e} seconds.")
else:
    if particleB_speed <= particleA_speed:
        st.error("Particle B must be faster to catch up to Particle A.")
        meeting_time = None
    else:
        relative_speed = particleB_speed - particleA_speed
        meeting_time = initial_distance / relative_speed
        st.success(f"⏱️ Collision will occur after {meeting_time:.2e} seconds.")

# Visualization
if meeting_time:
    st.markdown("### 🧲 Collision Animation")
    anim = st.empty()
    total_time = meeting_time + meeting_time * 0.1
    steps = int(total_time * 10)

    for t in range(steps):
        t_sec = t / 10.0
        posA = particleA_speed * t_sec
        posB = initial_distance - particleB_speed * t_sec

        if scenario == "Same Direction":
            posB = particleB_speed * t_sec
            posA = particleA_speed * t_sec

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[posA], y=[1], mode='markers+text', marker=dict(size=20), text=["Particle A"]))
        fig.add_trace(go.Scatter(x=[posB], y=[-1], mode='markers+text', marker=dict(size=20), text=["Particle B"]))

        fig.update_layout(title=f"Time: {t_sec:.1f} s", xaxis=dict(title="Position (m)"), yaxis=dict(visible=False), height=300)
        anim.plotly_chart(fig)
        time.sleep(0.05)

# Base 10 Practice Section
st.markdown("---")
st.subheader("🔢 Practice: Powers of Ten")
st.markdown("""
Convert each value to scientific notation:
- Speed of light: 299,792,458 m/s
- Diameter of an atom: 0.0000001 m
- Earth-Sun Distance: 149,600,000 km
""")

with st.expander("💡 Answer Key"):
    st.markdown("""
    - $2.9979 \times 10^8$ m/s
    - $1 \times 10^{-7}$ m
    - $1.496 \times 10^8$ km
    """, unsafe_allow_html=True)

# Forces context
st.subheader("💥 Forces Behind Opposing Motion")
st.markdown("""
Particles move in opposite directions due to **magnetic fields**, **electrostatic forces**, or initial launch force. In large colliders (like the LHC), particles are accelerated to high speeds and collided to study fundamental forces.

You can model this with the math you learned in **train problems**: calculate distance, relative speed, and meeting point.
""")

# Footer
st.markdown("""
---
<center style='font-size: 0.85em; color: gray;'>
Built with 💡 by Xavier Honablue, M.Ed. | MathCraft Series | All rights reserved.
</center>
""", unsafe_allow_html=True)

