from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkService:

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

    def split_documents(self, documents):

        chunks = []

        for document in documents:

            texts = self.text_splitter.split_text(document["text"])

            for index, text in enumerate(texts):

                chunk_id = f"{document['file']}_{document['page']}_{index+1}"

                chunks.append(
                {
                    "id": chunk_id,
                    "file": document["file"],
                    "page": document["page"],
                    "chunk": index+1,
                    "text": text
                }
                )
                # chunks.append(
                #     {
                #         "file": document["file"],
                #         "page": document["page"],
                #         "chunk": index + 1,
                #         "text": text,
                #     }
                # )

        return chunks