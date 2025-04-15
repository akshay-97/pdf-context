import fitz

def pdf_to_text_page(file):
    return fitz.open(file)
    
class Chunker:
    def __init__(self,overlap, line_chunk_size, doc = None):
        self.doc = doc
        self.overlap = overlap
        self.line_chunk_size = line_chunk_size
        #self.chunks = []
        #self.page = 0
    
    def set_doc(self, doc):
        self.doc = doc

    def chunk_documents(self):
        chunks = []
        
    
        for page in doc:

            page_lines = page.split('\n').to_list()
            total_lines = len(page_lines)
            start = 0
            diff =  self.line_chunk_size if self.line_chunk_size < total_lines else total_lines
            end = diff

            while start < end and end <= total_lines:
                chunk.append(total_lines[start:end])

                start = end - (diff *self.overlap) // 100
                if (start +diff) > total_lines:
                    end = total_lines
                else:
                    end = start + diff

        return chunks

        
