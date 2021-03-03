from kedro.pipeline import Pipeline, node
import sys
import os
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(FILE_DIR + "/../../")
from data import scraping_indoor_scene_images

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=scraping_indoor_scene_images.scraping_indoor_scene_images,
                inputs=["parameters"],
                outputs="scraping_indoor_scene_images_df"
            )
        ]
    )
