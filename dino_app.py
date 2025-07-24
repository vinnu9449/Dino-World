# ✅ 1. Install Streamlit
!pip install streamlit

# ✅ 2. Dino App Code (with working triple quotes)
dino_code = '''import streamlit as st

st.set_page_config(page_title="Dino World 🦖", page_icon="🦕", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to_dino_page():
    st.session_state.page = "dino_page"

# 🎉 Home Page
if st.session_state.page == "home":
    st.markdown("<h1 style='text-align: center; color: green;'>🦖 WELCOME TO THE WORLD OF DINOSAURS, KIDDO! 🦕</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Get ready to ROAAARR into the past and meet some giant, goofy, and cool dinosaurs!</p>", unsafe_allow_html=True)
    
    if st.button("🌟 Start the Adventure!"):
        go_to_dino_page()

# 🦕 Dino Selection Page
elif st.session_state.page == "dino_page":
    st.markdown("<h2 style='text-align: center;'>🌋 Choose Your Favorite Dinosaur!</h2>", unsafe_allow_html=True)

    dino_data = {
        "T-Rex 🦖": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/3/3a/Tyrannosaurus_rex.png",
            "facts": [
                "🍗 Meat-lover and top predator!",
                "📏 Up to 40 feet long!",
                "🦴 Had banana-sized teeth!",
                "🙃 Tiny arms, big attitude!"
            ]
        },
        "Triceratops 🐮": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/8/86/Triceratops_BW.png",
            "facts": [
                "🔱 Three horns for defense.",
                "🌿 Loved munching on plants!",
                "🛡️ Had a giant frill like a shield.",
                "😇 Gentle giant!"
            ]
        },
        "Stegosaurus 🦕": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/7/72/Stegosaurus_BW.png",
            "facts": [
                "🔰 Plates on back like armor.",
                "🧠 Brain was teeny tiny!",
                "🌱 A peaceful plant-eater.",
                "🦶 Tail spikes called 'thagomizers'."
            ]
        },
        "Velociraptor 🏃‍♂️": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/5/5f/Velociraptor_BW.png",
            "facts": [
                "⚡ Super fast and sneaky!",
                "👯‍♂️ Hunted in packs.",
                "🧠 Very smart for a dino!",
                "💅 Had sharp toe claws!"
            ]
        },
        "Brachiosaurus 🦒": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/1/19/Brachiosaurus_BW.png",
            "facts": [
                "📏 Could reach treetops!",
                "🌳 Ate leaves from tall trees.",
                "🦕 Long neck like a giraffe!",
                "🎈 Very chill and huge!"
            ]
        },
        "Ankylosaurus 🛡️": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/b/b1/Ankylosaurus_BW.png",
            "facts": [
                "🛡️ Armored like a tank!",
                "🔨 Had a clubbed tail.",
                "😎 Total dino-badass!",
                "🌿 Herbivore with style!"
            ]
        },
        "Spinosaurus 🐊": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/b/bc/Spinosaurus_BW.png",
            "facts": [
                "🛶 Loved to swim!",
                "🎣 Ate fish with its long snout.",
                "🦴 Had a giant sail on its back!",
                "😲 Bigger than a T-Rex!"
            ]
        },
        "Pteranodon 🪂": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/1/12/Pteranodon_BW.png",
            "facts": [
                "🌬️ Could fly high in the sky!",
                "📏 Wingspan up to 33 feet!",
                "🪁 Not a dinosaur — a flying reptile!",
                "🌊 Liked to chill near oceans."
            ]
        },
        "Pachycephalosaurus 💥": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/0/0a/Pachycephalosaurus_BW.png",
            "facts": [
                "💣 Had a super thick skull!",
                "🤯 Used headbutts like a wrecking ball.",
                "🌱 Ate low plants.",
                "🥽 Dino headgear champ!"
            ]
        },
        "Iguanodon 👆": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/f/f4/Iguanodon_BW.png",
            "facts": [
                "☝️ Had a thumb spike for defense!",
                "👨‍👦 Traveled in herds.",
                "🥬 Plant-eater with strong arms.",
                "📜 One of the first dinos discovered!"
            ]
        },
        "Dilophosaurus 🎯": {
            "image": "https://static.wikia.nocookie.net/dinosaurs/images/8/88/Dilophosaurus_BW.png",
            "facts": [
                "💀 Had two fancy crests on its head!",
                "🗣️ Might have made scary sounds!",
                "🎭 Spit venom in the movies — but not in real life!",
                "🎯 Light, fast, and deadly!"
            ]
        }
    }

    selected_dino = st.selectbox("👇 Pick a dino to meet!", list(dino_data.keys()))

    if selected_dino:
        st.image(dino_data[selected_dino]["image"], width=400, caption=f"Say hi to {selected_dino}!")
        st.markdown("### 💡 Fun Dino Facts:")
        for fact in dino_data[selected_dino]["facts"]:
            st.markdown(f"- {fact}")
'''

# ✅ 3. Save to .py file
with open("dino_app.py", "w") as f:
    f.write(dino_code)

# ✅ 4. Download the file
from google.colab import files
files.download("dino_app.py")
