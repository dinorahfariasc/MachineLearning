import requests
from dotenv import load_dotenv, find_dotenv
from transformers import pipeline
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from gtts import gTTS
import streamlit as st
from PIL import Image
import io

load_dotenv(find_dotenv())

# imgtotext
def img2text(image):
    img_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base", max_new_tokens=50)

    # Convert PIL image to a format suitable for the pipeline
    text = img_to_text(image)[0]["generated_text"]
    print(f"imagem para texto: {text}")
    return text
    
# Ajustar para usar PIL Image
def convert_uploaded_file(uploaded_file):
    image = Image.open(uploaded_file)
    return image

# llms
def generate_story(scenario):
    generator = pipeline("text-generation", model="gpt2")
    template = '''
    Generate a short simple story (do not supose or give steps) the story should be about 150 caracthers long, between 3 to 5 setences and should be based on the following Context: {scenario};

    STORY:
    '''
    
    text = generator(template, max_length=150, num_return_sequences=1, truncation=True)

    # selecionar o texto gerado e remover o contexto do prompt/template
    generated_text = text[0]['generated_text'].split("STORY:")[1].strip()

    print("Generated Text:", generated_text)
    return generated_text

# text to speech
def text2speech(text, filename='output.mp3'):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f"Audio saved as {filename}")

# interface com streamlit
def main():
    st.set_page_config(page_title="Image to audio story", page_icon="🤖", layout="centered")

    st.header("Turn img into audio story")
    uploaded_file = st.file_uploader("Choose an image...", type="jpeg")
    if uploaded_file is not None:
        image = convert_uploaded_file(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        scenario = img2text(image)
        story = generate_story(scenario)
        text2speech(story)

        with st.expander("Scenario"):
            st.write(scenario)
        with st.expander("Story"):
            st.write(story)
        with st.expander("Audio"):
            st.audio("output.mp3")

if __name__ == "__main__":
    main()


    # st.title("Image to Lore")
    # st.write("Upload an image and we will generate a short story based on it!")
    # uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    # if uploaded_file is not None:
    #     with open("image.jpeg", "wb") as f:
    #         f.write(uploaded_file.getbuffer())
    #     st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    #     st.write("Generating story...")
    #     scenario = img2text("image.jpeg")
    #     story = generate_story(scenario)
    #     text2speech(story)
    #     st.audio("output.mp3")
