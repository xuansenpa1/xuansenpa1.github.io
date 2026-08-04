import json
import os
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlencode, urljoin, urlparse

import requests
from bs4 import BeautifulSoup


SCHOLAR_PROFILE_URL = 'https://scholar.google.com/citations'
REQUEST_TIMEOUT_SECONDS = 30


def scholar_url(parameters: dict) -> str:
    return f'{SCHOLAR_PROFILE_URL}?{urlencode(parameters)}'


def fetch_profile_page(scholar_id: str, start: int) -> BeautifulSoup:
    response = requests.get(
        SCHOLAR_PROFILE_URL,
        params={
            'user': scholar_id,
            'hl': 'en',
            'cstart': start,
            'pagesize': 100,
        },
        headers={
            'User-Agent': (
                'Mozilla/5.0 (compatible; GitHub Actions scholar sync; '
                '+https://github.com/xuansenpa1/xuansenpa1.github.io)'
            ),
            'Accept-Language': 'en-US,en;q=0.9',
        },
        timeout=(10, REQUEST_TIMEOUT_SECONDS),
    )
    response.raise_for_status()
    if 'unusual traffic' in response.text.lower() or 'recaptcha' in response.text.lower():
        raise RuntimeError('Google Scholar returned a bot-check page; no homepage data was changed.')
    return BeautifulSoup(response.text, 'html.parser')


def extract_publications(soup: BeautifulSoup, scholar_id: str) -> list[dict]:
    publications = []
    for row in soup.select('tr.gsc_a_tr'):
        title_anchor = row.select_one('a.gsc_a_at')
        if not title_anchor:
            continue
        metadata = row.select('div.gs_gray')
        publication_query = parse_qs(urlparse(title_anchor.get('href', '')).query)
        publication_id = publication_query.get('citation_for_view', [title_anchor.get('href', '')])[0]
        scholar_publication_url = scholar_url({
            'view_op': 'view_citation',
            'hl': 'en',
            'user': scholar_id,
            'citation_for_view': publication_id,
        })
        citation_anchor = row.select_one('td.gsc_a_c a')
        year = row.select_one('span.gsc_a_h, span.gsc_a_y')
        publications.append({
            'id': publication_id,
            'title': title_anchor.get_text(' ', strip=True),
            'authors': metadata[0].get_text(' ', strip=True) if metadata else '',
            'venue': metadata[1].get_text(' ', strip=True) if len(metadata) > 1 else '',
            'year': year.get_text(' ', strip=True) if year else '',
            'url': urljoin(SCHOLAR_PROFILE_URL, title_anchor.get('href', '')),
            'scholar_url': scholar_publication_url,
            'citations': int(citation_anchor.get_text(strip=True)) if citation_anchor and citation_anchor.get_text(strip=True).isdigit() else 0,
        })
    return publications


def main() -> None:
    scholar_id = os.environ['GOOGLE_SCHOLAR_ID']
    first_page = fetch_profile_page(scholar_id, 0)
    author_name = first_page.select_one('#gsc_prf_in')
    if not author_name:
        raise RuntimeError('Google Scholar did not return an author profile; no homepage data was changed.')

    publications = extract_publications(first_page, scholar_id)
    publications.sort(key=lambda publication: (publication['year'], publication['title']), reverse=True)
    citation_cells = first_page.select('#gsc_rsb_st td.gsc_rsb_std')
    cited_by = int(citation_cells[0].get_text(strip=True)) if citation_cells and citation_cells[0].get_text(strip=True).isdigit() else 0
    updated = datetime.now(timezone.utc).isoformat()

    os.makedirs('results', exist_ok=True)
    raw_publications = {
        publication['id']: {'num_citations': publication['citations']}
        for publication in publications
    }
    with open('results/gs_data.json', 'w') as output_file:
        json.dump({
            'name': author_name.get_text(' ', strip=True),
            'citedby': cited_by,
            'updated': updated,
            'publications': raw_publications,
        }, output_file, ensure_ascii=False, indent=2)
    with open('results/gs_publications.json', 'w') as output_file:
        json.dump({'updated': updated, 'publications': publications}, output_file, ensure_ascii=False, indent=2)
    with open('results/gs_data_shieldsio.json', 'w') as output_file:
        json.dump({
            'schemaVersion': 1,
            'label': 'citations',
            'message': str(cited_by),
        }, output_file, ensure_ascii=False)


if __name__ == '__main__':
    main()
