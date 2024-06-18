# import os
# import requests
# import argparse
# import logging

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


# def parse_args():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--path", type=str, help="Path to the weights folder")
#     return parser.parse_args()


# def download_weights(url, save_dir):
#     logger.info("Loading weights...")
#     response = requests.get(url)
#     response.raise_for_status()
#     with open(save_dir, "wb") as f:
#         f.write(response.content)
#     logger.info(f"Model weights saved as {save_dir}")


# def main():
#     args = parse_args()
#     print(f"args: {args}")
#     save_path = os.path.join(args.path, "model.pt")

#     weights_url = "https://openaipublic.blob.core.windows.net/diffusion/jul-2021/256x256_diffusion_uncond.pt"

#     # Ensure the path exists
#     if not os.path.exists(args.path):
#         raise ValueError(f"The provided path does not exist: {args.path}")
#     logger.info(f"Processing path: {args.path}")

#     print("Downloading weights")
#     download_weights(weights_url, save_path)
#     print("Done")

import os
import requests
import argparse
import logging

from tqdm import tqdm

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, help="Path to the weights folder")
    return parser.parse_args()


def download_weights(url, save_dir):
    logger.info("Loading weights...")
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress = tqdm(total=total_size, unit='iB', unit_scale=True)

        with open(save_dir, 'wb') as f:
            for data in response.iter_content(block_size):
                progress.update(len(data))
                f.write(data)
        progress.close()
    logger.info(f"Model weights saved as {save_dir}")


def main():
    args = parse_args()
    save_path = os.path.join(args.path, "model.pt")

    weights_url = "https://openaipublic.blob.core.windows.net/diffusion/jul-2021/256x256_diffusion_uncond.pt"

    # Ensure the path exists
    if not os.path.exists(args.path):
        raise ValueError(f"The provided path does not exist: {args.path}")
    logger.info(f"Processing path: {args.path}")

    print("Downloading weights")
    download_weights(weights_url, save_path)
    print("Done")

if __name__ == "__main__":
    main()

