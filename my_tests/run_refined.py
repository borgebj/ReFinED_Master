from refined.inference.processor import Refined

refined = Refined.from_pretrained(
    model_name='wikipedia_model_with_numbers',
    entity_set="wikipedia"
)

texts = [
    "England won the FIFA World Cup in 1966.",
    "Barack Obama was the 44th President of the United States.",
    "Amazon was founded by Jeff Bezos.",
    "Oslo is the capital of Norway, neighbor to Sweden."
]

for text in texts:
    print(f"\n{text}")
    for span in refined.process_text(text):
        entity = span.predicted_entity
        title = getattr(entity, "wikipedia_entity_title", getattr(entity, "parsed_string", "None"))
        print(f"  {span.text} → {title}")
