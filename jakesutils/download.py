import requests
from tqdm import tqdm


def download_file(url: str, name: str):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(name, "wb+") as f:
            for chunk in tqdm(r.iter_content(chunk_size=8192)):
                if chunk:
                    f.write(chunk)
