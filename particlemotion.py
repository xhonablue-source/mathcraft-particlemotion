import streamlit as st
import time
import plotly.graph_objects as go
import numpy as np

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

# Interactive Base Ten Demonstration Section
st.markdown("---")
st.subheader("🎯 Interactive Base Ten Powers Demo: From Meters to Atoms")
st.markdown("""
**Key Concept**: When we write fractions like 1/10, 1/100, or 1/10,000,000 - each fraction is **always relative to the original whole meter**, not to previous subdivisions.

Let's explore this step by step:
""")

# Interactive slider for powers of 10
power_selection = st.slider("Select Power of 10 (negative exponent)", -10, 0, -3, 1)
selected_value = 10 ** power_selection

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    ### 📏 Current Selection:
    **10^{power_selection}** = **{selected_value}** meters
    
    **Fraction form**: 1/{int(1/selected_value):,} of a meter
    
    **Scientific notation**: {selected_value:.0e} meters
    """)

with col2:
    # Visual scale comparison
    scale_examples = {
        0: "🏠 1 meter (about 3 feet - door height)",
        -1: "✋ 0.1 meter (10 cm - hand width)", 
        -2: "🔘 0.01 meter (1 cm - fingernail)",
        -3: "📍 0.001 meter (1 mm - pinhead)",
        -4: "🦠 0.0001 meter (0.1 mm - bacteria)",
        -5: "⚡ 0.00001 meter (10 μm - cell)",
        -6: "🧬 0.000001 meter (1 μm - virus)",
        -7: "⚛️ 0.0000001 meter (100 nm - atom)",
        -8: "🔬 0.00000001 meter (10 nm - molecule)",
        -9: "⚡ 0.000000001 meter (1 nm - quantum scale)",
        -10: "🌌 0.0000000001 meter (0.1 nm - subatomic)"
    }
    
    st.markdown(f"### 🔍 Scale Reference:")
    st.markdown(f"**{scale_examples.get(power_selection, 'Ultra-microscopic scale')}**")

# Visual demonstration with bars
st.markdown("### 📊 Visual Scale Comparison")
powers = list(range(0, -8, -1))
values = [10**p for p in powers]
labels = [f"10^{p}" for p in powers]

fig = go.Figure()
fig.add_trace(go.Bar(
    x=labels,
    y=values,
    text=[f"{v:.0e} m" for v in values],
    textposition='auto',
    marker_color=['#f97316' if p == power_selection else '#94a3b8' for p in powers]
))

fig.update_layout(
    title="Powers of 10: Each Step is 1/10 of the Previous",
    xaxis_title="Power of 10",
    yaxis_title="Size in Meters",
    yaxis_type="log",
    height=400
)

st.plotly_chart(fig, use_container_width=True)

# Key insight box
st.info("""
💡 **Remember**: An atom at 10⁻⁷ meters is **one ten-millionth of the ORIGINAL meter** - not a fraction of any smaller piece along the way!
""")

# Comprehensive explanation section
st.markdown("---")
st.subheader("🧮 Understanding Base 10, Natural Log (ln), and e^x")

# Create tabs for different concepts
tab1, tab2, tab3, tab4 = st.tabs(["Base 10 Logs", "Natural Log (ln)", "e^x Calculator", "Physics Applications"])

with tab1:
    st.markdown("""
    ### 📊 Base 10 Logarithms (log₁₀)
    
    **What it means**: "To what power must I raise 10 to get this number?"
    
    **Examples from our particle physics:**
    """)
    
    # Interactive base 10 calculator
    base10_input = st.number_input("Enter a number to find its base 10 log:", 
                                   min_value=0.0000001, max_value=1000000000.0, 
                                   value=100000.0, format="%.7f")
    
    log10_result = np.log10(base10_input)
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**log₁₀({base10_input:g}) = {log10_result:.3f}**")
        st.markdown(f"This means: **10^{log10_result:.3f} = {base10_input:g}**")
    
    with col2:
        # Show scientific notation connection
        if base10_input >= 1:
            st.info(f"Scientific notation: **{base10_input:.2e}**")
        else:
            st.info(f"Scientific notation: **{base10_input:.2e}**")
    
    st.markdown("""
    **Real Physics Example:**
    - Atom diameter = 10⁻⁷ meters
    - log₁₀(0.0000001) = -7
    - The logarithm tells us the **power of 10** directly!
    """)

with tab2:
    st.markdown("""
    ### 🌿 Natural Logarithm (ln) - Base e
    
    **What is e?** e ≈ 2.71828... (Euler's number)
    **What ln means**: "To what power must I raise e to get this number?"
    
    **Why does e matter in physics?** Natural growth and decay processes!
    """)
    
    # Interactive natural log calculator
    ln_input = st.number_input("Enter a number to find its natural log (ln):", 
                              min_value=0.0001, max_value=1000000.0, 
                              value=100000.0, format="%.4f")
    
    ln_result = np.log(ln_input)
    e_check = np.exp(ln_result)
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**ln({ln_input:g}) = {ln_result:.3f}**")
        st.markdown(f"Check: **e^{ln_result:.3f} = {e_check:.1f}**")
    
    with col2:
        # Compare to base 10
        log10_compare = np.log10(ln_input)
        st.info(f"Compare to base 10: **log₁₀({ln_input:g}) = {log10_compare:.3f}**")
    
    st.markdown("""
    **Physics Applications:**
    - **Radioactive decay**: N(t) = N₀ × e^(-λt)
    - **Particle beam intensity**: I = I₀ × e^(-μx)
    - **Energy distribution**: f(E) ∝ e^(-E/kT)
    """)

with tab3:
    st.markdown("""
    ### 🔢 What does e^x mean on your calculator?
    
    **e^x** means "e raised to the power of x"
    - e^1 = e ≈ 2.718
    - e^2 ≈ 7.389  
    - e^0 = 1 (anything to power 0 equals 1)
    - e^(-1) = 1/e ≈ 0.368
    """)
    
    # Interactive e^x calculator
    exp_input = st.slider("Choose exponent (x) for e^x:", -5.0, 5.0, 1.0, 0.1)
    exp_result = np.exp(exp_input)
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**e^{exp_input} = {exp_result:.3f}**")
        
        # Show the relationship
        if exp_input > 0:
            st.markdown("📈 **Exponential Growth** - gets big fast!")
        elif exp_input < 0:
            st.markdown("📉 **Exponential Decay** - approaches zero")
        else:
            st.markdown("🎯 **Baseline** - e^0 = 1")
    
    with col2:
        # Visual representation
        x_vals = np.linspace(-3, 3, 100)
        y_vals = np.exp(x_vals)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='e^x'))
        fig.add_trace(go.Scatter(x=[exp_input], y=[exp_result], 
                                mode='markers', marker=dict(size=10, color='red'),
                                name=f'e^{exp_input}'))
        
        fig.update_layout(title="e^x Function", xaxis_title="x", yaxis_title="e^x", height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Calculator Connection:**
    - Look for **e^x** or **exp** button on scientific calculators
    - **ln** button does the reverse: if e^x = y, then ln(y) = x
    - They are **inverse functions**!
    """)

with tab4:
    st.markdown("""
    ### ⚛️ How These Apply to Our Particle Physics Examples
    
    Let's connect logs and exponentials to real particle collision scenarios:
    """)
    
    # Use current particle speeds from the main app
    current_speed_A = st.session_state.get('particleA_speed', 100000)
    current_speed_B = st.session_state.get('particleB_speed', 200000)
    
    st.markdown(f"""
    **Using Your Current Particle Speeds:**
    - Particle A: {current_speed_A:,} m/s
    - Particle B: {current_speed_B:,} m/s
    """)
    
    # Show logarithmic analysis
    log_speed_A = np.log10(current_speed_A)
    log_speed_B = np.log10(current_speed_B)
    ln_speed_A = np.log(current_speed_A)
    ln_speed_B = np.log(current_speed_B)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        **Base 10 Analysis:**
        - log₁₀({current_speed_A:,}) = {log_speed_A:.2f}
        - log₁₀({current_speed_B:,}) = {log_speed_B:.2f}
        
        **Meaning**: Particle A speed is 10^{log_speed_A:.2f}, 
        Particle B is 10^{log_speed_B:.2f}
        """)
    
    with col2:
        st.markdown(f"""
        **Natural Log Analysis:**
        - ln({current_speed_A:,}) = {ln_speed_A:.2f}
        - ln({current_speed_B:,}) = {ln_speed_B:.2f}
        
        **Meaning**: Particle A speed is e^{ln_speed_A:.2f}, 
        Particle B is e^{ln_speed_B:.2f}
        """)
    
    st.markdown("""
    **Real Physics Applications:**
    
    1. **Energy Scaling**: Particle kinetic energy E = ½mv² - when speeds get relativistic, 
       we use logarithmic scales to handle the huge numbers!
    
    2. **Beam Attenuation**: As particles travel through matter, intensity follows:
       **I = I₀ × e^(-μx)** where μ is attenuation coefficient
    
    3. **Half-Life Calculations**: Radioactive particles decay as:
       **N(t) = N₀ × e^(-λt)** - the natural exponential appears everywhere!
    
    4. **Data Analysis**: When collision energies range from 10³ to 10¹² electron volts,
       scientists plot on **logarithmic scales** to see patterns clearly.
    """)
    
    # Interactive decay example
    st.markdown("#### 🧪 Try a Decay Calculation:")
    half_life = st.slider("Half-life (seconds):", 1, 100, 10)
    time_elapsed = st.slider("Time elapsed (seconds):", 0, 200, 50)
    
    # Calculate decay
    decay_constant = np.log(2) / half_life  # λ = ln(2)/t_half
    remaining = np.exp(-decay_constant * time_elapsed)
    
    st.success(f"""
    **Decay Results:**
    - After {time_elapsed} seconds: **{remaining:.1%}** of original particles remain
    - Calculation: e^(-{decay_constant:.3f} × {time_elapsed}) = {remaining:.3f}
    """)

# Link to tutorial
st.markdown("---")
st.markdown("""
### 📚 Deep Dive Learning Resources
🎥 **[Complete Base Ten & Logarithms Tutorial](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs)** - Khan Academy's comprehensive guide to powers of 10 and logarithms

📖 **[Scientific Notation Interactive Practice](https://www.mathsisfun.com/numbers/scientific-notation.html)** - Math is Fun's hands-on exercises

🧮 **[Natural Logarithms Explained](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:logs/x2ec2f6f830c9fb89:log-intro/v/intro-to-logarithms)** - Understanding ln and e

⚛️ **[Exponential Decay in Physics](https://www.khanacademy.org/science/physics/quantum-physics/quantum-numbers-and-orbitals/a/radioactive-decay-types-article)** - Real applications of e^x
""")

# Original physics concept section
st.markdown("---")
st.subheader("🎯 Concept Introduction: Opposing Motion & Forces")
st.markdown("""
Imagine two particles launched from opposite sides of a collider tube. One from the left, one from the right. They're both accelerating *toward each other*. Just like two trains in opposite motion.

This models **Newton's Laws** and conservation of momentum. Scientists calculate when/where they meet using similar math to relative speed in train problems.
""")

# Choose direction
scenario = st.radio("Choose your particle motion setup:", ["Opposite Directions", "Same Direction"])

# Inputs
particleA_speed = st.slider("Particle A Speed (m/s)", 1, 1000000, 100000)
particleB_speed = st.slider("Particle B Speed (m/s)", 1, 1000000, 200000)
initial_distance = st.slider("Initial Distance Between (meters)", 100, 10000000, 1000000)

# Show scientific notation for current values
st.markdown(f"""
### 🧪 Your Values in Scientific Notation:
- **Particle A Speed**: {particleA_speed:,.0f} m/s = {particleA_speed:.2e} m/s
- **Particle B Speed**: {particleB_speed:,.0f} m/s = {particleB_speed:.2e} m/s  
- **Initial Distance**: {initial_distance:,.0f} m = {initial_distance:.2e} m
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
    
    # Animation control
    run_animation = st.button("▶️ Run Collision Animation")
    
    if run_animation:
        anim = st.empty()
        progress_bar = st.progress(0)
        
        total_time = meeting_time + meeting_time * 0.1
        steps = min(50, int(total_time * 10))  # Limit steps for performance

        for t in range(steps):
            progress = t / steps
            t_sec = (t / steps) * total_time
            
            if scenario == "Opposite Directions":
                posA = particleA_speed * t_sec
                posB = initial_distance - particleB_speed * t_sec
            else:
                posA = particleA_speed * t_sec
                posB = particleB_speed * t_sec

            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=[posA], y=[1], 
                mode='markers+text', 
                marker=dict(size=20, color='blue'), 
                text=["A"], 
                textposition="middle center",
                name="Particle A"
            ))
            fig.add_trace(go.Scatter(
                x=[posB], y=[-1], 
                mode='markers+text', 
                marker=dict(size=20, color='red'), 
                text=["B"], 
                textposition="middle center",
                name="Particle B"
            ))

            fig.update_layout(
                title=f"Collision Animation - Time: {t_sec:.3f} s", 
                xaxis=dict(title="Position (m)", range=[0, initial_distance]), 
                yaxis=dict(visible=False, range=[-2, 2]), 
                height=300,
                showlegend=False
            )
            
            anim.plotly_chart(fig, use_container_width=True)
            progress_bar.progress(progress)
            time.sleep(0.1)
        
        st.success("🎉 Animation Complete!")

# Enhanced Practice Section
st.markdown("---")
st.subheader("🔢 Practice: Powers of Ten in Real Physics")

# Interactive practice problems
practice_mode = st.selectbox("Choose Practice Level:", 
                           ["Beginner", "Intermediate", "Advanced"])

if practice_mode == "Beginner":
    st.markdown("""
    **Convert to Scientific Notation:**
    1. Speed of light: 299,792,458 m/s
    2. Diameter of hydrogen atom: 0.0000000001 m
    3. Distance to moon: 384,400,000 m
    """)
elif practice_mode == "Intermediate":
    st.markdown("""
    **Physics Applications:**
    1. If a proton travels at 2.4 × 10⁸ m/s, how far does it travel in 1 × 10⁻⁹ seconds?
    2. An electron has mass 9.1 × 10⁻³¹ kg. What's the mass of 1 million electrons?
    3. Light travels 3 × 10⁸ m/s. How long to travel 1.5 × 10¹¹ m (Earth to Sun)?
    """)
else:  # Advanced
    st.markdown("""
    **Particle Physics Calculations:**
    1. LHC accelerates protons to 0.999999991c (where c = 3×10⁸ m/s). Calculate exact speed.
    2. Planck length is 1.6 × 10⁻³⁵ m. How many Planck lengths in an atom diameter (10⁻¹⁰ m)?
    3. If particles collide with energy 1.3 × 10⁻⁶ J, convert to electron volts (1 eV = 1.6 × 10⁻¹⁹ J).
    """)

# Answer key in expandable section
with st.expander("💡 Answer Key"):
    if practice_mode == "Beginner":
        st.markdown("""
        1. **2.998 × 10⁸ m/s**
        2. **1.0 × 10⁻¹⁰ m** 
        3. **3.844 × 10⁸ m**
        """)
    elif practice_mode == "Intermediate":
        st.markdown("""
        1. **Distance = (2.4 × 10⁸) × (1 × 10⁻⁹) = 2.4 × 10⁻¹ = 0.24 m**
        2. **Mass = (9.1 × 10⁻³¹) × (1 × 10⁶) = 9.1 × 10⁻²⁵ kg**
        3. **Time = (1.5 × 10¹¹) ÷ (3 × 10⁸) = 5 × 10² = 500 seconds**
        """)
    else:
        st.markdown("""
        1. **Speed = 0.999999991 × (3 × 10⁸) = 2.99999997 × 10⁸ m/s**
        2. **Number = (10⁻¹⁰) ÷ (1.6 × 10⁻³⁵) = 6.25 × 10²⁴ Planck lengths**
        3. **Energy = (1.3 × 10⁻⁶) ÷ (1.6 × 10⁻¹⁹) = 8.125 × 10¹² eV = 8.125 TeV**
        """)

# Enhanced Forces context
st.subheader("💥 Forces Behind Opposing Motion")
st.markdown("""
Particles move in opposite directions due to **magnetic fields**, **electrostatic forces**, or initial launch force. In large colliders (like the LHC), particles are accelerated to high speeds and collided to study fundamental forces.

**Real-World Connection**: The Large Hadron Collider accelerates protons to 99.9999991% the speed of light - that's about **2.998 × 10⁸ m/s**! At these speeds, particles complete the 27-kilometer ring over 11,000 times per second.

You can model this with the math you learned in **train problems**: calculate distance, relative speed, and meeting point - just with much smaller scales and higher speeds!
""")

# Additional resources section
st.markdown("---")
st.subheader("📚 Additional Learning Resources")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **🔬 Physics:**
    - [CERN Virtual Visit](https://visit.cern)
    - [Particle Adventure](https://www.particleadventure.org)
    """)

with col2:
    st.markdown("""
    **📊 Math:**
    - [Powers of 10 Film](https://www.youtube.com/watch?v=0fKBhvDjuy0)
    - [IXL Exponents Practice](https://www.ixl.com/math/algebra-1/powers-of-ten)
    - [Scientific Notation Games](https://www.sheppardsoftware.com/mathgames/algebra/scientific_notation.htm)
    """)

with col3:
    st.markdown("""
    **🧮 Practice:**
    - [Khan Academy: Exponents](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:rational-exponents-radicals)
    - [PhET Simulations](https://phet.colorado.edu)
    """)

# Footer
st.markdown("""
---
<center style='font-size: 0.85em; color: gray;'>
Built with 💡 by Xavier Honablue, M.Ed. | MathCraft Series | All rights reserved.<br>
🎯 Connecting abstract math to real-world physics since 2024
</center>
""", unsafe_allow_html=True)
