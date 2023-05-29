import gradio as gr
from embaddings import *
from library import *




def greet(question,K,libraries):
    print(libraries)
    x,info =  query_search(question, int(K),libraries)
    
    return x,info


question = gr.Interface(fn=greet, 
                     inputs=[
                         gr.components.Textbox(label="question",placeholder="What do you want to know?"), 
                         gr.inputs.Slider(minimum=1, maximum=5, step=1, default=2, label="K"),
                         gr.components.CheckboxGroup(library_check(),label="libraries",info="select the libraries you want to you",value=library_check())
                         
                             ], 
                     outputs=[
                        gr.outputs.Textbox(label="Output 1"),
                        gr.outputs.Textbox(label="Output 2")


                     ], 
                     title="JTAI", 
                     description="Create different kinds of content")


if __name__ == "__main__":
    question.launch(share=False)