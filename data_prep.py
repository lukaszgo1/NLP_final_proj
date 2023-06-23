import pathlib

import pandas as pd

DS_PATH = pathlib.Path(__file__).parent.parent / "aclImdb" / "test"


def fill_with_reviews(reviews_dir: str, df: pd.DataFrame, sent: int) -> None:
    for review_file in (DS_PATH / reviews_dir).iterdir():
        with open(review_file, "r", encoding="utf-8") as f:
            review_text = f.read()
            df.loc[len(df)] = [review_text, sent]


def main() -> None:
    df = pd.DataFrame(
        {
            "review_text": pd.Series(dtype='str'),
            "sentiment": pd.Series(dtype='int')
        }
    )
    fill_with_reviews("neg", df, 0)
    fill_with_reviews("pos", df, 1)
    df.to_csv("movie_reviews.csv", sep=";", index_label="review_id")


if __name__ == "__main__":
    main()
