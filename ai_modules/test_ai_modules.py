from ai_modules import load_llm, process_pdf, generate_answer

llm = load_llm()
print("***** LLM loaded successfully *****")

#test llm
# response = llm.invoke("Thủ đô của Pháp là gì?")
# print(response)

# test process_pdf
tmp_file_path = "YOLOv10_Tutorials.pdf" # this is a placeholder, replace with the actual temp_path_file to the uploaded PDF
retriever = process_pdf(tmp_file_path)
print("***** Retriever created successfully *****")


query = "YOLOv10 là gì vậy?" # this is a placeholder, replace with the actual query
# response = retriever.invoke(query)
# print(response)

# test generate_answer
answer = generate_answer(retriever, llm, query)
print(answer)