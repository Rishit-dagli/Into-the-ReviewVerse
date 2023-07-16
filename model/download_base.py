import fire

from huggingface_hub import snapshot_download


def main(
    base_model_names: str = "",
):
    """
    Download and cache base models form Hugging Face.

    :param base_model_names: Base model names from HuggingFace, For example: 'decapoda-research/llama-7b-hf'.
    """

    assert base_model_names, "Need a base model"

    base_model_names_list = base_model_names.split(",")
    base_model_names_list = [name.strip() for name in base_model_names_list]

    print(f"Base models: {', '.join(base_model_names_list)}.")

    for name in base_model_names_list:
        print(f"Preparing {name}...")
        snapshot_download(name)

    print("Downloaded base models")


if __name__ == "__main__":
    fire.Fire(main)
