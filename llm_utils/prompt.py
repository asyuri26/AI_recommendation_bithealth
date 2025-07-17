import json
from langchain.prompts import PromptTemplate

# Load few-shot dataset from JSON
def load_examples(path="example_dataset.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def prompt_template(examples, new_input):
    example_str = ""
    for x in examples:
        example_str += (
            f"Input:\nGender: {x['gender']}\nAge: {x['age']}\n"
            f"Symptoms: {', '.join(x['symptoms'])}\n"
            f"Departemen: {x['department']}\n\n"
        )

    template = (
        "Tentukan departemen medis berdasarkan data pasien. Jawaban satu kata.\n\n"
        "Contoh:\n" + example_str +
        "Input:\nGender: {gender}\nAge: {age}\nSymptoms: {symptoms}\nDepartemen:"
    )

    prompt = PromptTemplate(
        input_variables=["gender", "age", "symptoms"],
        template=template
    )

    return prompt.format(
        gender=new_input["gender"],
        age=new_input["age"],
        symptoms=", ".join(new_input["symptoms"])
    )