from refined.inference.processor import Refined

# load pretrained model
refined = Refined.from_pretrained(model_name='wikipedia_model',
                                  entity_set="wikipedia")

# run refined on sample input
texts = [
    "Barack Obama was the 44th President of the United States.",
    "Amazon was founded by Jeff Bezos.",
    "Oslo is the capital of Norway, neighbor to Sweden."
]

# go through text-sample
for text in texts:
    
     # process text
     doc = refined.process_text(text)

     # print links
     for mention in doc.mentions:
         print(f"'{mention.text}' linked to {mention.predicted_entity.wikipedia_title}")