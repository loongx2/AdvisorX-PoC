import openai
import chainlit as cl
from chainlit import user_session


model_name = "gpt-3.5-turbo-16k"
openai.api_key = ""
settings = {"temperature": 0.5}


@cl.action_callback("personal_info")
async def on_action(action):
    required_info = "- Your age: \n- Your geographic location:\n - Your current income: per month\n - Your monthly expenses: per month\n - Your existing debt: \n - Your current savings: \n - Your financial objectives: \n - Your risk tolerance: \n- Your investment preferences: \n- Your financial concerns: \n - Your credit score: "
    await cl.Message(content=f"{required_info}").send()

    # Sending an action button within a chatbot message
    actions = [
        cl.Action(
            name="retirement_financial_trajectory",
            value="Using my information that I have given and your recommended financial budgeting plan, how can I get to retirement?",
            description="Retirement Financial Trajectory",
        ),
        cl.Action(
            name="insurance_for_dependents_properties",
            value="How do I know how much insurance needs to be allocated for my dependents and properties?",
            description="Insurance for dependents and properties",
        ),
        cl.Action(
            name="graduate_salary_for_mortgage",
            value="I want to know my salary earning trajectory for own home",
            description="Graduate salary earning trajectory for own home",
        ),
    ]

    await cl.Message(content="What is your goal?", actions=actions).send()

    await action.remove()


@cl.action_callback("retirement_financial_trajectory")
async def on_action(action):
    await cl.Message(content=f"{action.value}").send()
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": f"{action.value}"})
    cl.user_session.set(
        "message_history",
        [{"role": "user", "content": f"{action.value}"}],
    )

    msg = cl.Message(content="")
    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    id = await msg.send()

    if "retirement" in msg.content:
        actions = [
            cl.Action(name="rental_properties", value="Step by step, using my information that I have given and your recommended financial budgeting plan, how I buy rental properties?", description="Rental properties"),
            cl.Action(name="maximize_retirement_contributions", value="Step by step, using my information that I have given and your recommended financial budgeting plan, go into detail on how I can maximize my retirement contributions?", description="Maximize retirement contributions"),
            cl.Action(name="increase_savings", value="Step by step, using my information that I have given and your recommended financial budgeting plan, go into detail on how I can increase savings?", description="Increase Savings")
        ]

        await cl.Message(content="Which retirement strategy would you like to find out more?", parent_id=id, actions=actions).send()


@cl.action_callback("increase_savings")
async def on_action(action):
    await cl.Message(content=f"{action.value}").send()
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": f"{action.value}"})
    cl.user_session.set(
        "message_history",
        [{"role": "user", "content": f"{action.value}"}],
    )

    msg = cl.Message(content="")
    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()

@cl.action_callback("maximize_retirement_contributions")
async def on_action(action):
    await cl.Message(content=f"{action.value}").send()
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": f"{action.value}"})
    cl.user_session.set(
        "message_history",
        [{"role": "user", "content": f"{action.value}"}],
    )

    msg = cl.Message(content="")
    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()

@cl.action_callback("diversify_investments")
async def on_action(action):
    await cl.Message(content=f"{action.value}").send()
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": f"{action.value}"})
    cl.user_session.set(
        "message_history",
        [{"role": "user", "content": f"{action.value}"}],
    )

    msg = cl.Message(content="")
    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()

@cl.action_callback("rental_properties")
async def on_action(action):
    await cl.Message(content=f"{action.value}").send()
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": f"{action.value}"})
    cl.user_session.set(
        "message_history",
        [{"role": "user", "content": f"{action.value}"}],
    )

    msg = cl.Message(content="")
    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()


@cl.action_callback("insurance_for_dependents_properties")
async def on_action(action):
    await cl.Message(content=f"{action.value}").send()
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": f"{action.value}"})
    cl.user_session.set(
        "message_history",
        [{"role": "user", "content": f"{action.value}"}],
    )

    msg = cl.Message(content="")
    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    if "dependents" in msg.content or "housing" in msg.content:
        actions = [
            cl.Action(name="properties_insurance", value="Step by step, using my information that I have given and your recommended financial budgeting plan, how I insure my property assets?", description="Property assets insurance"),
            cl.Action(name="early_child_health_insurance", value="Step by step, using my information that I have given and your recommended financial budgeting plan, go into detail on how I should invest in my children's health insurance coverage?", description="Children's health insurance"),
            cl.Action(name="child_tertiary_education_fund", value="Step by step, using my information that I have given and your recommended financial budgeting plan, go into detail on how I can invest for my children's tertiary education fund?", description="Children's tertiary education fund")
        ]

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()

@cl.action_callback("properties_insurance")
async def on_action(action):
    await cl.Message(content=f"{action.value}").send()
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": f"{action.value}"})
    cl.user_session.set(
        "message_history",
        [{"role": "user", "content": f"{action.value}"}],
    )

    msg = cl.Message(content="")
    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()

@cl.action_callback("early_child_health_insurance")
async def on_action(action):
    await cl.Message(content=f"{action.value}").send()
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": f"{action.value}"})
    cl.user_session.set(
        "message_history",
        [{"role": "user", "content": f"{action.value}"}],
    )

    msg = cl.Message(content="")
    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()

@cl.action_callback("child_tertiary_education_fund")
async def on_action(action):
    await cl.Message(content=f"{action.value}").send()
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": f"{action.value}"})
    cl.user_session.set(
        "message_history",
        [{"role": "user", "content": f"{action.value}"}],
    )

    msg = cl.Message(content="")
    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()

@cl.action_callback("graduate_salary_for_mortgage")
async def on_action(action):
    await cl.Message(content=f"{action.value}").send()
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": f"{action.value}"})
    cl.user_session.set(
        "message_history",
        [{"role": "user", "content": f"{action.value}"}],
    )

    msg = cl.Message(content="")
    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()


@cl.on_chat_start
async def start_chat():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "I want you to act as a financial advisor. Here's a budgeting plan that I want you to understand, \n- range from 3 to 6 months of expenses\n- from income 10%% financial freedom, next 10%% on major purpose\n- 55%% on necessities of which up to 10 to 15%% on insurances and up to 35%% for serviceable debt\n- remaining 25%% for funds which comprises 5%% for charity or relationship building, 10%% for educational or experiential learning and 10%% just for fun"}],
    )

    actions = [
        cl.Action(
            name="retirement_financial_trajectory",
            value="Using my information that I have given and your recommended financial budgeting plan, how can I get to retirement? In addition, using my information that I have given and your recommended financial budgeting plan, recommend me some ways to generate passive income or assets that can give passive income.",
            description="Retirement Financial Trajectory",
        ),
        cl.Action(
            name="insurance_for_dependents_properties",
            value="How do I know how much insurance needs to be allocated for my dependents and properties based on my given salary?",
            description="Insurance for dependents and properties",
        ),
        cl.Action(
            name="graduate_salary_for_mortgage",
            value="I want to know my salary earning trajectory for own home",
            description="Graduate salary earning trajectory for own home",
        ),
    ]

    required_info = "- My age: \n- My gender: \n- My marital status: \n- My housing: \n- My housing finance: \n- My mode of transport: \n- My mode of transport finance: \n- My geographic location:\n - My current income: per month\n - My monthly expenses: per month\n - My existing debt: \n - My current savings: \n - My financial objectives: \n - My risk tolerance: \n- My preferences: \n- My financial concerns: \n - My credit score: "

    await cl.Message(content=f"Tell me more about yourself and where you are at financially?\n\nProvide your infomation in this format\n{required_info}", actions=actions).send()

@cl.author_rename
def rename(orig_author: str):
    rename_dict = {"Chatbot": "Expert"}
    return rename_dict.get(orig_author, orig_author)

@cl.on_message
async def main(message: str):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message})

    msg = cl.Message(content="")

    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    # temp_content = msg.content
    message_history.append({"role": "assistant", "content": msg.content})
    await msg.send()
