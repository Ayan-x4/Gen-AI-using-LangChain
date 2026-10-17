
import warnings
warnings.filterwarnings("ignore")

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100,
        "do_sample": False,
        "return_full_text": False
    }
)

model = ChatHuggingFace(llm=llm)

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        break

    if not user_input:
        continue

    result = model.invoke(user_input)
    answer = result.content.strip()

    for token in ["<|user|>", "<|assistant|>", "<|system|>", "</s>"]:
        answer = answer.replace(token, "")

    print("Bot:", answer.strip())


