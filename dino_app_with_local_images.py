
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Dino World 🦖", page_icon="🦕", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.markdown("<h1 style='text-align: center;'>🦖 WELCOME TO THE WORLD OF DINOSAURS, KIDDO! 🦕</h1>", unsafe_allow_html=True)
    if st.button("Start Exploring!"):
        st.session_state.page = "explore"
        st.experimental_rerun()

elif st.session_state.page == "explore":
    st.markdown("## 🦕 Choose a Dinosaur to Learn More!")
    dinos = {
        "Tyrannosaurus": {
            "image": "download (1).jpg",
            "facts": [
                "Name means 'Tyrant Lizard King'.",
                "One of the largest meat-eating dinosaurs.",
                "Lived around 68 million years ago."
            ]
        },
        "Triceratops": {
            "image": "download (2).jpg",
            "facts": [
                "Had three distinct horns on its face.",
                "Herbivore with a large bony frill.",
                "Lived in the Late Cretaceous period."
            ]
        },
        "Velociraptor": {
            "image": "download (3).jpg",
            "facts": [
                "Fast and intelligent hunter.",
                "Had feathers, not just scales!",
                "Much smaller than shown in movies."
            ]
        },
        "Brachiosaurus": {
            "image": "download (4).jpg",
            "facts": [
                "Had a long neck and small head.",
                "Herbivore that reached tree tops.",
                "Lived during the Jurassic period."
            ]
        },
        "Stegosaurus": {
            "image": "download (5).jpg",
            "facts": [
                "Famous for its back plates.",
                "Had a tiny brain, walnut-sized!",
                "Used its tail spikes for defense."
            ]
        },
        "Ankylosaurus": {
            "image": "download (6).jpg",
            "facts": [
                "Covered in heavy armor plates.",
                "Had a clubbed tail for protection.",
                "Herbivore from Late Cretaceous."
            ]
        },
        "Spinosaurus": {
            "image": "download (7).jpg",
            "facts": [
                "Had a large sail on its back.",
                "One of the few aquatic dinosaurs.",
                "Larger than T-Rex!"
            ]
        },
        "Parasaurolophus": {
            "image": "download (8).jpg",
            "facts": [
                "Had a long curved crest on its head.",
                "Could make loud honking sounds.",
                "Moved both on two and four legs."
            ]
        }
    }

    choice = st.selectbox("Pick your Dino!", list(dinos.keys()))
    dino = dinos[choice]

    try:
        image = Image.open(dino["image"])
        st.image(image, caption=choice, use_container_width=True)
    except:
        st.error("Image not found. Make sure the image file is in the same folder.")

    st.markdown("### Fun Facts:")
    for fact in dino["facts"]:
        st.write(f"• {fact}")

    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.experimental_rerun()
