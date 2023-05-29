import gradio as gr
from embaddings import *

def greet(file,name):
    
    return create_embadding(file,name)

train = gr.Interface(fn=greet, 
                     inputs= [
                     gr.inputs.File(label="upload your file"), 
                     gr.components.Textbox(label="name",placeholder="How do you want to call your file?")
                     ],
                     outputs="text", 
                     title="JTAI", 
                     description="Create different kinds of content")


if __name__ == "__main__":
    train.launch(share=False)