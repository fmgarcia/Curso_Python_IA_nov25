import spacy

texto = "Ayer hablé con Fran García en Alicante sobre Microsoft."

def cargar_modelo_spacy(modelo: str = "es_core_news_sm"):
    '''
    Esta función carga el modelo de spaCy especificado.\n
    modelo: Nombre del modelo de spaCy a cargar (por defecto "es_core_news_sm")\n
    return: Objeto Language del modelo cargado
    '''
    try:
        nlp = spacy.load(modelo)
        return nlp
    except Exception as e:
        print(f"Error al cargar el modelo de spaCy '{modelo}': {e}")
        return None
    
if __name__ == "__main__":
    nlp = cargar_modelo_spacy()
    if nlp:
        doc = nlp(texto)
        personas = [ent.text for ent in doc.ents if ent.label_ == "PER"]
        lugares = [ent.text for ent in doc.ents if ent.label_ == "LOC"]
        organizaciones = [ent.text for ent in doc.ents if ent.label_ == "ORG"]    
        print(f"Personas encontradas: {personas}")
        print(f"Lugares encontrados: {lugares}")
        print(f"Organizaciones encontradas: {organizaciones}")