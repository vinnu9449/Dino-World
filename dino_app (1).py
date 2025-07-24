
import streamlit as st

st.set_page_config(page_title="Dino World 🦖", page_icon="🦕", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "home"

def show_home():
    st.title("🦕 Welcome to the World of Dinosaurs, Kiddo!")
    st.write("Get ready to explore some cool dinosaurs! Click the button below to start your journey. 🦖🌿")
    if st.button("Start Exploring 🚀"):
        st.session_state.page = "explore"

def show_explore():
    st.title("🦖 Choose Your Dino Buddy!")
    dinos = {
        "Tyrannosaurus Rex": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/3/3a/Tyrannosaurus_rex.png",
            "facts": [
                "Name means 'Tyrant Lizard King'",
                "Lived about 68 million years ago",
                "Had banana-sized teeth!",
                "One of the most ferocious predators"
            ]
        },
        "Triceratops": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/8/86/Triceratops_BW.png",
            "facts": [
                "Had three awesome horns",
                "Used frill to scare enemies",
                "Was a plant-eater",
                "Loved to hang out in herds"
            ]
        },
        "Velociraptor": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/5/5f/Velociraptor_BW.png",
            "facts": [
                "Fast and clever hunter",
                "Had sharp claws",
                "Used teamwork to hunt",
                "Was smaller than shown in movies"
            ]
        },
        "Stegosaurus": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/7/72/Stegosaurus_BW.png",
            "facts": [
                "Had cool back plates",
                "Tail had spikes for defense",
                "Brain was tiny (like a puppy's)",
                "Loved munching on plants"
            ]
        },
        "Brachiosaurus": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/1/19/Brachiosaurus_BW.png",
            "facts": [
                "Was as tall as a 4-story building",
                "Had a super long neck",
                "A gentle plant-eater",
                "Loved to eat leaves from tall trees"
            ]
        },
        "Ankylosaurus": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/b/b1/Ankylosaurus_BW.png",
            "facts": [
                "Had armor like a tank",
                "Tail club used for defense",
                "A slow mover but super tough",
                "Loved low plants"
            ]
        }
    }

    dino_names = list(dinos.keys())
    choice = st.selectbox("Pick a dinosaur to meet:", dino_names)

    dino = dinos[choice]
    st.image(dino["image"], width=300, caption=choice)
    st.subheader("🦴 Fun Facts")
    for fact in dino["facts"]:
        st.markdown(f"- {fact}")

    if st.button("⬅️ Go Back"):
        st.session_state.page = "home"

if st.session_state.page == "home":
    show_home()
else:
    show_explore()
