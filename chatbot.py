# chainlit_app.py

import chainlit as cl
from main import Sir_Zain, run_config
from agents import Runner

@cl.on_message
async def main(message: cl.Message):
    prompt = message.content

    try:
        # Use the agent with run_config
        result = Runner.run_sync(Sir_Zain, prompt, run_config=run_config)

        await cl.Message(
            content=f"🧠 Sir Zain says:\n\n{result.final_output}"
        ).send()

    except Exception as e:
        await cl.Message(content=f"❌ Error: {str(e)}").send()
