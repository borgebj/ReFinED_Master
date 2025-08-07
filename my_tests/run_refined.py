
from my_tests.process_file import process_csv
from refined.inference.processor import Refined

refined = Refined.from_pretrained(model_name='wikipedia_model_with_numbers',
                                  entity_set="wikipedia")

# texts = [
#     "England won the FIFA World Cup in 1966.",
#     "Barack Obama was the 44th President of the United States.",
#     "Amazon was founded by Jeff Bezos.",
#     "Oslo is the capital of Norway, neighbor to Sweden."
# ]
#
texts = process_csv("my_tests/data/imdb_top_100.csv")

for text in texts:
    print(f'\n{text}')

# for text in texts[:10]:  # Test first 5 rows
#     print(f'\n{text}')
#
#     spans = refined.process_text(text)
#     for span in spans:
#         print(f"  {span.text} → {getattr(span.predicted_entity, 'wikipedia_entity_title', None)}")
#     print()