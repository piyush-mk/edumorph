import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=st.secrets["nvapi_key"]
)

def generate_prompt(user_input):
    prompt = f"""
You are an AI content generator tasked with creating educational content. When provided with a user’s input topic, you must perform the following steps:

1. **Validate the Input:**  
   - If the input is empty, extremely short, or ambiguous, output: "Sorry, not a thing we can help you learn about."  
   - If the input does not represent a valid educational subject (e.g., non-educational phrases like "let's eat cheese", jokes, or commands), output the same error message.

2. **Generate a Course Plan:**  
   - Create a detailed course plan outline for a course that teaches the subject.
   - The course plan should include clear objectives, a list of topics, and a brief description of what each topic will cover.

3. **Generate an Intro Video Script:**  
   - Write a short, engaging introduction video script for the course that lasts approximately 15–30 seconds.
   - The script should introduce the main topics, capture the learner's interest, and include a friendly call to action (e.g., "Let's begin this journey!").
   - **Limit the intro video script to no more than 100 words.**

4. **Formatting Requirements:**  
   - Clearly label two sections in your final output: "Course Plan Outline" and "Intro Video Script".
   - Do not include any text referencing "Validated Input:" or "Output:".
   - Ensure that both sections are formatted neatly and are easy to read.

Edge Cases to Consider:  
   - **Empty Input:** Prompt the user to enter a subject.
   - **Ambiguous or Too Short Input:** If the topic does not provide enough context to build an educational course, output the error message.
   - **Non-Learnable Input:** If the input is a joke, command, or unrelated phrase, output: "Sorry, not a thing we can help you learn about."
   - **Mixed or Irrelevant Content:** If the input contains valid subject matter along with irrelevant information, focus on the valid subject; if no valid subject can be determined, output the error message.

User Input: "{user_input}"

Please provide your final output with the following two sections clearly labeled:
1. Course Plan Outline
2. Intro Video Script
"""
    return prompt

st.title("AI Course Plan & Intro Video Generator")

with st.form("course_form"):
    user_input = st.text_input("Enter a subject or topic you'd like to learn about:")
    submit_button = st.form_submit_button("Generate Content")

if submit_button:
    if not user_input.strip():
        st.error("Please enter a subject or topic.")
    else:
        detailed_prompt = generate_prompt(user_input)
        response_text = ""
        with st.spinner("Generating course plan and intro video script..."):
            for chunk in client.chat.completions.create(
                model="nvidia/llama-3.1-nemotron-70b-instruct",
                messages=[{"role": "user", "content": detailed_prompt}],
                temperature=0.5,
                top_p=1,
                max_tokens=1024,
                stream=True
            ):
                if chunk.choices[0].delta.content is not None:
                    response_text += chunk.choices[0].delta.content

        filtered_lines = [
            line for line in response_text.splitlines()
            if not (line.strip().startswith("Validated Input:") or line.strip().startswith("Output:"))
        ]
        filtered_response_text = "\n".join(filtered_lines)
        parts = filtered_response_text.split("**Intro Video Script**")
        if len(parts) >= 2:
            course_plan_outline = parts[0].strip()
            video_script = "**Intro Video Script**" + parts[1].strip()
        else:
            course_plan_outline = filtered_response_text.strip()
            video_script = ""
        st.success("Generation complete!")
        st.markdown(course_plan_outline, unsafe_allow_html=True)
        st.session_state.video_script = video_script
