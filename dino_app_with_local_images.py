import streamlit as st
from PIL import Image

st.set_page_config(page_title="Animal World Explorer 🐾", page_icon="🌍", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.markdown("""
        <h1 style='text-align: center;'>🌟 Welcome to Animal World Explorer! 🌟</h1>
        <p style='text-align: center;'>Discover fun facts and cute images of animals from different categories! 🐘🦖🐦🦎</p>
    """, unsafe_allow_html=True)
    if st.button("🐾 Start Exploring"):
        st.session_state.page = "explore"
        st.experimental_rerun()

elif st.session_state.page == "explore":
    category = st.selectbox("Choose a Category 🧭", ["Dinosaurs", "Mammals", "Birds", "Reptiles"])

    animals = {}

    if category == "Dinosaurs":
        st.markdown("### 🦖 Dino Explorer Coming Up!")
        st.info("🔄 You can plug in your existing dino code block here!")

    elif category == "Mammals":
        animals = {
            "Lion": {
                "image": "C:/Users/VINWINER/Downloads/download.jpg",
                "facts": ["🦁 Known as the king of the jungle.", "🌞 Lives in prides and loves sunbathing."]
            },
            "Elephant": {
                "image": "C:/Users/VINWINER/Downloads/download (1).jpg",
                "facts": ["🐘 Largest land animal.", "👂 Uses ears to cool off."]
            },
            "Panda": {
                "image": "C:/Users/VINWINER/Downloads/download (2).jpg",
                "facts": ["🐼 Loves eating bamboo.", "💤 Sleeps a lot after eating."]
            }
        }

    elif category == "Birds":
        animals = {
            "Parrot": {
                "image": "C:/Users/VINWINER/Downloads/download (3).jpg",
                "facts": ["🦜 Can mimic human speech.", "🌈 Very colorful feathers."]
            },
            "Penguin": {
                "image": "C:/Users/VINWINER/Downloads/download (4).jpg",
                "facts": ["🐧 Can't fly but swims really well.", "❄️ Lives in icy places."]
            },
            "Owl": {
                "image": "C:/Users/VINWINER/Downloads/download (5).jpg",
                "facts": ["🦉 Can rotate its head a lot!", "🌙 Active at night."]
            }
        }

    elif category == "Reptiles":
        animals = {
            "Chameleon": {
                "image": "C:/Users/VINWINER/Downloads/download (6).jpg",
                "facts": ["🦎 Changes color to blend in.", "👀 Can move eyes independently."]
            },
            "Crocodile": {
                "image": "C:/Users/VINWINER/Downloads/images.jpg",
                "facts": ["🐊 Ancient reptiles still alive today.", "💤 Can sleep with one eye open."]
            },
            "Turtle": {
                "image": "C:/Users/VINWINER/Downloads/download (7).jpg",
                "facts": ["🐢 Lives both on land and in water.", "📦 Carries its house (shell) everywhere."]
            }
        }

    if animals:
        choice = st.selectbox(f"Pick a {category[:-1]} 🐾", list(animals.keys()))
        animal = animals[choice]

        try:
            image = Image.open(animal["image"])
            st.image(image, caption=choice, use_container_width=True)
        except:
            st.error("Image not found. Make sure the image file is in the correct path.")

        st.markdown("### 🧠 Fun Facts:")
        for fact in animal["facts"]:
            st.write(f"• {fact}")

        if st.button("🏠 Back to Home"):
            st.session_state.page = "home"
            st.experimental_rerun()
