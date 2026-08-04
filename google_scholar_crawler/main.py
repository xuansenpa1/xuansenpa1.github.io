from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime, timezone
import os
from urllib.parse import urlencode

scholar_id = os.environ['GOOGLE_SCHOLAR_ID']
author: dict = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = datetime.now(timezone.utc).isoformat()
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)


def publication_record(publication_id: str, publication: dict) -> dict:
    """Convert Scholar's author-publication entry into safe homepage data."""
    bib = publication.get('bib', {})
    paper_url = publication.get('pub_url') or publication.get('eprint_url')
    scholar_url = 'https://scholar.google.com/citations?' + urlencode({
        'view_op': 'view_citation',
        'hl': 'en',
        'user': scholar_id,
        'citation_for_view': publication_id,
    })
    return {
        'id': publication_id,
        'title': bib.get('title', 'Untitled publication'),
        'authors': bib.get('author', ''),
        'year': str(bib.get('pub_year', bib.get('year', ''))),
        'venue': bib.get('venue', bib.get('journal', bib.get('conference', bib.get('citation', '')))),
        'url': paper_url or scholar_url,
        'scholar_url': scholar_url,
        'citations': publication.get('num_citations', 0),
    }


homepage_publications = [
    publication_record(publication_id, publication)
    for publication_id, publication in author['publications'].items()
]
homepage_publications.sort(key=lambda publication: (publication['year'], publication['title']), reverse=True)
with open('results/gs_publications.json', 'w') as outfile:
    json.dump({
        'updated': author['updated'],
        'publications': homepage_publications,
    }, outfile, ensure_ascii=False, indent=2)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
