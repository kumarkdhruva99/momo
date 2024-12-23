import streamlit as st

st.title("Hello Beautiful...")
st.header("Kya kr rhi hai")
st.markdown("Bolo...")
st.markdown("Chalo kuch questions ke answer batao")
a = ["Please select an option","yes", "haa baby","bahut zyada"]
b = ["Please select an option","haa jaan","yes aur bache v","mujhe sharam aa rhi"]
c = ["Please select an option","Shirt","T shirt","Couple ring giva wala"]

onu = st.selectbox("Do you love me",a)
momo = st.selectbox("Tu shaadi kregi na mese",b)
bacha = st.selectbox("Mera aaj bday hai tu gift kya degi",c)

button = st.button("Ho gya")

if button:
    st.markdown(f"""
    Apka answer: {onu}
    Apka answer: {momo}
    Apka answer: {bacha}""")

st.text("Aee ye dekho hmara pic")
st.image("momo.jpg")
st.header("Love you baby :kissing_heart::kissing_heart:")
st.audio("tumhiho.mp3")




