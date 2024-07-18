# Project: Data Source Connections and Storage with Unstructured.io, Dataset Generation
### Project Goal: 
- Extract data from various sources and store it in S3 and a vector database for dataset generation and RAG applications.
- To generate datasets for DPO, fine-tuning, and RLHF, a powerful model like Llama3 will use data stored in S3. It will use this data to create questions, then query a vector database to retrieve relevant context for answering these questions. The resulting question-answer pairs will form datasets for further fine-tuning of foundational models.

**Dataset Generation(not part of this project):** To generate datasets for DPO, fine-tuning, and RLHF, a powerful model like Llama3 will use data stored in S3. It will use this data to create questions, then query a vector database to retrieve relevant context for answering these questions. The resulting question-answer pairs will form datasets for further fine-tuning of foundational models.
References: https://docs.unstructured.io/open-source/introduction/overview
- **Review Existing Connectors:** Review available connectors in Unstructured.io (Local storage, GitHub, Google Drive, MongoDB, S3, Slack, Wikipedia, Elasticsearch).
- **Review Data Preparation Options:** Review data preparation options within Unstructured.io (cleaning, chunking, embeddings).
- **Minio Documentation Review:** Study the Minio documentation, focusing on its features relevant to data storage and retrieval.
RAG and Vector Database Documentation(chroma) Review: Review documentation on Retrieval Augmented Generation (RAG) techniques and the Chroma vector database and their integration with Unstructured.io and their capabilities for building RAG systems.
6 hr
- **Connector Testing & Demo:** Test and create a demo of existing Unstructured.io connectors (Local storage, GitHub, Google Drive, MongoDB, S3, Slack, Wikipedia, Elasticsearch).
- Extract data from at least 2 source connectors, perform data preparation options, store prepared data in S3 bucket and vector database(Chroma, Quadrant, Pinecone, Weaviate).


### Dataset Generation
- **Datasets reference:** 
    - DPO: https://github.com/hiyouga/LLaMA-Factory/blob/main/data/dpo_en_demo.json
    - Fine Tuning dataset: https://github.com/hiyouga/LLaMA-Factory/blob/main/data/alpaca_en_demo.json
    - RLHF Dataset: https://huggingface.co/datasets/Anthropic/hh-rlhf

- **Model Selection and Setup:** Choose a suitable language model (Llama3 or similar) and set up the necessary environment.
- **Prompt Engineering with Few-Shot Learning:** Develop effective prompts for Llama3(or chosen model) to generate questions based on the S3 data chunks, use few-shot learning techniques to improve Llama3's question generation abilities.
- **Context Retrieval & Answer Generation:** Connect the language model to a chosen vector database (Chroma, Quadrant, Pinecone, Weaviate). Implement the process of retrieving relevant context from the vector database for each generated question. Utilise Llama3 to generate answers based on the retrieved context and the original question.
- **Fine-tuning Foundational Models (not part of the project):** The generated datasets are used to fine-tune foundational models (e.g. Llama3 itself).
- **Dataset Organization:** organise the generated question-answer pairs into JSONL format for distinct datasets for DPO, fine-tuning, and RLHF and ensure each dataset contains a sufficient number of question-answer pairs.
- **Final Testing & Demo:** Test the entire dataset generation pipeline.
Code Repository and Documentation: Move the completed code to a GitHub repository for future use and create proper documentation.

